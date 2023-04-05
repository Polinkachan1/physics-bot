from data import db_session
from bot_token import BOT_TOKEN
import telebot
from telebot import types


bot = telebot.TeleBot(BOT_TOKEN)
needen_class = 9


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    grade = types.KeyboardButton("Выбор класса")
    search_formula = types.KeyboardButton("Найти формулу")
    search_information = types.KeyboardButton("Найти тему")
    add_formula = types.KeyboardButton("Добавить формулу")
    markup.add(grade, search_formula, search_information, add_formula)


@bot.message_handler(content_types=['text'])
def replies(message):
    if message.text == "Выбор класса":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        grade_9 = types.KeyboardButton("9-й класс")
        grade_10 = types.KeyboardButton("10-й класс")
        grade_11 = types.KeyboardButton("11-й класс")
        markup.add(grade_9, grade_10, grade_11)
        bot.send_message(message.chat.id, 'В каком вы классе?')
    elif message.text == 'Найти формулу':
        bot.send_message(message.chat.id, "Чтобы найти формулу, напишите 'найди <название формулы>'")
    elif message.text == 'Найти тему':
        bot.send_message(message.chat.id, "Чтобы найти тему, напишите 'найди <название тему>' ")
    elif message.text == "Добавить формулу":
        bot.send_message(message.chat.id, "Чтобы добавить новую формулу ответьте на несколько вопросов.")
        bot.send_message(message.chat.id, "Введите название формулы.")
    elif message.text == '9-й класс':
        needen_grade = 9
    elif message.text == '10-й класс':
        needen_grade = 10
    elif message.text == '11-й класс':
        needen_grade = 11


def main():
    db_session.global_init("db/physics.db")
