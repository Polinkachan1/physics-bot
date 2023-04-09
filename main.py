from data import db_session
from bot_token import BOT_TOKEN
import telebot
from telebot import types
from data.db_session import create_session
from data.formula import Formula
from prettytable import PrettyTable

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    # start menu
    bot.send_message(message.chat.id, "Привет. Выбери, что хочешь делать?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    grade = types.KeyboardButton("Выбор класса")
    search_formula = types.KeyboardButton("Найти формулу")
    search_information = types.KeyboardButton("Найти тему")
    get_all = types.KeyboardButton("Все формулы")
    add_formula = types.KeyboardButton("Добавить формулу")
    markup.add(grade, search_formula, search_information, get_all, add_formula)


@bot.message_handler(content_types=['text'])
def replies(message):
    # choice of grade
    if message.text == "Выбор класса":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        grade_9 = types.KeyboardButton("9-й класс")
        grade_10 = types.KeyboardButton("10-й класс")
        grade_11 = types.KeyboardButton("11-й класс")
        markup.add(grade_9, grade_10, grade_11)
        bot.send_message(message.chat.id, 'В каком вы классе?')
    # find formula
    elif message.text == 'Найти формулу':
        bot.send_message(message.chat.id, "Чтобы найти формулу, напишите найди формулу Название формулы")
        print_needen_formula()
        # сделано(вроде)
    # find topic
    elif message.text == 'Найти тему':
        bot.send_message(message.chat.id, "Чтобы найти тему, напишите - найди тему Название тему ")
        # сделано(вроде)
    # add new formula to db
    elif message.text == "Добавить формулу":
        bot.send_message(message.chat.id, "Чтобы добавить новую формулу ответьте на несколько вопросов.")
        bot.send_message(message.chat.id, "Введите название формулы в формате - новая формула: название формулы")
    # output - all formulas from db
    elif message.text == "Все формулы":
        bot.send_message(message.chat.id, 'Готовлю для вас список всех формул....Пожалуйста ожидайте.')
        # сделано(вроде)

    # 9 grade
    elif message.text == '9-й класс':
        global needen_grade
        needen_grade = 9
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 9-го класса. Что вы хотите сделать?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_formula = types.KeyboardButton("Добавить формулу")
        markup.add(search_formula, search_information, get_all, add_formula)

    # 10 grade
    elif message.text == '10-й класс':
        needen_grade = 10
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 10-го класса. Что вы хотите сделать?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_formula = types.KeyboardButton("Добавить формулу")
        markup.add(search_formula, search_information, get_all, add_formula)

    # 11 grade
    elif message.text == '11-й класс':
        needen_grade = 11
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 11-го класса. Что вы хотите сделать?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_formula = types.KeyboardButton("Добавить формулу")
        markup.add(search_formula, search_information, get_all, add_formula)

    # search by name of formula
    elif message.text[:13].lower().startswith('найди формулу'):
        global what_to_find
        what_to_find = message.text[14:]
        bot.send_message(message.chat.id, 'Ищу формулу по вашему запросу....Пожалуйста ожидайте.')
        print_all_formulas_to_table()

    # search by topic
    elif message.text[:10].lower().startswith('найди тему'):
        global topic_to_find
        topic_to_find = message.text[11:]
        bot.send_message(message.chat.id, 'Ищу формулы по выбранной теме....Пожалуйста ожидайте.')

    # adding new formula with needen params
    # get name_of_formula
    elif message.text[:14].lower().startswith('новая формула:'):
        global name_f
        name_f = message.text[15:]
        bot.send_message(message.chat.id, 'Так с названием разобрались, продолжим. Введите формулу в формате - формула: .....')
    # get formula
    elif message.text[:8].lower().startswith('формула:'):
        global new_formula
        new_formula = message.text[9:]
        bot.send_message(message.chat.id, 'Так формула есть, продолжим. Введите тему в формате - тема: .....')
    # get theme
    elif message.text[:5].lower().startswith('тема:'):
        global new_topic
        new_topic = message.text[5:]
        bot.send_message(message.chat.id, 'С темой определились. Введите пояснения к формуле: .....')
    elif message.text[:10].lower().startswith('пояснения:'):
        global explaining
        explaining = message.text[11:]
        add_formula(new_topic, needen_grade, name_f, new_formula, explaining, details='отсутствуют')
        bot.send_message(message.chat.id, 'Пояснение принято. Формула будет добавлена в каталог в ближайшее время.')


def get_all_formulas(chat_id):  # получение всех формул за все классы
    session = create_session()
    all_formulas = session.query(Formula).all()
    row = [(note.topic, note.formula_name, note.formula, note.explanation, note.details) for note in all_formulas]
    return row


# message all formulas
def print_all_formulas_to_table(message):
    table = PrettyTable()
    table.field_names = ['Тема', 'Название формулы', 'Формула', 'Обьяснение', 'Детали']
    all_formulas = get_all_formulas(message.chat.id)
    for note in enumerate(all_formulas):
        table.add_row(note)
    bot.send_message(message.chat.id, table)


# get one formula
def get_needen_formula(chat_id):
    session = create_session()
    if needen_grade:
        formula = session.query(Formula).filter(Formula.grade == needen_grade, Formula.formula_name == what_to_find)
        result = [(formula.formula_name, formula.formula, formula.explanation) for form in formula]
    else:
        formula = session.query(Formula).filter(Formula.formula_name == what_to_find)
        result = [(formula.formula_name, formula.formula, formula.explanation) for form in formula]
    return result


# print one formula
def print_needen_formula(message):
    search_formula = get_needen_formula(message.chat.id)
    table = PrettyTable()
    table.field_names = ['Название формулы', 'Формула', 'Обьяснение']

    bot.send_message(message.chat.id, table)


# find topic
def get_needen_topic(chat_id):
    session = create_session()
    if needen_grade:
        formula = session.query(Formula).filter(Formula.grade == needen_grade, Formula.topic == topic_to_find)
        result = [(formula.formula_name, formula.formula, formula.explanation) for form in formula]
    else:
        formula = session.query(Formula).filter(Formula.formula_name == topic_to_find)
        result = [(formula.formula_name, formula.formula, formula.explanation) for form in formula]
    return result


# print topic
def print_needen_topic(message):
    search_formula = get_needen_formula(message.chat.id)
    table = PrettyTable()
    table.field_names = ['Тема', 'Название формулы', 'Формула', 'Обьяснение']

    bot.send_message(message.chat.id, table)


def add_formula(topic_of_form, needen_grade, name_of_formula, current_formula, explanation, details):
    session = create_session()
    formula = Formula(
        topic=topic_of_form,
        grade=needen_grade,
        formula_name=name_of_formula,
        formula=current_formula,
        explanation=explanation,
        details=details,
    )
    session.add(formula)
    session.commit()


# just main
def main():
    db_session.global_init("db/physics.db")
    bot.infinity_polling()


if __name__ == '__main__':
    main()
