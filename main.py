import telebot
from telebot import types
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

def square(num):
    return num**2

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("открыть pdf", callback_data='open_pdf')
    button2 = types.InlineKeyboardButton("открыть pdf", callback_data='open_pdf')
    markup.row(button1,button2)
    bot.reply_to(message, f"Привет, {message.from_user.first_name} {message.from_user.last_name}.Выбери нужное", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'open_pdf':
        with open('call.txt', 'w')as file:
            file.write(str(call))
        with open('1.pdf', 'rb') as pdf_file:
            bot.send_document(call.message.chat.id, pdf_file)


@bot.message_handler(func=lambda msg: True)
def send_all(message):
    # bot.reply_to(message, area(int(message)))
    try:
        number = int(message.text)
        number_square = square(number)
        bot.reply_to(message, number_square)
    except ValueError:
        print("Это не цифра")


bot.infinity_polling()

















