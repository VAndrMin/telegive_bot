import telebot

bot = telebot.TeleBot("5729519893:AAEp364nJgQEROZt4UoZHRxNtvq2G5r-CvM")

@bot.message_handler(commands=['start'])
def send_welcome(massage) :
    bot.reply_to(massage, "Вітання в гів бот тесті")

#bot.polling()
