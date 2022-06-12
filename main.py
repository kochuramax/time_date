import time
from urllib import request
import datetime

from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update
from telegram.ext import MessageHandler, Updater, CommandHandler, Filters, CallbackContext

TOKEN= "5512191268:AAEtu0TxbcfJ47faVZFhCAVa6tv0wwY7CVw"
bot_user_name = "Time_Data_bot"




def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я информационный бот компании "Путешествия и туризм".\n'
                              'Для получения информации можете воспользоваться подсказками ниже!',
                              reply_markup=markup)


def close_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def echo(update: Update, context: CallbackContext):
    if update.message.text[-1] == '?':
        update.message.reply_text('Конечно можно спросить! Только я культурно промолчу...')
    else:
        update.message.reply_text('Вполне возможно, кто ж знает?')


def address(update: Update, context: CallbackContext):
    update.message.reply_text('Адрес: Китай, Гималаи, хребет Махалангур-Химал, вершина Эверест, д. 1')


def phone(update: Update, context: CallbackContext):
    update.message.reply_text('Телефон: +86 133 2686 8519')


def site(update: Update, context: CallbackContext):
    update.message.reply_text('hello')


def work_time(update: Update, context: CallbackContext):
    update.message.reply_text('Время работы: пн-пт, 9-00 - 19-00')


updater = Updater(TOKEN)

dp = updater.dispatcher

reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))

dp.add_handler(CommandHandler('close', close_keyboard))

dp.add_handler(CommandHandler('address', address))
dp.add_handler(CommandHandler('phone', phone))
dp.add_handler(CommandHandler('site', site))
dp.add_handler(CommandHandler('work_time', work_time))

text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)

updater.start_polling()

updater.idle()



#git add . добавление нового файла
#git commit -m "update 1" добавление нового сохранения
#git push имя.сервера(origin) имя.ветки(master) отправление, сохранение на сервер
#git fetch вытащить все изменения1