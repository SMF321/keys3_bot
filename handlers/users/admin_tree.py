from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.bot_states import Register
from keyboards.default.bot_button import add_button, admin_menu_button, topics_for_appeals
from utils.db_api.main import *


@dp.message_handler(state=Register.admin_start, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == admin_menu_button[0]:
        await message.answer(f"Выберите тему по которой хотите просмотреть обращения", reply_markup=add_button(GET_SUGGESTIONS()))
        # TODO сделаю потом, но тут kolya
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))
    elif message.text == admin_menu_button[1]:
        await message.answer(f"Введите название темы по которую хотите добавить:")
        await Register.created_chat.set()
        # await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    elif message.text == admin_menu_button[2]:
        await message.answer(f"тут что-то будет")
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))


@dp.message_handler(state=Register.created_chat, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer(f"ВВедите описание данной темы")
    POST_NEW_SUGGESTIONS1(message.text)
    await Register.created_chat1.set()



@dp.message_handler(state=Register.created_chat1, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    POST_NEW_SUGGESTIONS1(message.text)
    await Register.created_chat1.set()
