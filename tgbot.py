from telebot import*
from telebot import types
import sqlite3
from datetime import datetime, timedelta
from time import sleep

token = '6362477321:AAHDb8DSRHey2lRc0oki_i4uigQFnczzIzI' # Это токен бота для тестов
bot = telebot.TeleBot(token)

clickIdTimes = {}
promocode = ['mafia', 'l1nkooln']

def checkClick(chat_id, timer_dict, timeout):
    if chat_id not in timer_dict or timer_dict[chat_id] < datetime.now() - timedelta(seconds=timeout):
        timer_dict[chat_id] = datetime.now()
        return True
    return False


print(checkClick(10, clickIdTimes, timeout=1))
print(checkClick(10, clickIdTimes, timeout=1))
sleep(2)
print(checkClick(10, clickIdTimes, timeout=1))
print(checkClick(10, clickIdTimes, timeout=1))

def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

@bot.message_handler(commands=['start'])
def button(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt7 = types.KeyboardButton('Додати оголошення')
    markup.add(bt7)
    # admins_id = [1090256518, 1132004570]
    # for admin in admins_id:
    #     if message.from_user.id == admin:
    #         bt8 = types.KeyboardButton('Показати клієнтів')
    #         markup.add(bt8)
    #     else:
    #         pass
    bot.send_message(chat_id, f'<b>Привіт {message.from_user.first_name}👋!</b> <b>Що бажаєш обрати?</b>',
        parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Додати оголошення':
            a = types.ReplyKeyboardRemove()
            # bot.send_message(message.from_user.id, 'Что', reply_markup=a)
            # if not checkClick(chat_id, clickIdTimes, 30*60):
            #     bot.send_message(chat_id, "📌Ви вже записалися \n Спробуйте пізніше")
            #     return
            vid = bot.send_message(chat_id, 'Напиши марку та модель авто')
            bot.register_next_step_handler(vid, regist_1)

def regist_1(message):
    global marka
    global description
    global photo
    global category
    global price
    marka = message.text
    msg3 = bot.send_message(message.chat.id, "Вкажи опис авто")
    bot.register_next_step_handler(msg3, regist_2)

def regist_2(message):
    global marka
    global description
    global photo
    global category
    global price
    description = message.text
    msg2 = bot.send_message(message.chat.id, "Надішли фото свого авто (фото приймаються посиланням)")
    bot.register_next_step_handler(msg2, regist_3)

def regist_3(message):
    global marka
    global description
    global photo
    global category
    global price
    photo = message.text
    msg4 = bot.send_message(message.chat.id, "Введіть категорію авто(марку)")
    bot.register_next_step_handler(msg4, regist_4)

def regist_4(message):
    global marka
    global description
    global photo
    global category
    global price
    category = message.text
    msg5 = bot.send_message(message.chat.id, "Введіть бажану ціну за яку б ви хотіли продати своє авто")
    bot.register_next_step_handler(msg5, regist_5)

def regist_5(message):
    global marka
    global description
    global photo
    global category
    global price
    price= message.text
    msg4 = bot.send_message(message.chat.id, "Введіть знижку(якщо немає то напиішть просто нуль)")
    bot.register_next_step_handler(msg4, regist_6)

def regist_6(message):
    global marka
    global description
    global photo
    global category
    global price
    global sale
    sale = message.text
    msg4 = bot.send_message(message.chat.id, "Дякуюємо! Ваше оголошення буде опубліковане після схвалення адміністратором")
    admin_id = (1132004570)
    bot.send_message(admin_id, f"📍Нове оголошення: \n : Нікнейм користувача {message.from_user.username} \n Марка авто: {marka}\n Опис авто: {description} \n Фото т/з: {photo} \n Ціна: {price} \n Знижка: {sale}")
    user = message.from_user.id
    if (user == 1132004570):  
        if message.chat.type == 'private':
            msg4 = bot.send_message(message.chat.id, "Додати оголошення на сайт?")
            bot.register_next_step_handler(msg4, regist_7)
        
def regist_7(message):
    global answer
    connection = sqlite3.connect('instance/portfolio.db')
    cursor = connection.cursor()
    answer = message.text
    if answer== 'true':
        cursor.execute("INSERT INTO item (title, description, category, image, price, sale) VALUES (?, ?, ?, ?, ?, ?)", (marka, description,category, photo, price, sale))
        connection.commit()
        print("Data inserted successfully.")
        bot.send_message(message.chat.id, "Адміністратор схвалив запит, ваше оголошення незабаром буже додано на сайт")
        connection.close()
    else:
        bot.send_message(message.chat.id, "Нажаль адміністратор не схвалив ваш запит")
        print("Data inserted unsuccessfully.")

            

   

    
    # except sqlite3.Error as e:
    #     print("SQLite error:", e)
    # finally:
        

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)