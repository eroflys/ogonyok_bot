#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import sqlite3


def start(update, context):
    reply_keyboard = [['А что за конференция?', 'Популярные вопросы', 'Cайт и соцсети'], ['Хочу зарегистрироваться', 'Расселение', 'Как добраться?'], ['Спикеры', 'Программа конференции', 'Мастер-классы']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Привет, на связи Огонек - чат-бот конференции, готов помочь тебе, что тебя интересует?', reply_markup=markup)


def ques(update, context):
    reply_keyboard = [['Что входит в регистрацию?', 'Будет ли расселение?'], ['Будут подростков сопровождать взрослые, у которых они живут?'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Какой вопрос интересует?', reply_markup=markup)


def anwir(update, context):
    reply_keyboard = [['Другой вопрос', 'Хочу зарегистрироваться'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''В регистрацию входит: участие в конференции, стартовый пакет. Целевое пожертвование — 500₽.
Еда оплачивается отдельно при регистрации: один день +300₽ (завтрак, обед, перекус)''', reply_markup=markup)


def anras(update, context):
    reply_keyboard = [['Другой вопрос', 'Хочу зарегистрироваться'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Да, будет, но заявку надо подать до 31.05.2021.
Подается заявка в форме регистрации''', reply_markup=markup)


def ansop(update, context):
    reply_keyboard = [['Другой вопрос', 'Хочу зарегистрироваться'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Скорее всего нет, поэтому рекомендуем заранее убедиться, чтобы подросток самостоятельно смог провести все дни конференции в Москве''', reply_markup=markup)


def geo(update, context):
    reply_keyboard = [['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("""Все служения и мастер-классы проходят по адресу главного здания церкви: `г. Москва, ул. Павла Корчагина, д.2а`, советуем скачать карты, чтобы точно не заблудиться
Ссылки на геолокацию в популярных приложениях:
yandex:  https://yandex.ru/maps/-/CCU44JRNSC
google:  https://goo.gl/maps/As7GB44wEq7myDLb7
2gis:  https://go.2gis.com/1o4q1""", reply_markup=markup, parse_mode = 'Markdown')


def arm(update, context):
    reply_keyboard = [['Посмотреть других спикеров'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Армен - второй молодежный пастор, подростковый лидер церкви «Слово жизни» Москва.
ig:  https://www.instagram.com/armenij/''', reply_markup=markup)


def rom(update, context):
    reply_keyboard = [['Посмотреть других спикеров'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Алексей - молодежный пастор церкви «Слово жизни» Москва.
ig:  https://www.instagram.com/pastor.romanov/''', reply_markup=markup)


def evg(update, context):
    reply_keyboard = [['Посмотреть других спикеров'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Евгений - подростковый пастор церкви «Слово жизни»  Саратов.
ig:  https://www.instagram.com/genyabrr/''', reply_markup=markup)


def vch(update, context):
    reply_keyboard = [['Посмотреть других спикеров'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Вячеслав - подростковый пастор церкви «Слово жизни» Самара.
ig:  https://www.instagram.com/pastorslava/''', reply_markup=markup)


def mar(update, context):
    reply_keyboard = [['Посмотреть других спикеров'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Мария - лидер служения «Мое поколение» в России..
ig:  https://www.instagram.com/podolskayamaria/''', reply_markup=markup)


def speak(update, context):
    reply_keyboard = [['Армен Асатрян', 'Алексей Романов'], ['Евгений Брощенко', 'Вячеслав Шпаковский', 'Мария Подольская'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('О ком хочешь узнать?', reply_markup=markup)


def resettlement(update, context):
    reply_keyboard = [['Рeгистрация для служителей', 'Рeгистрация для подростков'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Расселение бесплатное. Но заявку важно подать до 31.05.2021', reply_markup=markup)


def regfteen(update, context):
    reply_keyboard = [['Назад', 'В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Подростки до 18 лет должны иметь при себе разрешение от родителей, а также доверенность на сопровождающего (совершеннолетнее лицо). Скачайте документы для заполнения и подписи.
Переходи по ссылке и регистрируйся:  https://my.wolrus.org/forms/teensconf''', reply_markup=markup)


def regfteenr(update, context):
    reply_keyboard = [['Hазад', 'В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Подростки до 18 лет должны иметь при себе разрешение от родителей, а также доверенность на сопровождающего (совершеннолетнее лицо). Скачайте документы для заполнения и подписи.
Переходи по ссылке и регистрируйся:  https://my.wolrus.org/forms/teensconf''', reply_markup=markup)


def regfadu(update, context):
    reply_keyboard = [['Назад', 'В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Переходи по ссылке и регистрируйся:  https://my.wolrus.org/forms/teensconf_serve', reply_markup=markup)


def regfadur(update, context):
    reply_keyboard = [['Hазад', 'В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Переходи по ссылке и регистрируйся:  https://my.wolrus.org/forms/teensconf_serve', reply_markup=markup)


def asreg(update, context):
    reply_keyboard = [['Регистрация для служителей', 'Регистрация для подростков'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''Хочешь зарегистрироваться на конференцию? Красавчик.
Расселение бесплатное. Но заявку важно подать до 31.05.2021''', reply_markup=markup)


def about(update, context):
    reply_keyboard = [['Хочу зарегистрироваться'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('9–11 июня пройдет первая подростковая конференция «Огонь» в Москве. Мы верим, что подростки — будущее церкви, которое призвано влиять на следующие поколения. Именно поэтому так важно вкладывать в них правильные ценности уже сейчас. На конференции мы коснемся практических моментов и ответим на вопросы о подростковом служении.', reply_markup=markup)


def sites(update, context):
    reply_keyboard = [['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''ВК:  https://vk.com/wolrusteens
ig:  https://www.instagram.com/wolrusteens/
TikTok:  https://www.tiktok.com/@rusteens
Сайт:  https://wolrus.org/event/teensconf''', reply_markup=markup)


def maskl(update, context):
    reply_keyboard = [['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Совсем скоро мы поделимся подробностями, а пока, почему бы не посмотреть наш музыкальный клип?')
    update.message.reply_text('Правда, круто получилось? https://vk.com/videos-49066020?z=video-49066020_456239140%2Fclub49066020%2Fpl_-49066020_-2', reply_markup=markup)


def prog(update, context):
    reply_keyboard = [['День первый, 9 июня, среда','День второй, 10 июня, четверг', 'День третий, 11 июня, пятница'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Какой день тебя интересует?', reply_markup=markup)


def firstd(update, context):
    reply_keyboard = [['Хочу зарегистрироваться', 'День второй, 10 июня, четверг', 'День третий, 11 июня, пятница'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''9:00 регистрация и актив в фойе

12:00 актив

13:00 огненные мастер-классы для подростков

13:00 огненные мастер-классы для служителей

14:00 обед

15:00 большая игра

16:00 богослужение

18:00 Квест: Зарядье + Красная площадь (от 14 лет)''', reply_markup=markup)


def secd(update, context):
    reply_keyboard = [['День первый, 9 июня, среда', 'Хочу зарегистрироваться', 'День третий, 11 июня, пятница'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''8:00 завтрак и квест на ВДНХ

10:00 богослужение

11:40 огненные мастер-классы для подростков

11:40 огненные мастер-классы для служителей

12:40 обед

13:20 большая игра

15:20 актив в фойе

16:00 богослужение

18:00 квест: Парк Горького + Музеон + Храм Христа Спасителя (от 14 лет)''', reply_markup=markup)


def thid(update, context):
    reply_keyboard = [['День первый, 9 июня, среда', 'День второй, 10 июня, четверг', 'Хочу зарегистрироваться'], ['В начало']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('''8:00 завтрак и актив в фойе

10:00 богослужение

11:40 огненные мастер-классы для подростков

11:40 огненные мастер-классы для служителей

12:40 обед

13:20 большая игра

15:20 актив в фойе

16:00 богослужение

18:00 творческий вечер''', reply_markup=markup)


def chlvl(update, context):
    if update['message']['text'] == 'Cайт и соцсети':
        sites(update, context)
    elif update['message']['text'] == 'Мастер-классы':
        maskl(update, context)
    elif update['message']['text'] == 'В начало':
        start(update, context)
    elif update['message']['text'] == 'Программа конференции':
        prog(update, context)
    elif update['message']['text'] == 'День первый, 9 июня, среда':
        firstd(update, context)
    elif update['message']['text'] == 'День второй, 10 июня, четверг':
        secd(update, context)
    elif update['message']['text'] == 'День третий, 11 июня, пятница':
        thid(update, context)
    elif update['message']['text'] == 'А что за конференция?':
        about(update, context)
    elif update['message']['text'] == 'Хочу зарегистрироваться':
        asreg(update, context)
    elif update['message']['text'] == 'Расселение':
        resettlement(update, context)
    elif update['message']['text'] == 'Спикеры':
        speak(update, context)
    elif update['message']['text'] == 'Регистрация для служителей':
        regfadu(update, context)
    elif update['message']['text'] == 'Регистрация для подростков':
        regfteen(update, context)
    elif update['message']['text'] == 'Рeгистрация для служителей':
        regfadur(update, context)
    elif update['message']['text'] == 'Рeгистрация для подростков':
        regfteenr(update, context)
    elif update['message']['text'] == 'Армен Асатрян':
        arm(update, context)
    elif update['message']['text'] == 'Алексей Романов':
        rom(update, context)
    elif update['message']['text'] == 'Евгений Брощенко':
        evg(update, context)
    elif update['message']['text'] == 'Вячеслав Шпаковский':
        vch(update, context)
    elif update['message']['text'] == 'Мария Подольская':
        mar(update, context)
    elif update['message']['text'] == 'Как добраться?':
        geo(update, context)
    elif update['message']['text'] == 'Посмотреть других спикеров':
        speak(update, context)
    elif update['message']['text'] == 'Популярные вопросы':
        ques(update, context)
    elif update['message']['text'] == 'Будет ли расселение?':
        anras(update, context)
    elif update['message']['text'] == 'Что входит в регистрацию?':
        anwir(update, context)
    elif update['message']['text'] == 'Будут подростков сопровождать взрослые, у которых они живут?':
        ansop(update, context)
    elif update['message']['text'] == 'Другой вопрос':
        ques(update, context)
    elif update['message']['text'] == 'Hазад':
        resettlement(update, context)
    elif update['message']['text'] == 'Назад':
        asreg(update, context)
    else:
        update.message.reply_text('Для работы с ботом используйте команду /start.')


def main():
    updater = Updater('1741302417:AAE3AtNZfawhExdWS8rIA3XpCC125qNHsXY', use_context=True)

    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, chlvl)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()