# from aiogram import types
# from aiogram.dispatcher import FSMContext
# import re

# from loader import dp

# from states.bot_states import Register
# from keyboards.default.bot_button import user_menu_button, add_button

# @dp.message_handler(state=Register.fio, content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     match = re.search(r'[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?',rf'{message.text}')
#     print(match[0] if match else 'Not found') 
#     await message.answer(match)