from urllib import request
import datetime
import telegram

TOKEN= "5512191268:AAEtu0TxbcfJ47faVZFhCAVa6tv0wwY7CVw"
bot_user_name = "Time_Data_bot"
bot = telegram.Bot(token=TOKEN)
chat_id= 1739372630
# bot.sendMessage(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
data = bot.getUpdates()
last_message=data[len(data)-1]['message']['text']


print(datetime.date.today())
