from sqlalchemy import update
from sqlalchemy.exc import IntegrityError

from data import db_session
from bot_token import BOT_TOKEN
import telebot
from telebot import types
from data.db_session import create_session
from data.formula import Formula
from data.user import User
from prettytable import PrettyTable
bot = telebot.TeleBot(BOT_TOKEN)


def main():
    db_session.global_init("db/formulas.sqlite")
    db_session.global_init("db/users.sqlite")
    bot.infinity_polling()


@bot.message_handler(commands=['start'])
def start_message(message):
    session = create_session()
    user = User(
        user_id=message.chat.id,
    )
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        pass

    # start menu
    with open('assets/smile.png', 'rb') as img:
        bot.send_photo(message.chat.id, img)
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    grade = types.KeyboardButton("Выбор класса")
    markup_1.add(grade)
    bot.send_message(message.chat.id, "Привет. Выбери класс.", reply_markup=markup_1)


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
        bot.send_message(message.chat.id, "Чтобы найти формулу, напишите: найди формулу: 'Название формулы' ")

    # find topic
    elif message.text == 'Найти тему':
        bot.send_message(message.chat.id, "Чтобы найти тему, напишите: найди тему: 'Название темы' ")

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
        needen_grade = 9
        print(needen_grade)
        add_grade(message.chat.id, needen_grade)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_form = types.KeyboardButton("Добавить формулу")
        change_class = types.KeyboardButton("Поменять класс")
        markup.add(search_formula, search_information, get_all, add_form, change_class)
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 9-го класса. Что вы хотите сделать?',
                         reply_markup=markup)

    # 10 grade(working)
    elif message.text == '10-й класс' or message.text == '10':
        needen_grade = 10
        add_grade(message.chat.id, needen_grade)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("Найти формулу"),
            types.KeyboardButton("Найти тему"),
            types.KeyboardButton("Все формулы"),
            types.KeyboardButton("Добавить формулу"),
            types.KeyboardButton("Поменять класс"),
        )
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 10-го класса. Что вы хотите сделать?',
                         reply_markup=markup)

    # 11 grade(working)
    elif message.text == '11-й класс' or message.text == '11':
        needen_grade = 11
        add_grade(message.chat.id, needen_grade)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        search_formula = types.KeyboardButton("Найти формулу")
        search_information = types.KeyboardButton("Найти тему")
        get_all = types.KeyboardButton("Все формулы")
        add_form = types.KeyboardButton("Добавить формулу")
        change_class = types.KeyboardButton("Поменять класс")
        markup.add(search_formula, search_information, get_all, add_form, change_class)
        bot.send_message(message.chat.id, 'Теперь вам доступна программа только 11-го класса. Что вы хотите сделать?',
                         reply_markup=markup)

    # search by name of formula
    elif message.text.lower().startswith('найди формулу: '):
        what_to_find = message.text[15:]
        bot.send_message(message.chat.id, 'Ищу формулу по вашему запросу....Пожалуйста ожидайте.')
        bot.send_message(message.chat.id, get_needen_formula(message.chat.id, what_to_find))

    # search by topic
    elif message.text.lower().startswith('найди тему: '):
        topic_to_find = message.text[12:]
        bot.send_message(message.chat.id, 'Ищу формулы по выбранной теме....Пожалуйста ожидайте.')
        messages = get_needen_topic(message.chat.id, topic_to_find)
        for message_text in messages:
            bot.send_message(message.chat.id, message_text)

    # adding new formula with needen params
    # get year
    elif message.text.lower().startswith('класс:'):
        new_year = int(message.text[len('класс:') + 1:])
        add_formula(new_year)
        bot.send_message(message.chat.id, 'С классом определились. Введите тему: .....')

    # get topic
    elif message.text.lower().startswith('тема:'):
        new_topic = message.text[len('тема:') + 1:]
        session = create_session()
        session.execute(
            update(Formula)
                .where(Formula.is_finished == False)
                .set(topic=new_topic)
        )
        bot.send_message(message.chat.id, 'С темой определились. Введите название формулы: .....')
        # bot.send_message(message.chat.id, 'Введите пояснения к формуле - пояснения: .....')

    # get name of formula
    elif message.text.lower().startswith('новая формула:'):
        new_formula_name = message.text[len('новая формула:') + 1:]
        session = create_session()
        session.execute(
            update(Formula)
                .where(Formula.is_finished == False)
                .values(formula_name=new_formula_name)
        )
        bot.send_message(message.chat.id,
                         'Так с названием разобрались, продолжим. Введите формулу в формате - формула: .....')

    # get formula
    elif message.text.lower().startswith('формула: '):
        new_formula = message.text[len('формула: ') + 1:]
        session = create_session()
        session.execute(
            update(Formula)
                .where(Formula.is_finished == False)
                .values(formula=new_formula)
        )
        bot.send_message(message.chat.id, 'Так формула есть, продолжим. Введите пояснения в формате - пояснения: .....')

    # get explanation
    elif message.text.lower().startswith('пояснения:'):
        new_explanation = message.text[len('пояснения:') + 1:]
        session = create_session()
        session.execute(
            update(Formula)
                .where(Formula.is_finished == False)
                .values(explanation=new_explanation)
        )
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        i_dont_understand = types.KeyboardButton("Обьяснение")
        markup.add(i_dont_understand)
        bot.send_message(message.chat.id, 'Пояснение принято. Теперь напишите детали - детали:....'
                                          'Если не знаете что такое детали, нажмите на кнопку обьяснение. ',
                         reply_markup=markup)

    # get details
    elif message.text.lower().startswith('детали:'):
        new_details = message.text[len('детали:') + 1:]
        session = create_session()
        session.execute(
            update(Formula)
                .where(Formula.is_finished == False)
                .values(details=new_details)
        )
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        all_done = types.KeyboardButton("формула готова")
        markup.add(all_done)
        bot.send_message(message.chat.id,
                         'Детали успешно добавлены. Чтобы завершить нажмите на кнопку или напишите формула готова.',
                         reply_markup=markup)

    elif message.text.lower() == 'формула готова':
        session = create_session()
        session.execute(
            update(Formula)
                .where(Formula.is_finished == False)
                .values(is_finished=True)
        )
        bot.send_message(message.chat.id, 'Формула добавлена в каталог.')

    elif message.text.lower() == 'обьяснение':
        bot.send_message(message.chat.id, 'what_to_do.txt')


def add_grade(chat_id, grade):
    session = create_session()
    session.execute(
        update(User)
            .where(User.user_id == chat_id)
            .values(grade=grade)
    )
    session.commit()


def get_all_formulas():  # получение всех формул за все классы(работает)
    session = create_session()
    notes = session.query(Formula).all()
    if len(notes) == 0:
        return 'Это были все формулы, которые у нас есть.'
    return '\n'.join(
        f'{note.topic}, {note.formula_name}, {note.formula}, {note.explanation}, {note.details}' for note in notes)


# get one formula(работает)
def get_needen_formula(chat_id, what_to_find):
    session = create_session()
    user = session.query(User).filter(User.user_id == chat_id).one()
    print(what_to_find)
    print(user.grade)
    formula = session.query(Formula).filter(Formula.formula_name == what_to_find, Formula.year == user.grade).one()
    if formula is None:
        return 'Формула не найдена'
    return f'{formula.formula_name}, {formula.formula}, {formula.explanation}'


# find topic
def get_needen_topic(chat_id, topic_to_find):
    session = create_session()
    user = session.query(User).filter(User.user_id == chat_id).one()
    print(topic_to_find)
    print(user.grade)
    print(session.query(Formula).filter(Formula.topic == topic_to_find, Formula.year == user.grade))
    notes = session.query(Formula).filter(Formula.topic == topic_to_find, Formula.year == user.grade).all()
    if len(notes) == 0:
        return ['Формула не найдена']
    return [f'{note.topic}, {note.formula_name}, {note.formula}, {note.explanation}, {note.details}'
            for note in notes]


def add_formula(year):
    session = create_session()
    formula = Formula(
        year=year,
    )
    session.add(formula)
    session.commit()


main()
