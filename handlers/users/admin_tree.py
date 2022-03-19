from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.bot_states import Register
from keyboards.default.bot_button import add_button, admin_menu_button, topics_for_appeals,admin_1_button
from utils.db_api.main import *
kostil = ""

@dp.message_handler(state=Register.admin_start, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == admin_menu_button[0]:
        await message.answer(f"Выберите тему по которой хотите просмотреть обращения", reply_markup=add_button(GET_SUGGESTIONS()))
        await Register.viewing_and_editing_requests.set()
        # await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))
    elif message.text == admin_menu_button[1]:
        await message.answer(f"Введите название темы по которую хотите добавить:")
        await Register.created_chat.set()
        # await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    elif message.text == admin_menu_button[2]:
        await message.answer(f"Выберите тему для удаления:", reply_markup=add_button(GET_SUGGESTIONS()))
        await Register.deleted.set()
    elif message.text == admin_menu_button[3]:
        await message.answer(f"Выберите тему для просмотра количества новых сообщений :", reply_markup=add_button(GET_SUGGESTIONS()))
        await Register.count.set()

@dp.message_handler(state=Register.count, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in GET_SUGGESTIONS():
        await message.answer(f'Количество новых сообщений : {GET_COUNT_MESSAGE(message.text)}') 
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))

@dp.message_handler(state=Register.viewing_and_editing_requests, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    global kostil
    if message.text in GET_SUGGESTIONS():
        kostil = message.text
        await message.answer(f'Имя пользоваетя : @{GET_VIEW(kostil)[1]}\n'+f'Текст обращения :\n{GET_VIEW(kostil)[0]}', reply_markup=add_button(admin_1_button))
    if message.text in GET_SUGGESTIONS() or message.text == 'Следующее объявление':
        if message.text == 'Следующее объявление':
            await message.answer(f'Имя пользоваетя : @{GET_VIEW(kostil)[1]}\n'+f'Текст обращения :\n{GET_VIEW(kostil)[0]}', reply_markup=add_button(admin_1_button))
            
    elif message.text == 'Назад':
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))
    elif message.text == 'Убрать пользователя в бан-лист':
        # TODO
        await message.answer('Пользователь забанен!!!')
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))

@dp.message_handler(state=Register.created_chat, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer(f"Введите описание данной темы")
    POST_NEW_SUGGESTIONS1(message.text)
    await Register.created_chat1.set()



@dp.message_handler(state=Register.created_chat1, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    POST_NEW_SUGGESTION_DESCRIPTION(message.text)
    await message.answer(f"Изменения приняты:")
    for i in GET_SUGGESTIONS():
        await message.answer('✔️ ' + f'{i}')
    await Register.admin_start.set()
    await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))


@dp.message_handler(state=Register.deleted, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    DELETE_SUGGESTION(message.text)
    await message.answer(f"Изменения приняты:")
    for i in GET_SUGGESTIONS():
        await message.answer('❌ '+f'{i}')
    await Register.admin_start.set()
    await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))