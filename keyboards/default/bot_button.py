from turtle import back
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.main import *

user_menu_button = ['ℹ️ Информация о проекте ℹ️',
                    '🔍 Действующие предложения 🔎', '🕒 История моих обращений 🕤', '🔐 Ключевое слово 🔐']


def admin_menu_button():
    test = GET_ALL_NULL()
    admin_menu_button = ['Обновить',
    f'Просмотр количества новых сообщений : {GET_ALL_NULL()}',
    'Просмотр обращений по темам/Добавить в бан-лист',
    'Добавить открытую тему обращения', 
    'Удалилить открытую тему обращения', 
    'Добавить секретную тему',
    'Удалить секретную тему']
    return admin_menu_button


topics_for_appeals = ['Кошечки', 'Собачки']
back_button_or_not = ['Принять участие', 'Назад']
help_button = ['Просмотреть предложения']
admin_1_button = ['Следующее объявление',
                  'Убрать пользователя в бан-лист', 'Назад']
back_bat = ['Назад']
back_add = KeyboardButton(back_bat[0])


def add_button(mass):
    buttons = ReplyKeyboardMarkup(True, True, True)
    for i in range(len(mass)):
        keyboad = KeyboardButton(mass[i])
        buttons.add(keyboad)
    return buttons


def add_button_cont(mass):
    buttons = ReplyKeyboardMarkup(True, True, True)
    for i in range(len(mass)):
        keyboad = KeyboardButton(f'{mass[i]} : {GET_COUNT_MESSAGE(mass[i])}')
        buttons.add(keyboad)
    return buttons


predlojeniya = [
    'Создание Бота который может варить кофе',
    'Создание всемогущего сайта',
    'Создание чего-то для Сбера'
]


# user_menu_button1 = KeyboardButton('Информация о проекте')
# user_menu_button2 = KeyboardButton('Заполнение анкеты')
# user_menu_button3 = KeyboardButton('История моих обращений')

# user_menu = ReplyKeyboardMarkup(True,True)
# user_menu.add(user_menu_button1).add(user_menu_button2).add(user_menu_button3)
