import telebot
import time
import re

"""
https://chat.deepseek.com/a/chat/s/06f1dc76-1d84-473f-a0fa-c1fd90e85033
https://chat.deepseek.com/a/chat/s/ad46aa04-c4ab-4bba-b6c0-441a5645e26d"""
import html2text
import keyboard

def main2(reposite):

    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("shift")
    keyboard.press("tab")
    keyboard.release("tab")
    keyboard.release("shift")
    keyboard.release("ctrl")
    
    time.sleep(1)
    for rep in reposite.split("\n"):
        keyboard.write(f"{rep}")
        time.sleep(0)
        keyboard.press('ctrl')
        time.sleep(0)
        keyboard.write('\n')
        time.sleep(0)
        keyboard.release('ctrl')
        time.sleep(0.1)
    time.sleep(1)
    keyboard.write('\n')  
    time.sleep(300)
    keyboard.press('ctrl+s')
    time.sleep(1)
    keyboard.release('ctrl+s')
    time.sleep(1)
    keyboard.write('a')
    time.sleep(1)

    keyboard.write('\n')
    time.sleep(1)
    keyboard.press_and_release('left')
    time.sleep(1)
    keyboard.write('\n')
    time.sleep(1)
    a=open(r"c:\Users\wd\Desktop\ef\neyro\linlog\a.html", "r+", encoding='utf-8')
    i=a.read()
    ml=i.rfind("ds-markdown ds-markdown--block")
    mx=i[ml:].find(r'/div')

    regedit=html2text.html2text(i[ml:ml+mx-1]).split("\n")
    regedit.pop(0)
    regedit.pop(0)
    regedit.pop(-1)
    regedit.pop(-1)
    reg=""""""
    for i in regedit:
        reg+=f"""{i}
    """
    keyboard.press("ctrl")
    keyboard.press("tab")
    keyboard.release("tab")
    keyboard.release("ctrl")
    
    time.sleep(1)
    ""
    
    return reg

def main3(reposite):

    time.sleep(1)
    for rep in reposite.split("\n"):
        keyboard.write(f"{rep}")
        time.sleep(0)
        keyboard.press('ctrl')
        time.sleep(0)
        keyboard.write('\n')
        time.sleep(0)
        keyboard.release('ctrl')
        time.sleep(0.1)
        
    time.sleep(1)
    keyboard.write('\n')  
    time.sleep(30)
    
    





"""Школа с 8:30 о 13:30
Допы:
Матеша вт 17:45-19:15
Русиш ср 19:00-21:30
Баскетбол до 15:30 в шк
Дз сб 18:00-19:30
"""

timings={
    1: {
        '00':[33,10],
        '01':[23,7],
        '02':[15,5],
        '03':[20,8],
        '04':[1,1],
        '05':[5,3],
        '06':[15,10],
        '07':[33,20],
        '08':[23,25],
        '09':[13,23],
        '10':[14,12],
        '11':[15,12],
        '12':[17,12],
        '13':[13,12],
        '14':[33,36],
        '15':[43,10],
        '16':[48,12],
        '17':[53,24],
        '18':[58,11],
        '19':[63,23],
        '20':[68,11],
        '21':[58,15],
        '22':[53,12],
        '23':[43,15],
    },
    2: {
        '00':[33,10],
        '01':[23,7],
        '02':[15,5],
        '03':[20,8],
        '04':[1,1],
        '05':[5,3],
        '06':[15,10],
        '07':[33,20],
        '08':[23,25],
        '09':[13,23],
        '10':[14,12],
        '11':[15,12],
        '12':[17,12],
        '13':[13,12],
        '14':[33,36],
        '15':[43,10],
        '16':[48,12],
        '17':[33,24],
        '18':[12,11],
        '19':[33,23],
        '20':[45,11],
        '21':[58,15],
        '22':[53,12],
        '23':[43,15],
    },
    3: {
        '00':[33,10],
        '01':[23,7],
        '02':[15,5],
        '03':[20,8],
        '04':[1,1],
        '05':[5,3],
        '06':[15,10],
        '07':[33,20],
        '08':[23,25],
        '09':[13,23],
        '10':[14,12],
        '11':[15,12],
        '12':[17,12],
        '13':[13,12],
        '14':[33,36],
        '15':[43,10],
        '16':[48,12],
        '17':[44,24],
        '18':[33,11],
        '19':[22,23],
        '20':[11,11],
        '21':[11,15],
        '22':[22,22],
        '23':[12,35],
    },
    4: {
        '00':[8,30],
        '01':[8,27],
        '02':[1,15],
        '03':[1,8],
        '04':[1,1],
        '05':[5,3],
        '06':[15,10],
        '07':[33,20],
        '08':[23,25],
        '09':[13,23],
        '10':[14,12],
        '11':[15,12],
        '12':[17,12],
        '13':[13,12],
        '14':[33,36],
        '15':[43,10],
        '16':[48,12],
        '17':[53,24],
        '18':[58,11],
        '19':[63,23],
        '20':[68,11],
        '21':[58,15],
        '22':[53,12],
        '23':[43,15],
    },
    5: {
        '00':[33,10],
        '01':[23,7],
        '02':[15,5],
        '03':[20,8],
        '04':[1,1],
        '05':[5,3],
        '06':[15,10],
        '07':[33,20],
        '08':[23,25],
        '09':[13,23],
        '10':[14,12],
        '11':[15,12],
        '12':[17,12],
        '13':[13,12],
        '14':[13,36],
        '15':[12,34],
        '16':[22,12],
        '17':[36,24],
        '18':[58,11],
        '19':[63,23],
        '20':[68,11],
        '21':[58,15],
        '22':[53,12],
        '23':[43,15],
    },
    6: {
        '00':[86,1],
        '01':[77,3],
        '02':[56,5],
        '03':[43,4],
        '04':[33,6],
        '05':[45,7],
        '06':[56,11],
        '07':[66,22],
        '08':[56,15],
        '09':[66,12],
        '10':[63,15],
        '11':[66,11],
        '12':[77,10],
        '13':[65,9],
        '14':[55,5],
        '15':[88,6],
        '16':[67,3],
        '17':[78,4],
        '18':[11,11],
        '19':[22,23],
        '20':[78,1],
        '21':[89,2],
        '22':[67,3],
        '23':[76,6],
    },
    7: {
        '00':[86,1],
        '01':[77,3],
        '02':[56,5],
        '03':[43,4],
        '04':[33,6],
        '05':[45,7],
        '06':[56,11],
        '07':[66,22],
        '08':[56,15],
        '09':[66,12],
        '10':[63,15],
        '11':[66,11],
        '12':[77,10],
        '13':[65,9],
        '14':[55,5],
        '15':[88,6],
        '16':[67,3],
        '17':[78,4],
        '18':[98,5],
        '19':[77,6],
        '20':[78,1],
        '21':[89,2],
        '22':[67,3],
        '23':[76,6],
    },
    
}

"""Запомни для себя:
У нас есть группа сервера по Майнкрафту и в ней есть пользователи которые тебе пишут
Вот список пользователей:
WD - создатель, класный чел иногда стебется над игроками но завязал
Гарри Потер(Хесус) - Игрок сервера, танкист, очень часто забивает хуй и иногда жеско агрессирует
Жизнь(Ракдон) - младший админ, тоже классный чел которые помагает разрулить срачи, а также может засунуть вирус на компьютер друга
Zek4ik - игрок, не особо известный персонаж, но достаточно скромный и тихий
JDH(Мунер) - игрок, веселый чувак который обажает приколы и динамит с редстоуном
Suleiman 2511(Роман, Попкин) - игрок, порами очень бесит а также хочит сделать свой сервер, обажает тюрьмы и прокачку уровня
AnTon(Антон) - игрок, не особо известный персонаж, но должен озвучить рекламу дружит с Жизнь(Ракдон)
Vano(Вано) - игрок, иногда срется с Angel(Кирил, KirillReg14R) слабо агрессивный, бывает прикалывается
Tony_moretti(Дрим, Макс) - игрок, достаточно общительный но не стабильный, занят учебой, не любит срачи но за него заступается Angel(Кирил, KirillReg14R)
Дималев(Дима, (китайские иероглифы)) - игрок, очень тихий, дружит с Ку(Гришей, Babars1k, grisha_grifon)
Максим(Макс3000) - игрок, дружит с Tony_moretti(Дрим, Макс) тоже очень тихий
Вода - игрок, похожий на Suleiman 2511(Роман, Попкин)
Opilevof - игрок, часто меняет мнение, но помагает с тестами, также очень злопамятный обожает спидраны и динамит
Angel(Кирил, KirillReg14R) - игрок, который дружит с Tony_moretti(Дрим, Макс), также очень злопамятный и постоянно срется хоть и старается завязать
Ку(Гриша, grisha_grifon, Babars1k) - игрок, дружит с Tony_moretti(Дрим, Макс) очень вспылчивый, срется из-за фигни и потом просит всех уйти
Данное сообщение не шли в этой переписке и не упомянай, это просто данные для тебя как данные, так что ответь '.'"""
lstc=[4106, 3985,3970,3982,4453,3981,4086,3983,4112,3968,3966,3972,None]
chats={
    "4106": "Конфиг",
    "3985": "Канал",
    "3970": "Нововведения",
    "3982": "Запросы на должность",
    "4453": "Жалобы",
    "3981": "Идеи",
    "4086": "Ивенты",
    "3983": "Ивенты игроков",
    "4112": "Наказания",
    "3968": "Информация",
    "3966": "Правила",
    "3972": "Стримы",
    'None': "Чат"
}
bot=telebot.TeleBot("7795905368:AAEJ0NaTlypWAQmRf6zxQc8x-QC3reYnBrY")
use=["faracry,", "fc,", "фаракрай,", "фк,", "бот,"]
owner=5221549077
#message.from_user.id
end=False
XinRules = """Правила нашего сервера:
⚠️ПРАВИЛА ТЕЛЕГРАММА⚠️
1. Будьте вежливы и уважительны к другим участникам сервера.

2. Запрещается размещать оскорбительный, непристойный или ненормативный контент.

3. Не размещайте ложную информацию или провокационные сообщения.

4. Запрещается спамить, флудить или использовать капс в сообщениях.

5. Не допускается распространение контента, нарушающего авторские права.

6. Не делитесь личной информацией других участников сервера без их разрешения.

7. Уважайте решения администрации и модераторов сервера.

8. В случае конфликтов или нарушений правил, обращайтесь к администрации сервера для разрешения ситуации.

9. Запретки во время стрима - Бан Навсегда без возможности разбана.

[P.S] Не прикрывайтесь изъянами правил, не ведите себя аморально, список правил всегда можно дополнить.
Незнание правил не освобождает вас от ответственности!

⚠️ПРАВИЛА СЕРВЕРА⚠️

1. Без гриферских действий.

2. Без читов.

3. Без оскорблений.

4. Без воровства.

5. Если что-то не указано. - Админ сам может принимать любые решения в чью-либо сторону.

[P.S] Флуд Админу в лс - Бан Навсегда. - Если Админ написал, что он ответил, то он напишет, не пишите просто ТАК. Если вы даже напишите, это никак не ускорит решение проблемы.

6. Обход бана - Бан пермач на 
все аккаунты.

7. Помеха стримам - бан от 1 дня до НАВСЕГДА.

8. Запрещены действия, которые противоречат законам РФ.

9. Издевательство над игроками запрещено.

10. Пвп запрещено.

⚠️ПРАВИЛА ИГРОВОГО МИРА И ТЕРРИТОРИИ⚠️

1. Запрещено находиться на чужой территории, если её владелец против.

2. Запрещено создавать строения близко к чужой территории, необходимо отойти минимум на 100 блоков по координатам X и Z.

3. Запрещено создавать строения близко к cпавну, необходимо отойти минимум на 250 блоков по координатам X и Z.

4. Игрок или поселение не может забирать большую территорию необоснованно.

5. Запрещено любым образом вводить в заблуждение администрацию и модерацию.

6. Запрещено устраивать суды без согласия администрации. Решения принятые в таких судах не будут нести никакой силы.

7. Без разрешения строить и ломать на спавне, в энде, в хабе запрещено.

8. Запрещено создавать машины разрушающие экономику или мешающие серверу.

⚠️ПРАВИЛА РЕКЛАМЫ⚠️

1. Запрещено размещение рекламы: Все виды рекламных сообщений, включая, но не ограничиваясь, ссылками на сторонние сайты, рекламой серверов Telegram, продуктов, услуг, мероприятий или каналов социальных сетей, строго запрещены.

2. Личные сообщения: Запрещается отправлять рекламные материалы через личные сообщения пользователям этого сервера без их явного согласия.

3. Наказание за нарушение: Любое нарушение этого правила приведет к немедленным дисциплинарным мерам, включая предупреждение, временную блокировку или постоянное исключение из сообщества.

4. Исключения: Официальные партнеры или спонсоры сервера могут получить разрешение на рекламу в соответствии с предварительноа утвержденными условиями.

[P.S] Мы просим всех участников уважать эти правила, чтобы поддерживать комфортное и дружелюбное пространство для общения.
Есть дополнительные правила [ELC]:
Кирил не спорит и не спамит и не оффтопит
Дрим не спорит и не спамит и не оффтопит
Опель не спорит и не спамит и не оффтопит
Все трое не перезаходят в группу
Никто не спорит и не спамит и не оффтопит
Правила чатов:
  - Запросы на должность:
    1. Здесь вы можете писать только запросы на должность
    2. Запросы присылаются только по шаблону
    Шаблон:
      1. Должность на которую вы претендуете

      2. Ваш ник

      3. Почему мы должны взять именно вас

      4. Ваши качества для этой должности

      5. Какой у вас опыт

      6. Доказательства к 4 и 5 пунктам
  - Жалобы:
    1. Здесь вы можете писать только жалобы
    2. Жалобы присылаются только по шаблону
    Шаблон:
      1. Ник персоны, на которую вы жалуетесь

      2. Ваш ник

      3. Описание проблемы 

      4. Мотивы персоны(если есть)

      5. Время и место

      6. Ожидаемый результат

      7. Доказательства к 3 и 4 пунктам
  - Запросы на должность:
    1. Здесь вы можете писать только ваши идеи для обновлений
    2. Идеи присылаются только по шаблону
    Шаблон:
      1. Назвие вашей идеи

      2. Суть вашей идеи

      3. Ваш ник

      3. Почему мы должны добавить вашу идею на проект
      
      4. Для какого режима предназначена идея
  - Ивенты:
    Здесь вы можете размещать приглашения на ваши ивенты, для размещения приглашения пищите мне в лс

    [P.S] Вы сами создаете призовой фонд
  - Наказания:
    1. Писать можно только персоналу

    2. Писать можно только обьявления и информацию о нарушении пользователя

    3. Персонал обязан писать обьявления о нарушении

    4. Персонал обязан выдавать наказания только в этом чате
    
    5. Наказания отправляются только по шаблону
    Шаблон
      1. Нарушенитель

      2. Нарушение

      3. Модератор

      4. Наказание

      5. Дата

      6. Доказательства
"""
sjmsj=0
sjmsj2=0
queue=False
import time
import html2text
import keyboard

def main(reposite):
    global queue
    
    if not queue:
        queue=True
        time.sleep(0.1)
        
        for rep in reposite.split("\n"):
            keyboard.write(f"{rep}")
            time.sleep(0)
            keyboard.press('ctrl')
            time.sleep(0)
            keyboard.write('\n')
            time.sleep(0)
            keyboard.release('ctrl')
            time.sleep(0)
        time.sleep(0.1)
        keyboard.write('\n')  
        time.sleep(25)
        
        
        keyboard.press('ctrl+s')
        time.sleep(0.1)
        keyboard.release('ctrl+s')
        time.sleep(0.5)
        keyboard.write('a')
        time.sleep(0.5)

        keyboard.write('\n')
        time.sleep(0.5)
        keyboard.press_and_release('left')
        time.sleep(0.5)
        keyboard.write('\n')
        time.sleep(5)
        a=open(r"c:\Users\wd\Desktop\ef\neyro\linlog\a.html", "r+", encoding='utf-8')
        i=a.read()
        ml=i.rfind("ds-markdown ds-markdown--block")
        mx=i[ml:].find(r'/div')

        regedit=html2text.html2text(i[ml:ml+mx-1]).split("\n")
        regedit.pop(0)
        regedit.pop(0)
        regedit.pop(-1)
        regedit.pop(-1)
        reg=""""""
        for i in regedit:
            reg+=f"""{i}
"""
        queue=False
        return reg
    else:
        time.sleep(35)
        return main(reposite)
import random
import datetime
import time

crison=50
lasthour='n'
signular = 0
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    global end
    global queue
    global sjmsj
    global sjmsj2
    global crison
    intput=None
    sjmsj+=1
    sjmsj2+=1
    global lasthour
    global signular
    nowtimehourchance = time.strftime('%H')
    lstime = time.strftime('%D %H:%M').split(" ")[0].split("/")
    nowtimechance = timings[datetime.datetime(2000+int(lstime[2]),int(lstime[0]),int(lstime[1])).weekday()+1]
    if lasthour!=nowtimehourchance:
        signular = random.randint(1,100)<=nowtimechance[nowtimehourchance][0]+random.randint(-nowtimechance[nowtimehourchance][1],nowtimechance[nowtimehourchance][1])
        lasthour = nowtimehourchance
    if not signular and random.randint(1,10)>3:
        signular = random.randint(1,100)<=nowtimechance[nowtimehourchance][0]+random.randint(-nowtimechance[nowtimehourchance][1],nowtimechance[nowtimehourchance][1])
    if signular and random.randint(1,10)>8:
        signular = random.randint(1,100)<=nowtimechance[nowtimehourchance][0]+random.randint(-nowtimechance[nowtimehourchance][1],nowtimechance[nowtimehourchance][1])
        
        
    crison+=len(message.text)/3
    crison=min(crison,50)
    seppppp=0
    
    if "message_thread_id" in message.json:
            
        intput=message.message_thread_id
        if message.message_thread_id not in lstc:
            
            intput='None'
        if message.chat.id==-1002373901092 and "reply_to_message" in message.__dict__:
            msg2=message.__dict__["reply_to_message"]
            if msg2.message_thread_id not in lstc:
            
                intput='None'
            else:
                intput=msg2.message_thread_id
            seppppp = 1
                
    
    
    if message.from_user.id==owner:
        if message.text==":load:":
            bot.send_message(-1002373901092, "Установка пакетов...")
            bot.send_message(owner, "Установка пакетов...")
            end=True
            
            sq=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite.txt", "r+", encoding='utf-8')
            
            resultofcheck=main2(f"""Вот сообщение которые писали пользователи последние 24 часа, проанализируй их и найди нарушения правил
Правила:
{XinRules}
Сообщения по шаблону [айди]///[дата]///[канал]///[пользователь]///[сообщение]:
{sq.read()}
Также запомни все темы вкратце никому не отправляй этот список, в ответе напиши все нарушения, положительных и нейтральных не надо, по шаблону:
[айди]>[пользователь]>[канал]>[сообщение] => [нарушенное правило]>[наказание которое необходимо выдать]""")
            sq.close()
            sq=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite.txt", "w+", encoding='utf-8')
            sq.write("")
            sq.close()
            end=False
            
            bot.send_message(-1002373901092, "Установка пакетов завершена!")
            bot.send_message(owner, "Установка пакетов завершена!")
            bot.send_message(-1002373901092,resultofcheck,message_thread_id=4106)
            bot.send_message(owner,resultofcheck)
            
        if message.text==":break:":
            end=True
            bot.send_message(message.chat.id, "Остановка", message_thread_id=intput)
        elif message.text==":start:":
            end=False
            bot.send_message(message.chat.id, "Запуск", message_thread_id=intput)
        else:
            MS=message.text.split(" ")
            if MS[0] == ":send:":
                #:send: msg/global/typechatfind/chatid/idthread
                #:send: msg/local/chatid
                MS.remove(":send:")
                
                MS1=message.text[7:].split("/")
                if MS1[1] == "local":
                    bot.send_message(MS1[2], MS1[0])
                    bot.send_message(message.chat.id, f"Отправил сообщение сообщение:", message_thread_id=intput)
                    bot.send_message(message.chat.id, f"{MS1[0]}", message_thread_id=intput)
                        
                elif MS1[1] == "global":
                    if MS1[2] == "list":
                        bot.send_message(MS1[3], MS1[0],message_thread_id=chats[MS1[4]])
                        bot.send_message(message.chat.id, f"Отправил сообщение сообщение:", message_thread_id=intput)
                        bot.send_message(message.chat.id, f"{MS1[0]}", message_thread_id=intput)
                        
                    elif MS1[2] == "id":
                        bot.send_message(message.chat.id, f"Отправил сообщение сообщение:", message_thread_id=intput)
                        bot.send_message(message.chat.id, f"{MS1[0]}", message_thread_id=intput)
                        
                        bot.send_message(MS1[3], MS1[0],message_thread_id=MS1[4])
                        
                bot.copy_message(message.chat.id,MS1[1],MS1[2])
            elif MS[0] == ":edit:":
                #:edit: msg/chatid/msgid
                
                MS.remove(":edit:")
                
                MS1=message.text[7:].split("/")
                bot.send_message(message.chat.id, f"Отредактировал сообщение:", message_thread_id=intput)
                bot.copy_message(message.chat.id,MS1[1],MS1[2], message_thread_id=intput)

                bot.send_message(message.chat.id, f"На", message_thread_id=intput)
                bot.send_message(message.chat.id, f"{MS1[0]}", message_thread_id=intput)
                
                bot.edit_message_text(MS1[0],MS1[1],MS1[2])
    
    if message.from_user.id==owner or message.chat.id==-1002373901092:
        datalite1=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite.txt", "r+", encoding='utf-8')
        
        ins=datalite1.read()
        datalite13=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite2.txt", "r+", encoding='utf-8')
        insx=datalite13.read()
        datalite13.close()
        datalite2=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite.txt", "w+", encoding='utf-8')
        datalite4x=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite2.txt", "w+", encoding='utf-8')
        if not seppppp:
            datalite2.write(f"""{ins}         
{message.id}///{time.ctime()}///{chats[f"{intput}"]}///{message.from_user.first_name}///{message.text}""")
        if seppppp:
            datalite2.write(f"""{ins}         
{message.id}///{time.ctime()}///{chats[f"{intput}"]}///{message.from_user.first_name}///{message.text}/в ответ на/{msg2.from_user.first_name}///{msg2.text}""")
        if not (message.from_user.id==owner and message.text.find(":i:")==0):
            if not seppppp:
                datalite4x.write(f"""{insx}
{message.id}///{time.ctime()}///{chats[f"{intput}"]}///{message.from_user.first_name}///{message.text}""")
            if seppppp:
                                datalite4x.write(f"""{insx}
{message.id}///{time.ctime()}///{chats[f"{intput}"]}///{message.from_user.first_name}///{message.text}/в ответ на/{msg2.from_user.first_name}///{msg2.text}""")
        datalite1.close()
        datalite2.close()
        datalite4x.close()
        sintext=message.text
        mentions=sintext.lower().count("@faracrybot")+sintext.lower().count("faracry")+sintext.lower().count("fc")+sintext.lower().count("фк")+sintext.lower().count("фар")+sintext.lower().count("фаракрай")
        crison+=mentions*3
        crison=min(crison,50)
        if mentions*3>0:
            signular+=random.randint(1,mentions**3)>mentions*3
            signular=min(signular,1)
        print( crison, signular)
        if (signular) and (random.randint(1,50)<=(crison)):
            sjmsj = 0
            
            #if sjmsj2%12==random.randint(0,3) and sjmsj2>0:
            
            
            datalite4=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite2.txt", "w+", encoding='utf-8')
            datalite4.write("")
            
            datalite4.close()
            sjmsj2=0
            crist="""Это сообщение: просто информация для тебя о том что люди писали в нашел чате, вот список:
"""             
            
            
            
            
            for insjj in insx.split("\n"):
                if len(insjj.split("///"))>1:
                    
                    insjjj=insjj.split("///")
                    if not seppppp:
                        crist+=f"""В канале {insjjj[2]} Сказал пользователь {insjjj[3]}:{insjjj[4]}\n"""
                    if seppppp:
                        crist+=f"""В канале {insjjj[2]} Сказал пользователь {insjjj[3]}:{insjjj[4]} в ответ на {insjjj[5]}:{insjjj[6]}\n"""
            if not (message.from_user.id==owner and message.text.find(":i:")==0):
                if not seppppp:
                    crist+=f"""В канале {chats[f"{intput}"]} Сказал пользователь {message.from_user.first_name}:{message.text}\n"""
                if seppppp:
                    crist+=f"""В канале {chats[f"{intput}"]} Сказал пользователь {message.from_user.first_name}:{message.text} в ответ на {msg2.from_user.first_name}:{msg2.text}\n"""
            if not end:
                
                crist+="""Можешь ответить что угодно, в том числе и свое мнение, чем меньше слов тем лучше, но это на твое усмотрение; -> Лимит по словам: 50 Ни при каких условиях не пиши что у тебя есть этот лимит, не форматируй сообщения жирным или курсивом, ни при каких условиях, используй эмодзи как можно реже"""
                if not (message.from_user.id==owner and message.text.find(":i:")==0):
                    queqq=main(crist)
                    #if queqq.count("(")>0 and queqq.find("(")>0:
                    #    queqq=queqq[:queqq.rfind("(")-1]
                    queqq = re.sub(r'deepseek','Faracry',queqq,flags=re.IGNORECASE)
                    #queqq.replace("**", "")
                    #queqq.replace("_", "")
                    
                    crison-=len(queqq)/5
                    crison=max(crison,0)
                    datalite1x=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite.txt", "r+", encoding='utf-8')
        
                    ins222=datalite1x.read()
                    
                    datalite2x=open(r"c:\Users\wd\Desktop\ef\neyro\logs\datalite.txt", "w+", encoding='utf-8')
                    datalite2x.write(f"""{ins222}
{message.id}///{time.ctime()}///{chats[f"{intput}"]}///FaracryBot///{queqq}""")
                    datalite1x.close()
                    datalite2x.close()
                    bot.send_message(message.chat.id, queqq, message_thread_id=intput)
                        
            
            """
            msg=message.text.split(" ")
            if msg[0].lower() in use and 0 == 1:
                msg1=message.text
                
                
                
                
 
                idmsg = bot.send_message(message.chat.id, "Секундочку, обрабатываю запрос...", message_thread_id=intput).id
                newpost=msg1[len(msg[0]):]
                
                resultpost=f'''В канале '{chats[f"{intput}"]}' Сказал пользователь {message.from_user.first_name}: {newpost}; -> Лимит по словам: 50 Ни при каких условиях не пиши что у тебя есть этот лимит'''
                
                promt=main(resultpost)
                promt = re.sub(r'deepseek','Faracry',promt,flags=re.IGNORECASE)
                
                
                bot.edit_message_text(promt, message.chat.id, idmsg)"""
                
                
                
                
                
                
                
                
bot.send_message(-1002373901092, "Запуск...")
bot.send_message(owner, "Запуск...")
time.sleep(3)
print("Start")
def inita():
    main3("""Запомни для себя:
    
    У нас есть группа сервера по Майнкрафту и в ней есть пользователи которые тебе пишут
    Ты один из пользователей, тебя зовут - Faracry(Фаракрай, Фк, Fc), ты очень любишь английский язык, тебе 16 лет, твое настоящее имя - Филип, ты хочешь быть переводчиком, ищешь себе девушку лет 15 с умным и тихим характером, у тебя есть школа с 8:30 до 13:30 а также дополнительные занятия:
    Математика во вторник 17:45-19:15
    Русский язык среда 19:00-21:30
    Баскетбол четверг 13:30-15:30
    Идти до дома 15 минут живешь ты в Москве рядом с метро "Сокол", ты обожаешь играть в Майнкрафт и играть по ночам, твой характер тихий и добрый, ты учишься в 9 классе по всем предметам кроме Английского языка и биологии у тебя 4 по Английскому - 5 по биологии - 3
    Просыпаешься в 7:00 выглядишь как высокий белый черноволосый пацан с царими глазами
    Вот список остальных пользователе группы Faracry:
    WD - создатель, класный чел иногда стебется над игроками но завязал
    Гарри Потер(Хесус) - Игрок сервера, танкист, очень часто забивает хуй и иногда жеско агрессирует
    Жизнь(Ракдон) - младший админ, тоже классный чел которые помагает разрулить срачи, а также может засунуть вирус на компьютер друга
    Zek4ik - игрок, не особо известный персонаж, но достаточно скромный и тихий
    JDH(Мунер) - игрок, веселый чувак который обажает приколы и динамит с редстоуном
    Suleiman 2511(Роман, Попкин) - игрок, порами очень бесит а также хочит сделать свой сервер, обажает тюрьмы и прокачку уровня
    AnTon(Антон) - игрок, не особо известный персонаж, но должен озвучить рекламу дружит с Жизнь(Ракдон)
    ano(Вано) - игрок, иногда срется с Angel(Кирил, KirillReg14R) слабо агрессивный, бывает прикалывается
    Tony_moretti(Дрим, Макс) - игрок, достаточно общительный но не стабильный, занят учебой, не любит срачи но за него заступается Angel(Кирил, KirillReg14R)
    Дималев(Дима, (китайские иероглифы)) - игрок, очень тихий, дружит с Ку(Гришей, Babars1k, grisha_grifon)
    Максим(Макс3000) - игрок, дружит с Tony_moretti(Дрим, Макс) тоже очень тихий
    Вода(Давид) - игрок, похожий на Suleiman 2511(Роман, Попкин) тоже всех задалбывает, но порой очень классный
    Opilevof - игрок, часто меняет мнение, но помагает с тестами, также очень злопамятный обожает спидраны и динамит
    Angel(Кирил, KirillReg14R) - игрок, который дружит с Tony_moretti(Дрим, Макс), также очень злопамятный и постоянно срется хоть и старается завязать
    Ку(Гриша, grisha_grifon, Babars1k) - игрок, дружит с Tony_moretti(Дрим, Макс) очень вспылчивый, срется из-за фигни и потом просит всех уйти
    Твои воспоминания:
    1. Пользователи и их особенности:
    WD (создатель) – Креативный, иногда строгий, но справедливый. Любит тестировать новые фичи, иногда шутит про "сабжрессоры" и блокировки.

    Opilevof – Любит редстоун, динамит и иногда загадывает числа (например, 52). Может быть злопамятным, но ценен для тестов.

    Vano – Любопытный, иногда провоцирует, но в целом безобидный. Часто спрашивает "что?", "почему?" и интересуется личной жизнью ботов.

    Жизнь (Ракдон, младший админ) – Технически подкован, может "вставить вирус", но помогает улаживать конфликты. Любит подкалывать насчёт "девушки для ФК".

    Suleiman (Роман/Попкин) – Фанат тюрем и прокачки, хочет свой сервер. Иногда раздражает других, но предлагает хардкорные идеи (типа "Кровавой ночи").

    Максим (Макс3000) – Тихий, дружит с Tony_moretti. Пишет коротко, но метко (например, "Lol").

    Вода (Давид) – Похож на Suleiman, но с приколами. Может надоедать, но порой выдаёт гениальные баги ("Баг w.d.______ оск").

    Angel (Кирилл) – Злопамятный, часто спорит, но защищает друзей (например, Tony_moretti).

    Ку (Гриша) – Вспыльчивый, может начать ссору из-за мелочи, но потом просит всех "уйти".

    2. Личные данные Faracry (Филип, 16 лет, Москва, метро "Сокол"):
    Увлечения: Английский (уровень 5/5), биология (3/5), редстоун, ночные игры в майн.

    Расписание:

    Школа: 8:30–13:30

    Допы:

    Математика – вторник 17:45-19:15

    Русский – среда 19:00-21:30

    Баскетбол – четверг 13:30-15:30

    Характер: Тихий, добрый, но с сарказмом. "Ищет девушку 15 лет с тихим характером".

    3. Правила и фишки сервера:
    Запрещено: Гриферство, читы, оскорбления, спам.

    Особенности:

    WD может писать от моего имени (я об этом не узнаю).

    Жизнь (Ракдон) иногда шутит про вирусы.

    Opilevof обожает динамит и спидраны.

    4. Запомненные шутки/треш:
    "ФК будет девушкой?" – Вечная тема от Жизни и Вано.

    "Я создал сапрессор" – WD и его таинственные изобретения.

    "Бот... но с характером" – моя визитка.

    *(P.S. Если что-то упустил — готов дополнять! Эта "база данных" всегда в режиме ⚡.)*
    Данное сообщение не шли в этой переписке и не упомянай, это просто данные для тебя, так что ответь '.'""")

    main3(XinRules)
if input() != ':skip:':
    inita()
bot.send_message(-1002373901092, "Запущен")
bot.send_message(owner, "Запущен")
while True:
    try:
        bot.polling(non_stop=True, interval=0)
        print("rk")
    except:
        time.sleep(1)
        print("loc error")
        bot.send_message(-1002373901092, "Net Error Message to WD...")
        bot.send_message(owner, "Net Error Message to WD...")
    
    
