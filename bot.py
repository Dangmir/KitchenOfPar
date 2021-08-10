import telebot
from telebot import types
import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
dbuser = client['tguser']
db = client['tgdb']


bot = telebot.TeleBot('1840665419:AAH_pw1tKDJt_LkP_-mO2wOMTsVDKAsr4Bg',parse_mode=None)

#Регистраиция
@bot.message_handler(commands=['start'])
def start(message):
    a = dbuser.user.find_one({'tgid': message.from_user.id})
    print(a,message.from_user.id)
    if a:
        bot.send_message(message.from_user.id,'Вы уже зарегистрированны')
    else:
        a = bot.send_message(message.from_user.id,'Здравствуйте, введите ваши данные перед заказом через запятую вот в таком формате:\nAlexey,89877500711')
        bot.register_next_step_handler(a,register)

def register(message):
    text = message.text.split(',')
    name = text[0]
    phone = text[1]
    dbuser.user.insert_one({'name':name,'phone':phone,'tgid':message.from_user.id})
    bot.send_message(message.from_user.id,'Успешно зарегистрированны')



@bot.message_handler(commands=['shop'])
def shop(message):
    mainmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton(text='Одноразки')
    key2 = types.KeyboardButton(text='Жидскости')
    mainmenu.add(key1, key2)
    bot.send_message(message.from_user.id, 'Это главное меню!', reply_markup=mainmenu)



@bot.callback_query_handler(func=lambda c: True)
def ans(c):
    if c.data=='toBucket':
        toBucket(c)
    if c.data =='buyall':
        buyall(c)
#МЕНЮ
def menuone(message):
    mainmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton(text='HQD')
    key2 = types.KeyboardButton(text='IZI')
    key3 = types.KeyboardButton(text='Корзина')
    mainmenu.add(key1, key2,key3)
    bot.send_message(message.from_user.id, 'Одноразки', reply_markup=mainmenu)

def hqdsearch(message):
    result = db.tgdb.find({"name": {"$regex": 'HQD'}}).limit(10)
    mainmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton(text='HQD 300 затяжек')
    key2 = types.KeyboardButton(text='HQD 600 затяжек')
    key3 = types.KeyboardButton(text='HQD 1200 затяжек')
    key4 = types.KeyboardButton(text='HQD 2000 затяжек')
    key5 = types.KeyboardButton(text='HQD 2500 затяжек')
    key6 = types.KeyboardButton(text='Корзина')
    key7 = types.KeyboardButton(text='Вернуться')
    mainmenu.add(key1, key2, key3,key4,key5,key6,key7)
    bot.send_message(message.from_user.id, 'HQD', reply_markup=mainmenu)

def hqd300(message):
    result = db.tgdb.find({"name": {"$regex": 'HQD Cuvie 280'}}).limit(10)
    for i in result:
        mainmenu = types.InlineKeyboardMarkup()
        right = types.InlineKeyboardButton(text='>', callback_data='right')
        left = types.InlineKeyboardButton(text='<', callback_data='left')
        key1 = types.InlineKeyboardButton(text=f'В корзину', callback_data='toBucket')
        mainmenu.add(left, right, key1 )
        bot.send_message(message.from_user.id,f'ID:{i["id"]}\nНазвание:{i["name"]}\nЦена: {i["price"]} \nОстаток:{i["stock"]}',reply_markup=mainmenu)

def hqd600(message):
    result = db.tgdb.find({"name": {"$regex": 'HQD Super'}}).limit(10)
    for i in result:
        mainmenu = types.InlineKeyboardMarkup()
        right = types.InlineKeyboardButton(text='>', callback_data='right')
        left = types.InlineKeyboardButton(text='<', callback_data='left')
        key1 = types.InlineKeyboardButton(text=f'В корзину', callback_data='toBucket')
        mainmenu.add(left, right, key1)
        bot.send_message(message.from_user.id,
                         f'ID:{i["id"]}\nНазвание:{i["name"]}\nЦена: {i["price"]} \nОстаток:{i["stock"]}',
                         reply_markup=mainmenu)

def hqd1200(message):
    result = db.tgdb.find({"name": {"$regex": 'HQD Cuvie PLUS'}}).limit(10)
    for i in result:
        mainmenu = types.InlineKeyboardMarkup()
        right = types.InlineKeyboardButton(text='>', callback_data='right')
        left = types.InlineKeyboardButton(text='<', callback_data='left')
        key1 = types.InlineKeyboardButton(text=f'В корзину', callback_data='toBucket')
        mainmenu.add(left, right, key1)
        bot.send_message(message.from_user.id,
                         f'ID:{i["id"]}\nНазвание:{i["name"]}\nЦена: {i["price"]} \nОстаток:{i["stock"]}',
                         reply_markup=mainmenu)

def hqd2000(message):
    result = db.tgdb.find({"name": {"$regex": 'HQD King'}}).limit(10)
    for i in result:
        mainmenu = types.InlineKeyboardMarkup()
        right = types.InlineKeyboardButton(text='>', callback_data='right')
        left = types.InlineKeyboardButton(text='<', callback_data='left')
        key1 = types.InlineKeyboardButton(text=f'В корзину', callback_data='toBucket')
        mainmenu.add(left, right, key1)
        bot.send_message(message.from_user.id,
                         f'ID:{i["id"]}\nНазвание:{i["name"]}\nЦена: {i["price"]} \nОстаток:{i["stock"]}',
                         reply_markup=mainmenu)

def hqd2500(message):
    result = db.tgdb.find({"name": {"$regex": 'HQD Maxx'}}).limit(10)
    for i in result:
        mainmenu = types.InlineKeyboardMarkup()
        right = types.InlineKeyboardButton(text='>', callback_data='right')
        left = types.InlineKeyboardButton(text='<', callback_data='left')
        key1 = types.InlineKeyboardButton(text=f'В корзину', callback_data='toBucket')
        mainmenu.add(left, right, key1)
        bot.send_message(message.from_user.id,
                         f'ID:{i["id"]}\nНазвание:{i["name"]}\nЦена: {i["price"]} \nОстаток:{i["stock"]}',
                         reply_markup=mainmenu)

def backet(message):
    mainmenu = types.InlineKeyboardMarkup()
    delete = types.InlineKeyboardButton(text='Удалить',callback_data='delete_from_bucket')
    mainmenu.add(delete)
    buy = types.InlineKeyboardMarkup()
    buy1 = types.InlineKeyboardButton(text='Оформить заказ',callback_data='buyall')
    buy.add(buy1)
    try:
        a = dbuser.user.find_one({'tgid':message.from_user.id})['bucket']
        bot.send_message(message.from_user.id, 'Корзина')
        count = 1
        item = []
        for i in a:
            item.append({'id': i[0]['id']})

            bot.send_message(message.from_user.id,
                             f'ID:{i[0]["id"]}\nНазвание:{i[0]["name"]}\nЦена: {i[0]["price"]}\nОстаток на складе: {i[0]["stock"]}\nКоличество к покупке:',
                             reply_markup=mainmenu)
        bot.send_message(message.from_user.id, 'Заказ', reply_markup=buy)
    except:
        bot.send_message(message.from_user.id, "Корзина пуста")


def toBucket(message):
    id_tovara = message.message.text.split()[0].split(':')[1]
    tovar = db.tgdb.find_one({'id':int(id_tovara)})
    user = dbuser.user.find_one({'tgid':message.from_user.id})

    item = {'name':tovar['name'],'price':tovar['price'],'id':tovar['id'],'stock':tovar['stock']}
    dbuser.user.update_one({'tgid':message.from_user.id},{'$push':{'bucket':[item]}})
    bot.send_message(message.from_user.id,'Добавленно в корзину')

def buyall(message):
    id = dbuser.user.find_one({'tgid':message.from_user.id})
    bucket = id['bucket']
    print(bucket)
    bot.send_message(861813649, f'Hello Pidar прими заказ от {id["name"]}\n Номер телефона:{id["phone"]}')
    for i in bucket:
        print(i)
        bot.send_message(861813649,f'{i[0]["name"]}')
    dbuser.user.update_one({'tgid':message.from_user.id},{'$unset':{'bucket':1}})
@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == 'Одноразки':
        menuone(message)
    if message.text == 'HQD':
        hqdsearch(message)
    if message.text == 'Корзина':
        backet(message)
    if message.text == 'HQD 300 затяжек':
        hqd300(message)
    if message.text == 'HQD 600 затяжек':
        hqd600(message)
    if message.text == 'HQD 1200 затяжек':
        hqd1200(message)
    if message.text == 'HQD 2000 затяжек':
        hqd2000(message)
    if message.text == 'HQD 2500 затяжек':
        hqd2500(message)
    if message.text =='Вернуться':
        menuone(message)

if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except BaseException as e:
            print(e)
            pass