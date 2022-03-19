from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from states.bot_states import Register
from loader import dp
from data.config import ADMINS
from states.bot_states import Register
from keyboards.default.bot_button import add_button, user_menu_button, admin_menu_button


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    if str(message.chat.id) in ADMINS:
        await message.answer(f"Привет админ, {message.from_user.full_name}!")
        print(message.chat.id)
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
    else:
        await message.answer(f"🤖 Привет, {message.from_user.full_name} 🤖")
        print(message.chat.id)
        await Register.user_start.set()
        await message.answer(f"🤔 Меню 🤔", reply_markup=add_button(user_menu_button))
