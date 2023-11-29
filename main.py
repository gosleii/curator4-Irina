import telebot

bot = telebot.TeleBot('6697289666:AAG8HLE8-tXs3HVMU5ttB3-EbrPEV5hwiQI')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Здравствуй, Уважаемый друг! Ты готов погрузиться в мир клуба романтики? Если да, то поехали',
                     parse_mode='Markdown')


@bot.message_handler(commands=['go'])
def main(message):
    bot.send_message(message.chat.id,
                     'Клуб романтики-это коллекция романтических историй, в которых вы можете делать выборы, тем самым влияя на сюжет',
                     parse_mode='Markdown')


@bot.message_handler(commands=['kr'])
def main(message):
    bot.send_message(message.chat.id, '[Если тебя заинтересовало, то присоединяйся к нам](https://club-romance.ru)',
                     parse_mode='Markdown')


bot.infinity_polling()