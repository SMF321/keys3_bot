from turtle import back
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

user_menu_button = ['Информация о проекте',
                    'Действующие проедложения', 'История моих обращений']
admin_menu_button = ['Просмотр обращений по темам',
                     'Добавить кнопку', 'Удалить кнопку']
topics_for_appeals = ['Кошечки', 'Собачки']
back_button_or_not = ['Принять участие','Назад']
help_button = ['Просмотреть предложения']


def add_button(mass):
    buttons = ReplyKeyboardMarkup(True, True, True)
    for i in range(len(mass)):
        keyboad = KeyboardButton(mass[i])
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
