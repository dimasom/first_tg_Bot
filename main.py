import telebot
from telebot import types
import os
from dotenv import load_dotenv
from langid import classify
from modules.translate import translate
#------------------------------------------------------------------------------------------------
# Инициализация
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
#------------------------------------------------------------------------------------------------
# Функция возведения в квадрат
def square(num):
    return num**2
#------------------------------------------------------------------------------------------------
# Обработчик при вводе команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("открыть pdf", callback_data='open_pdf')
    button2 = types.InlineKeyboardButton("открыть txt", callback_data='open_txt')
    markup.row(button1,button2)
    bot.reply_to(message, f"Привет, {message.from_user.first_name} {message.from_user.last_name}.Выбери нужное", reply_markup=markup)

#------------------------------------------------------------------------------------------------
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'open_pdf':
        with open('src/call.txt', 'w')as file:
            file.write(str(call))
        with open('src/1.pdf', 'rb') as pdf_file:
            bot.send_document(call.message.chat.id, pdf_file)
    elif call.data == 'open_txt':
        with open('src/call.txt', 'w')as file:
            file.write(str(call))
        with open('src/call.txt', 'rb') as pdf_file:
            bot.send_document(call.message.chat.id, pdf_file)

#------------------------------------------------------------------------------------------------
# Обработчик всех сообщений
@bot.message_handler(func=lambda msg: True)
def send_all(message):
    detect_language = classify(message.text)
    if detect_language[0] == 'en':
        new_msg = translate(message, 'en', 'ru')
        bot.reply_to(message, new_msg)
    elif detect_language[0] == 'ru':
        new_msg = translate(message, 'ru', 'en')
        bot.reply_to(message, new_msg)
    else:
        print('Извините, я не могу понять ваш язык')
        bot.reply_to(message, 'Извините, я не могу понять ваш язык')

#------------------------------------------------------------------------------------------------
# Запуск бота    
bot.infinity_polling()

















