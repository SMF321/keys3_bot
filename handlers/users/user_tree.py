from aiogram import types
from aiogram.dispatcher import FSMContext
import re

from loader import dp

from states.bot_states import Register
from keyboards.default.bot_button import user_menu_button, add_button, help_button, back_button_or_not, back_add
from utils.db_api.main import *
#import GET_SUGGESTIONS, GET_DESCRIPTION,POST_USER_DATA, POST_USER,UPDATE__USER_DATA_USER,POST_QUESTION,POST_CLASS_QUESTION,POST_PHONE


@dp.message_handler(state=Register.user_start, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.chat.id in GET_BAN():
        await message.answer('❗️Вы были забанены администратором❗️')
    else:
        if message.text == user_menu_button[0]:
            await message.answer(f"Данный проект предназначен для следующих целей:\n☝️ Набрать команду востребованных специалистов для решения различных задач.\n📲 Для удобного использования как корреспонденами так и менеджерами.\n☎️ Дает возможность легко связывать менеджеров с корреспонденами.")
            await Register.user_start.set()
            await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
        elif message.text == user_menu_button[1]:
            await message.answer(f"❗️ Перед выбором тем обращений внимательно ознакомьтесь с содержанием требований❗️", reply_markup=add_button(help_button))
            await Register.project_list.set()
            # await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
        elif message.text == user_menu_button[2]:
            await message.answer(f"📜Ваша история обращений📜:")
            for i in range(len(GET_QUESTION(message.chat.id)[0])):
                await message.answer(f"Тема обращения : {(GET_QUESTION(message.chat.id)[1][i])}\n" + f"Текст обращения : {(GET_QUESTION(message.chat.id)[0][i])}")
            await Register.user_start.set()
            await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
        elif message.text == user_menu_button[3]:
            await message.answer(f"🔑 Введите секретный ключ 🔑")
            await Register.sekret.set()


@dp.message_handler(state=Register.sekret, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    if message.text in GET_SECRET_KEY():
        await message.answer('☑️ Вы успешно авторизованы \nПросмотрите список приватных предложений:', reply_markup=add_button(GET_SECRET_SUGGESTION(message.text)).add(back_add))
        await Register.print_sekret_topics.set()
    else:
        await Register.user_start.set()
        await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))


@dp.message_handler(state=Register.print_sekret_topics, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    if message.text in GET_SECRET_SUGGESTION_ALL():
        POST_TEST(message.chat.id)
        POST_CLASS_QUESTION(message.chat.id, message.text)
        await message.answer(GET_SECRET_DESCRIPTION(message.text))
        await message.answer('📝Напишите что-то о себе📝\n(Например : Я самый лучший работник, владею 5 языками.)')
        await Register.quesion.set()
    elif message.text == 'Назад':
        await Register.user_start.set()
        await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
    else:
        await message.answer('Список действующих пердложений:', reply_markup=add_button(GET_SECRET_SUGGESTION(message.text)).add(back_add))
        await Register.print_sekret_topics.set()


@dp.message_handler(state=Register.project_list, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    try:
        POST_USER_DATA(message.chat.id, message.chat.username)
    except:
        pass
    await message.answer('📄Список действующих пердложений📄:', reply_markup=add_button(GET_SUGGESTIONS()).add(back_add))
    await Register.info_about_work.set()


@dp.message_handler(state=Register.info_about_work, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in GET_SUGGESTIONS():
        POST_TEST(message.chat.id)
        POST_CLASS_QUESTION(message.chat.id, message.text)
        await message.answer(GET_DESCRIPTION(message.text))
        await message.answer('📝Напишите что-то о себе📝\n(Например : Я самый лучший работник, владею 5 языками.)')
        await Register.quesion.set()
    elif message.text == 'Назад':
        await Register.user_start.set()
        await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
    else:
        await message.answer('Список действующих пердложений:', reply_markup=add_button(GET_SUGGESTIONS()).add(back_add))
        await Register.info_about_work.set()


@dp.message_handler(state=Register.info_about_concrete_work, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == back_button_or_not[1]:
        await Register.user_start.set()
        await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
    elif message.text == back_button_or_not[0]:
        await message.answer('📝Напишите что-то о себе📝\n(Например : Я самый лучший работник, владею 5 языками.)')
        await Register.quesion.set()


@dp.message_handler(state=Register.quesion, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    POST_QUESTION(message.chat.id, message.text)
    POST_QUESTION_DELETE()
    await message.answer('🎊 Спасибо за Ваше обращение\n📬 Мы свяжемся с Вами в ближайшее время.\n❓ По интерисующим вопросам обращаться сюда.\nhttps://t.me/Text_project')
    await Register.user_start.set()
    await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
