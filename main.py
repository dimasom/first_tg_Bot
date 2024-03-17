import telebot

TOKEN = '7164557265:AAELlzH_SgYzJc4-MoSRyvS_nRlYJq6dOg8'
bot = telebot.TeleBot(TOKEN)

def square(num):
    return num**2

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, {message.from_user.first_name.username.last_name}.How are you doing?")

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

















