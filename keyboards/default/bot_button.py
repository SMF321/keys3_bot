from turtle import back
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.main import *

user_menu_button = ['Информация о проекте',
                    'Действующие предложения', 'История моих обращений']
admin_menu_button = ['Просмотр обращений по темам/Удалить обращение/Добавить в бан-лист',
                     'Добавить тему обращения', 'Удалилить тему обращения',f'Просмотр количества новых сообщений : {GET_ALL_NULL()}']
topics_for_appeals = ['Кошечки', 'Собачки']
back_button_or_not = ['Принять участие','Назад']
help_button = ['Просмотреть предложения']
admin_1_button = ['Следующее объявление','Убрать пользователя в бан-лист','Назад']
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
