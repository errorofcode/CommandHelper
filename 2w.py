#!/usr/bin/env python3
"""
monitor_files_by_proc.py - Windows версия

Функции:
- Запуск процесса через --run "C:\\path\\to\\program.exe"
- Мониторинг процессов по имени (ввод в консоли)
- Отслеживание создания, удаления и изменения файлов
- Вывод в консоль

Требования:
pip install psutil
"""

import argparse
import psutil
import subprocess
import threading
import time
import os
from pathlib import Path
import hashlib

POLL_INTERVAL = 1.0  # секунды

# -----------------------
# Хелперы
# -----------------------
def hash_file(path):
    """Возвращает SHA256 хеш файла, если он существует, иначе None"""
    try:
        with open(path, "rb") as f:
            h = hashlib.sha256()
            while chunk := f.read(8192):
                h.update(chunk)
            return h.hexdigest()
    except:
        return None

def list_procs_by_name(name):
    """Возвращает список psutil.Process по имени (case-insensitive)"""
    res = []
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        try:
            n = (p.info.get("name") or "")
            if n.lower() == name.lower():
                res.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return res

# -----------------------
# Мониторинг файлов процесса
# -----------------------
class FileMonitor:
    def __init__(self, pid):
        self.pid = pid
        try:
            self.proc = psutil.Process(pid)
        except psutil.NoSuchProcess:
            self.proc = None
        self.prev_files = {}  # path -> (exists, mtime)
        self.lock = threading.Lock()
        self.active = True

    def scan(self):
        """
        Проверяет открытые файлы + все файлы в рабочем каталоге процесса
        """
        if not self.proc or not psutil.pid_exists(self.pid):
            return False

        # 1) Собираем открытые файлы через psutil
        try:
            open_files = self.proc.open_files()
            paths = [f.path for f in open_files]
        except (psutil.AccessDenied, Exception):
            paths = []

        # 2) Добавляем текущую рабочую директорию
        try:
            cwd = self.proc.cwd()
            # Рекурсивно все файлы в cwd (можно ограничить глубину)
            for root, dirs, files in os.walk(cwd):
                for f in files:
                    paths.append(os.path.join(root, f))
        except (psutil.AccessDenied, Exception):
            pass

        # 3) Удаляем дубли
        paths = list(set(paths))

        # 4) Проверяем состояния файлов
        events = []
        current_state = {}
        for p in paths:
            try:
                mtime = os.path.getmtime(p)
                exists = True
            except FileNotFoundError:
                mtime = None
                exists = False
            current_state[p] = (exists, mtime)

            if p not in self.prev_files:
                if exists:
                    events.append(f"CREATED -> {p}")
            else:
                prev_exists, prev_mtime = self.prev_files[p]
                if exists and prev_exists and mtime != prev_mtime:
                    events.append(f"MODIFIED -> {p}")
                if not exists and prev_exists:
                    events.append(f"DELETED -> {p}")

        # Проверка на удалённые файлы
        for p in self.prev_files:
            if p not in current_state and self.prev_files[p][0]:
                events.append(f"DELETED -> {p}")

        self.prev_files = current_state
        return events

    def run(self):
        print(f"[Monitor] PID={self.pid}, Name={self.proc.name() if self.proc else 'unknown'} started monitoring")
        while self.active and self.proc and psutil.pid_exists(self.pid):
            events = self.scan()
            for e in events:
                print(f"[PID {self.pid}] {e}")
            time.sleep(POLL_INTERVAL)
        print(f"[Monitor] PID={self.pid} ended monitoring")

# -----------------------
# Менеджер мониторинга
# -----------------------
class MonitorManager:
    def __init__(self):
        self.threads = {}

    def start_monitor_for_pid(self, pid):
        if pid in self.threads:
            print(f"[Monitor] PID {pid} уже мониторится")
            return
        fm = FileMonitor(pid)
        t = threading.Thread(target=fm.run, daemon=True)
        self.threads[pid] = (t, fm)
        t.start()

    def start_monitor_for_name(self, name):
        procs = list_procs_by_name(name)
        if not procs:
            print(f"[Monitor] Процессы с именем '{name}' не найдены")
            return
        for p in procs:
            self.start_monitor_for_pid(p.pid)

# -----------------------
# Ввод имени процесса
# -----------------------
def input_thread_fn(mgr: MonitorManager):
    print("Ввод: введите имя процесса (например 'notepad.exe') и нажмите Enter.")
    print("Команда 'exit' завершит ввод.")
    while True:
        try:
            s = input("process_name> ").strip()
        except EOFError:
            break
        if not s:
            continue
        if s.lower() in ("exit", "quit"):
            break
        mgr.start_monitor_for_name(s)

# -----------------------
# Запуск процесса через --run
# -----------------------
def run_subprocess(cmdline):
    import shlex
    if isinstance(cmdline, str):
        cmd = shlex.split(cmdline)
    else:
        cmd = cmdline
    try:
        proc = subprocess.Popen(cmd)
        time.sleep(0.1)  # дать psutil время увидеть процесс
        p = psutil.Process(proc.pid)
        print(f"[Run] PID={p.pid}, Name={p.name()}, cmdline={p.cmdline()}")
        return p
    except Exception as e:
        print(f"[Error] Не удалось запустить процесс: {e}")
        return None

# -----------------------
# Main
# -----------------------
def main():
    parser = argparse.ArgumentParser(description="Monitor file actions by process name/PID (Windows)")
    parser.add_argument("--run", "-r", help="Запустить процесс для мониторинга, например --run \"C:\\Windows\\notepad.exe\"")
    args = parser.parse_args()

    mgr = MonitorManager()

    # Если указано --run
    if args.run:
        p = run_subprocess(args.run)
        if p:
            mgr.start_monitor_for_pid(p.pid)

    # Поток для ввода имени процесса
    t = threading.Thread(target=input_thread_fn, args=(mgr,), daemon=True)
    t.start()

    try:
        while t.is_alive():
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("Ctrl-C — завершение программы")

if __name__ == "__main__":
    main()
