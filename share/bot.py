import telebot
from telebot import types
from mysql_handler import SQLHandler
from arg import *

bot = telebot.TeleBot(TG_TOKEN)

registered_users = {}

@bot.message_handler(commands=['start'])
def accept(message):
    user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_agree = types.KeyboardButton('Принять условия')
    markup.row(item_agree)
    bot.send_message(user_id, 'Я даю свое согласие ООО "ИТ"...', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Принять условия')
def start_registration(message):
    bot.send_message(message.chat.id, 'Введите, пожалуйста, Ваш номер телефона')
    bot.register_next_step_handler(message, get_phone_number)

def get_phone_number(message):
    global phone_number_from_user
    phone_number_from_user = message.text.strip()

    bot.send_message(message.chat.id, 'Введите, пожалуйста, Ваши имя и фамилию')
    bot.register_next_step_handler(message, get_first_last_name)

def get_first_last_name(message):
    global first_last_name
    first_last_name = message.text.strip()
    user_id = message.from_user.id
    db = SQLHandler('mysql_registration', MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, 'MyDB')
    db.insert(phone_number_from_user, first_last_name, user_id)
    bot.send_message(message.chat.id, f'Ваша учетная запись: {phone_number_from_user}, {first_last_name}', reply_markup=change_data())

def change_data():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Изменить имя/фамилию")
    button2 = types.KeyboardButton("Изменить номер телефона")
    button3 = types.KeyboardButton("Завершить редактирование")
    markup.add(button1, button2, button3)
    return markup

# Обработчик для кнопки "Изменить имя/фамилию" ------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "Изменить имя/фамилию")
def button1(message):
    bot.send_message(message.chat.id, "Введите, пожалуйста, Ваши имя и фамилию")
    bot.register_next_step_handler(message, get_changed_first_last_name)

def get_changed_first_last_name(message):
    global new_first_last_name
    new_first_last_name = message.text.strip()
    user_id = message.from_user.id
    db = SQLHandler('mysql_registration', MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, 'MyDB')
    db.update_changed_name(user_id, new_first_last_name)
    bot.send_message(message.chat.id, f'Имя/Фамилия изменены: {new_first_last_name}', reply_markup=accept_change_first_last_name())
    bot.register_next_step_handler(message, handle_next_step)
    
def accept_change_first_last_name():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_accept = types.KeyboardButton("Принять")
    button_change = types.KeyboardButton("Изменить")
    markup.add(button_accept, button_change)
    return markup

def handle_next_step(message):
    if message.text == "Принять":
        bot.send_message(message.chat.id, f"Ваша учетная запись: {phone_number_from_user}, {new_first_last_name}")
        button3(message)
    elif message.text == "Изменить":
        button1(message)

# Обработчик для кнопки "Изменить номер телефона" ------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "Изменить номер телефона")
def button2(message):
    bot.send_message(message.chat.id, "Введите, пожалуйста, Ваш номер телефона")
    bot.register_next_step_handler(message, get_changed_phone_number)

def get_changed_phone_number(message):
    global new_phone_number
    new_phone_number = message.text.strip()
    user_id = message.from_user.id
    db = SQLHandler('mysql_registration', MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, 'MyDB')
    db.update_changed_phone_number(user_id, new_phone_number)
    bot.send_message(message.chat.id, f'Номер телефона изменен: {new_phone_number}', reply_markup=accept_change_phone_number())
    bot.register_next_step_handler(message, handle_next_step_phone)

def accept_change_phone_number():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_accept = types.KeyboardButton("Принять")
    button_change = types.KeyboardButton("Изменить")
    markup.add(button_accept, button_change)
    return markup

def handle_next_step_phone(message):
    if message.text == "Принять":
        bot.send_message(message.chat.id, f"Ваша учетная запись: {new_phone_number}, {first_last_name}")
        button3(message)
    elif message.text == "Изменить":
        button2(message)

# Обработчик для кнопки "Завершить редактирование" ------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "Завершить редактирование")
def button3(message):
    bot.send_message(message.chat.id, "Регистрация завершена")

if __name__ == "__main__":
    bot.polling()