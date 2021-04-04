import telebot

bot = telebot.TeleBot('1483702341:AAETLsXl2Ae-ne6doiAlz5uXI20WyrhuALQ')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('hello', 'bye')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет, ты написал мне /start', reply_markup = keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'hi!')
    elif message.text == 'bye':
        bot.send_message(message.chat.id, 'bye!')
bot.polling()