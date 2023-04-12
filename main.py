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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    grade = types.KeyboardButton("Выбор класса")
    search_formula = types.KeyboardButton("Найти формулу")
    search_information = types.KeyboardButton("Найти тему")
    get_all = types.KeyboardButton("Все формулы")
    add_form = types.KeyboardButton("Добавить формулу")
    markup.add(grade, search_formula, search_information, get_all, add_form)
    bot.send_message(message.chat.id, "Привет. Выбери, что хочешь делать?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def replies(message):
    # choice of grade(работает)
    if message.text == "Выбор класса" or message.text == "Поменять класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        grade_9 = types.KeyboardButton("9-й класс")
        grade_10 = types.KeyboardButton("10-й класс")
        grade_11 = types.KeyboardButton("11-й класс")
        markup.add(grade_9, grade_10, grade_11)
        bot.send_message(message.chat.id, 'В каком вы классе?', reply_markup=markup)
    # find formula
    elif message.text == 'Найти формулу':
        bot.send_message(message.chat.id, "Чтобы найти формулу, напишите найди формулу Название формулы")

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
        bot.send_message(message.chat.id, get_all_formulas())

    # 9 grade(working)
    elif message.text == '9-й класс' or message.text == '9':
        global needen_grade
        needen_grade = 9
        print(needen_grade)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_form = types.KeyboardButton("Добавить формулу")
        change_class = types.KeyboardButton("Поменять класс")
        markup.add(search_formula, search_information, get_all, add_form, change_class)
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 9-го класса. Что вы хотите сделать?', reply_markup=markup)

    # 10 grade(working)
    elif message.text == '10-й класс' or message.text == '10':
        needen_grade = 10
        print(needen_grade)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("Найти формулу"),
            types.KeyboardButton("Найти тему"),
            types.KeyboardButton("Все формулы"),
            types.KeyboardButton("Добавить формулу"),
            types.KeyboardButton("Поменять класс"),
        )
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 10-го класса. Что вы хотите сделать?', reply_markup=markup)

    # 11 grade(working)
    elif message.text == '11-й класс' or message.text == '11':
        needen_grade = 11
        print(needen_grade)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_form = types.KeyboardButton("Добавить формулу")
        change_class = types.KeyboardButton("Поменять класс")
        markup.add(search_formula, search_information, get_all, add_form, change_class)
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 11-го класса. Что вы хотите сделать?', reply_markup=markup)

    # search by name of formula
    elif message.text[:13].lower().startswith('найди формулу'):
        global what_to_find
        what_to_find = message.text[14:]
        bot.send_message(message.chat.id, 'Ищу формулу по вашему запросу....Пожалуйста ожидайте.')
        bot.send_message(message.chat.id, get_needen_formula(what_to_find))

    # search by topic
    elif message.text[:10].lower().startswith('найди тему: '):
        global topic_to_find
        topic_to_find = message.text[11:]
        print(topic_to_find)
        bot.send_message(message.chat.id, get_needen_topic(topic_to_find))
        bot.send_message(message.chat.id, 'Ищу формулы по выбранной теме....Пожалуйста ожидайте.')

    # adding new formula with needen params
    # get name_of_formula
    elif message.text[:14].lower().startswith('новая формула:'):
        name_f = message.text[15:]
        print(name_f)
        add_formula(current_formula=name_f)
        bot.send_message(message.chat.id, 'Так с названием разобрались, продолжим. Введите формулу в формате - формула: .....')
    # get formula
    elif message.text[:8].lower().startswith('формула:'):
        new_formula = message.text[9:]
        print(new_formula)
        add_formula(name_of_formula=new_formula)
        bot.send_message(message.chat.id, 'Так формула есть, продолжим. Введите тему в формате - тема: .....')
    # get theme
    elif message.text[:5].lower().startswith('тема:'):
        new_topic = message.text[6:]
        print(new_topic)
        add_formula(topic_of_form=new_topic)
        bot.send_message(message.chat.id, 'С темой определились. Введите пояснения к формуле - пояснения: .....')
    elif message.text[:10].lower().startswith('пояснения:'):
        explaining = message.text[11:]
        print(explaining)
        add_formula(explanation=explaining, details='отсутствуют')
        bot.send_message(message.chat.id, 'Пояснение принято. Формула будет добавлена в каталог в ближайшее время.')


def get_all_formulas():  # получение всех формул за все классы(работает)
    session = create_session()
    notes = session.query(Formula).all()
    if len(notes) == 0:
         return 'Это были все формулы, которые у нас есть.'
    return '\n'.join(f'{note.topic}, {note.formula_name}, {note.formula}, {note.explanation}, {note.details}' for note in notes)


#message all formulas
#def print_all_formulas_to_table():
    #table = PrettyTable()
    #table.field_names = ['Тема', 'Название формулы', 'Формула', 'Обьяснение', 'Детали']
    #all_formulas = get_all_formulas()
    #for note in enumerate(all_formulas):
        #table.add_row(note)
    #bot.send_message(all_formulas)


# get one formula(работает)
def get_needen_formula(what_to_find):
    session = create_session()
    if needen_grade:
        for formula in session.query(Formula).filter(Formula.grade == needen_grade, Formula.formula_name == what_to_find):
            return (f' {formula.formula_name}, {formula.formula}, {formula.explanation}')
    else:
        for formula in session.query(Formula).filter(Formula.formula_name == what_to_find):
            return (f' {formula.formula_name}, {formula.formula}, {formula.explanation}')



# find topic
def get_needen_topic(topic_to_find):
    session = create_session()
    needen_grade = 9
    if needen_grade:
        notes = session.query(Formula).filter(Formula.grade == needen_grade, Formula.formula_name == topic_to_find)
        return '\n'.join(f'{note.topic}, {note.formula_name}, {note.formula}, {note.explanation}, {note.details}' for note in notes)

    else:
        notes = session.query(Formula).filter(Formula.formula_name == topic_to_find)
        return '\n'.join(
            f'{note.topic}, {note.formula_name}, {note.formula}, {note.explanation}, {note.details}' for note in notes)


def add_formula(name_of_formula):
    session = create_session()
    formula = Formula(
        formula_name=name_of_formula,
    )
    print(formula)
    session.add(formula)
    session.commit()


# just main
def main():
    db_session.global_init("db/physics.db")
    bot.infinity_polling()


if __name__ == '__main__':
    main()