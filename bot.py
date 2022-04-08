import telebot
import random
import datetime as t
import pytz
from telebot import types
import time as tm
from time import time
import MySQLdb
admins=[2095244384]
bot = telebot.TeleBot('5022928871:AAGsIpQzcGa3PJGw_0qhfu7tkQhmtZoies8')
@bot.message_handler(commands=["a"])
def start(message):
    bot.send_message(message.chat.id, 'я сплю не пиши мне')
@bot.message_handler(commands=["r"])
def startt(message):
    text = bot.reply_to(message, "напиши цифру от 1 до 10\n(в чатах в ответ на это сообщение)")
    chatforr = message.chat.id
    bot.register_next_step_handler(text, result)
def result(message):
    aa = 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10
    a = str(random.choice(aa))
    msg = str(message.text)
    if msg.isdigit():
        a = str(random.choice(aa))
        msg = message.text
        if msg == a :
            winner = [message.from_user.first_name, message.from_user.last_name, "(", message.from_user.username, ")", "угадал число"]
            wwiner = str(winner)
            bot.send_message(message.chat.id, wwiner)
        if msg != a :
            send = send = bot.send_message(message.chat.id, 'ты не угадал')
            tm.sleep(1)
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
            bot.register_next_step_handler(send, result)
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "1-/start - приветствие\n2-/help - помощь\n3-/r- игра на угадывание чисел\n4-/knb - камень ножныцы бумага(игра с ботом\n5-/time -время\n6-/reg-регистрация\n7-/unreg-убрать регистрацию\n8-/calc-калькулятор\n9-/mutee (время мута и ответ на сообщение)-мутить человека\n10-/kickk(ответ на сообщение)-кикает человека из группы\n11-/mine-пойти на работу\n 12-/balance-ваш баланс\n13-/top-топ по балансу")
@bot.message_handler(commands=["start"])
def startsr(message):
    bot.send_message(message.chat.id, 'привет, я бот которого зовут five_bot, на данный момент я нахожусь на стадии разработки и еще не готов,так как во мне очень много багов и недоработок которые создатель уже пытаеться фиксить так же в будующем я смогу присылать новости и играть в различные игры,одна из которых разрабатываеться в данный момент,помощь по командам:\n/help\nпо всем вопросам:\nhttps://t.me/lllllllllllllll_l_l\n(туда же и баги)  ')
@bot.message_handler(commands=["yandex"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
@bot.message_handler(commands=["time"])
def any_msg(message):
    moscow_time = t.datetime.now(pytz.timezone('Europe/Moscow'))
    mmoscow_time = moscow_time.hour, ":", moscow_time.minute, ":", moscow_time.second
    mmm = str(mmoscow_time)
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, mmm)
@bot.message_handler(content_types=["photo"])
def lol(message):
    bot.send_message(message.chat.id, "красиво")
@bot.message_handler(content_types=["contact"])
def iol(message):
    bot.send_message(message.chat.id, "щас позвоню")
@bot.message_handler(content_types=["sticker"])
def iolf(message):
    bot.send_message(message.chat.id, "прикольно")
@bot.message_handler(content_types=["location"])
def iiolf(message):
    bot.send_message(message.chat.id, "*шипение как из рации, голос говорит : выдвигаемся*")
@bot.message_handler(commands=['reg'])
def asd(message):
    mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
    cur = mydb.cursor()
    com='INSERT INTO reg(id) VALUES(%s);' %(message.from_user.id)
    try:
        cur.execute(com)
        bot.send_message(message.chat.id, "ты зарегестрирован!")
    except:
        bot.send_message(message.chat.id, "ты уже был зарегестрирован")
    mydb.close()
@bot.message_handler(commands=['registr'])
def re(message):
    mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
    cur = mydb.cursor()
    com='SELECT id FROM reg;'
    cur.execute(com)
    result = list(cur.fetchall())
    number = []
    errors=0
    count=0
    data=[]
    for i in result:
        number=[]
        i=list(i)
        for a in i:
            a=str(a)
            if a!=")" or a!="(" or a!=",":
                number.append(i)
            else:
                pass
        id=str(number)
        id=id.replace('[','').replace(']','').replace("'"," ").replace(",","")
        data.append(int(id))
    mydb.close()
    print(data)
    for i in data:
        try:
            print(i)
            count += 1
            text=message.text
            bot.send_message(i, text)
        except:
            errors += 1
    count = count - errors
    results_send = "успешно отосланно", count, "сообщений", "не успешно:", errors
    lpop = str(results_send)
    bot.send_message(message.chat.id, lpop)
@bot.message_handler(commands=['send'])
def qwe(message):
    if admins[-0]==message.from_user.id:
        send = bot.send_message(message.chat.id, 'что отослать?')
        bot.register_next_step_handler(send, re)
    else:
        bot.send_message(message.chat.id, "если уж так хочешь сделать рассылку спроси у создателя ботa")
def lollol(message):
    bot.send_message(int(message.text, message))
def fonts(message):
    message = message.text
    send = send = bot.send_message(message.chat.id, 'id?')
    bot.register_next_step_handler(send, lollol)
@bot.message_handler(commands=['sendlsssssssssssssssssssssssssssssssssssssssssssssssssssss'])
def qqqwe(message):
    if message.from_user.id == 2095244384 :
        send = bot.send_message(message.chat.id, 'что отослать?')
        bot.register_next_step_handler(send, fonts)
def ddwe(message):
    text = message.text
    try:
        result = eval(str(text))
        bot.send_message(message.chat.id, result)
    except:
        bot.send_message(message.chat.id, "что-то тут не так,шаришь?")
@bot.message_handler(commands=["calc"])
def dwe(message):
    send = bot.send_message(message.chat.id, 'что решить?')
    bot.register_next_step_handler(send, ddwe)
@bot.message_handler(commands=['knb'])
def starttt(message):
    text = bot.send_message(message.chat.id, "камень,ножницы или бумага\n(в чатах в ответ на это сообщение)")
    chatforr = message.chat.id
    bot.register_next_step_handler(text, resultt)
def resultt(message):
    aa = "камень", "ножницы", "бумага"
    a = random.choice(aa)
    msg = str(message.text)
    if msg == a :
        bot.send_message(message.chat.id, "ничья")
    if msg != a :
        win_lose = "выйграл", "проиграл"
        random2 = random.choice(win_lose)
        if random2 == "проиграл":
            bot.send_message(message.chat.id, 'ты проиграл(')
        if random2 == "выйграл":
            bot.send_message(message.chat.id, 'ты выйграл)')
def sendcode(message):
    if message.from_user.id == 2095244384:
        doccode = open('bot.py', 'rb')
        bot.send_document(message.chat.id, doccode)
@bot.message_handler(commands=['test'])
def any_mhsg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "@", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима")
@bot.message_handler(commands=['stop'])
def stop(message):
    if admins[-0] or admins[-1]==message.from_user.id:
        exit()
        print('ok')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    count = 0
    if call.data == "test":
        count += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=count)
@bot.message_handler(commands =["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Нажми меня", switch_inline_query="Telegram")
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)
@bot.message_handler(commands=['kickk'])
def kick(message):
    a=bot.get_chat_member(message.chat.id, message.from_user.id)
    aa=a.status
    aaa=str(message.reply_to_message.from_user.id)
    if aa=="creator" or aa=="administrator" or message.from_user.id == 2095244384:
        try:
            bot.kick_chat_member(message.chat.id, int(aaa))
        except Exception as exp:
            bot.send_message(message.chat.id, "error \n проверь дал ли ты боту админку")
            print(exp)
    else:
        bot.send_message(message.chat.id, "ты не админ")
@bot.message_handler(commands=['mutee'])
def mute(message):
    a=bot.get_chat_member(message.chat.id, message.from_user.id)
    aa=a.status
    if aa=="creator" or aa=="administrator" or message.from_user.id == 2095244384:
        try:
            bb=str(message.text)
            b=str(message.reply_to_message.from_user.id)
            v=bb.split(" ")
            bot.restrict_chat_member(message.chat.id, b, until_date=time()+int(v[-1]))
        except Exception as exp:
            bot.send_message(message.chat.id, "error\nпроверь дал ли ты боту админку и указал ли время")
            print(exp)
    else:
        bot.send_message(message.chat.id, "ты не админ")
@bot.message_handler(commands=['balance'])
def dsgf(message):
    mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
    cur = mydb.cursor()
    com='SELECT count FROM reg WHERE id=%s;'%(message.from_user.id)
    cur.execute(com)
    result = list(cur.fetchall())
    bot.send_message(message.chat.id, result)
    mydb.close()
@bot.message_handler(commands=['mine'])
def dsgds(message):
    mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
    cur = mydb.cursor()
    com='SELECT time FROM reg WHERE id=%s;'%(message.from_user.id)
    cur.execute(com)
    result = list(cur.fetchall())
    try:
        result=str(result)
        FRMAT = '[(datetime.date(%Y, %m, %d),)]'
        if t.datetime.today()>t.datetime.strptime(result, FRMAT) or t.datetime.today()==t.datetime.strptime(result, FRMAT):
            EndDate = t.datetime.today()+t.timedelta(days=1)
            com='UPDATE `reg` SET `time` = "{}" WHERE id=%s;'.format(EndDate)%(message.from_user.id)
            cur.execute(com)
            com='UPDATE `reg` SET `count` = count + 10 WHERE id=%s;'%(message.from_user.id)
            cur.execute(com)
            com='SELECT count FROM reg WHERE id=%s;'%(message.from_user.id)
            cur.execute(com)
            result = list(cur.fetchall())
            bot.send_message(message.chat.id, "ты поднял бабла,теперь твой баланс: {}".format(result))
        else:
            com='SELECT time FROM reg WHERE id=%s;'%(message.from_user.id)
            cur.execute(com)
            result = str(cur.fetchall())
            result = result.replace("(", "")
            result = result.replace(")", "")
            result = result.replace(",", "")
            result = result.replace("d", "")
            result = result.replace("a", "")
            result = result.replace("t", "")
            result = result.replace("e", "")
            result = result.replace("i", "")
            result = result.replace("m", "")
            result = result.replace(".", "")
            bot.send_message(message.chat.id, "время еще не пришло,ты еще отдыхаешь,ты пойдешь на работу только {}".format(result))
    except Exception as exp:
        print(exp)
        mydb.close()
        bot.send_message(message.chat.id, "в боте какая-то ошибка,напиши об этом @hatimacura")
@bot.message_handler(commands=['unreg'])
def unreg(message):
    mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
    cur = mydb.cursor()
    com='DELETE FROM reg WHERE id=%s;'%(message.from_user.id)
    cur.execute(com)
    mydb.close()
    bot.send_message(message.chat.id, "ты больше не зарегестрирован")
@bot.message_handler(commands=['top'])
def top(message):
    mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
    cur = mydb.cursor()
    com='SELECT MAX(count) FROM reg;'
    cur.execute(com)
    result = str(cur.fetchall())
    result = result.replace("(", "")
    result = result.replace(")", "")
    result = result.replace(",", "")
    com='SELECT id FROM reg WHERE count=%s;'%(result)
    cur.execute(com)
    resultt = str(cur.fetchall())
    resultt = resultt.replace("(", "")
    resultt = resultt.replace(")", "")
    resultt = resultt.replace(",", "")

    user_send_message = "самое большое количество денег сейчас у "+"["+ "этого человека" +"](tg://user?id="+ str(resultt)+")"+"({})".format(result)
    bot.send_message(message.chat.id,str(user_send_message), parse_mode="Markdown")
    mydb.close()
@bot.message_handler(commands=['name'])
def newname(message):
    try:
        chunkss=message.text.split(" ")
        first=chunkss[-1]
        try:
            mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
            cur = mydb.cursor()
            com="UPDATE `reg` SET `name` = '{}' WHERE id=%s;".format(first)%(message.from_user.id)
            cur.execute(com)
            mydb.close()
            bot.send_message(message.chat.id, "твой ник успешно изменен!")
        except Exception as exp:
            print(exp)
            bot.send_message(message.chat.id, "ошибка")
    except:
        bot.send_message(message.chat.id, "ты не указал ник")
@bot.message_handler(commands=['see'])
def see(message):
    if message.from_user.id == 2095244384:
        mydb = MySQLdb.connect(host = 'tokotaru.mysql.pythonanywhere-services.com',user = 'tokotaru',passwd = 'Tpa228228',db = 'tokotaru$reg' ,autocommit=True)
        cur = mydb.cursor()
        com="SELECT * FROM reg;"
        cur.execute(com)
        result = str(cur.fetchall())
        mydb.close()
        bot.send_message(message.chat.id, result)
bot.polling()