import time
from urllib import request
import datetime

from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update
from telegram.ext import MessageHandler, Updater, CommandHandler, Filters, CallbackContext

from weather import get_weather

TOKEN= "5512191268:AAEtu0TxbcfJ47faVZFhCAVa6tv0wwY7CVw"
bot_user_name = "Time_Data_bot"
city= ""



def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я информационный бот компании "Путешествия и туризм".\n'
                              'Для получения информации можете воспользоваться подсказками ниже!',
                              reply_markup=markup)


def close_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def echo(update: Update, context: CallbackContext):
    global city
    city = update.message.text


    update.message.reply_text('Мы запомнили ваш город = '+ city)


def min_temp(update: Update, context: CallbackContext):

    update.message.reply_text("min temp = "+str(get_weather(city)["min_temp"]))


def max_temp(update: Update, context: CallbackContext):

    update.message.reply_text("max temp = "+str(get_weather(city)["max_temp"]))


def temp(update: Update, context: CallbackContext):

    update.message.reply_text("temp = "+ str(get_weather(city)["temp"]))

def feels_like(update: Update, context: CallbackContext):
    print(city)
    update.message.reply_text(f"feels like = {get_weather(city)['feels_like']}")

updater = Updater(TOKEN)

dp = updater.dispatcher

reply_keyboard = [['/min_temp', '/max_temp'],
                  ['/temp', '/feels_like']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))

dp.add_handler(CommandHandler('close', close_keyboard))

dp.add_handler(CommandHandler('min_temp', min_temp))
dp.add_handler(CommandHandler('max_temp', max_temp))
dp.add_handler(CommandHandler('temp', temp))
dp.add_handler(CommandHandler('feels_like', feels_like))

text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)

updater.start_polling()
updater.idle()







#git add . добавление нового файла
#git commit -m "update 1" добавление нового сохранения
#git push имя.сервера(origin) имя.ветки(master) отправление, сохранение на сервер
#git fetch вытащить все изменения1



