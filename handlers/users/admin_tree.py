from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.bot_states import Register
from keyboards.default.bot_button import add_button, admin_menu_button, topics_for_appeals,admin_1_button,add_button_cont
from utils.db_api.main import *
kostil = ""

@dp.message_handler(state=Register.admin_start, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == admin_menu_button()[0]:
        await message.answer(f"Выберите тему, по которой хотите просмотреть обращения", reply_markup=add_button(GET_UNIQE_CLASS_QUESTION()))
        await Register.viewing_and_editing_requests.set()
        # await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button))
    elif message.text == admin_menu_button()[1]:
        await message.answer(f"Введите название темы, которую хотите добавить:")
        await Register.created_chat.set()
        # await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    elif message.text == admin_menu_button()[2]:
        await message.answer(f"Выберите тему для удаления:", reply_markup=add_button(GET_SUGGESTIONS()))
        await Register.deleted.set()
    elif message.text.split(' ')[1] == admin_menu_button()[3].split(' ')[1]:
        await message.answer(f"Количество новых сообщений :", reply_markup=add_button_cont(GET_UNIQE_CLASS_QUESTION()))
        await message.answer(f"Нажмите на любую кнопку.")
        await Register.count.set()
    elif message.text == admin_menu_button()[4]:
        await message.answer(f"Введите секретный ключ, который хотите добавить:")
        await Register.add_sekret.set()
    elif message.text == admin_menu_button()[5]:
        await message.answer(f"Выберите тему для удаления:", reply_markup=add_button(GET_UNIQE_SECRET_SUGGESTION()))
        await Register.del_sekret.set()


@dp.message_handler(state=Register.del_sekret, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in GET_UNIQE_SECRET_SUGGESTION():
        DELETE_SECRET_SUGGESTION(message.text)
        await message.answer('Вы успешно удалили секретную тему')
        await message.answer(f'Список секретных тем :')
        for i in GET_UNIQE_SECRET_SUGGESTION():
            await message.answer('❌ '+f'{i}')
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
        await Register.admin_start.set()
    else:
        await message.answer(f'Вы где-то ошиблись при заполнеии')
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
        await Register.admin_start.set()



@dp.message_handler(state=Register.add_sekret, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    POST_SECRET_KEY(message.text)
    await message.answer(f"Введите название для данной секретной темы:")
    await Register.add_sekret2.set()



@dp.message_handler(state=Register.add_sekret2, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    POST_SECRET_SUGGESTION(message.text)
    await message.answer(f"Введите описание для данной секретной темы:")
    await Register.add_sekret3.set()

@dp.message_handler(state=Register.add_sekret3, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    POST_SECRET_DESCRIPTION(message.text)
    await message.answer(f"Секретная тема успешно добавлена")
    await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
    await Register.admin_start.set()

@dp.message_handler(state=Register.count, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == f'Просмотр количества новых сообщений : {GET_ALL_NULL()}':
        await message.answer(f'Количество новых сообщений : {GET_COUNT_MESSAGE(message.text)}') 
        await Register.admin_start.set()
    else:
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
        await Register.admin_start.set()

@dp.message_handler(state=Register.viewing_and_editing_requests, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    global kostil
    if message.text in GET_UNIQE_CLASS_QUESTION():
        kostil = message.text
        print(kostil)
        test = GET_VIEW(kostil)
        if test == 'Все записи по данной теме просмотрены':
            await message.answer('Все записи по данной теме просмотрены')
            await Register.admin_start.set()
            await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
        else:
            await message.answer(f'Имя пользоваетя : @{test[1]}\n'+f'Текст обращения :\n{test[0]}', reply_markup=add_button(admin_1_button))
    if message.text == 'Следующее объявление':
        print(kostil)
        test = GET_VIEW(kostil)
        if test == 'Все записи по данной теме просмотрены':
            await message.answer('Все записи по данной теме просмотрены')
            await Register.admin_start.set()
            await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
        else:
            await message.answer(f'Имя пользоваетя : @{test[1]}\n'+f'Текст обращения :\n{test[0]}', reply_markup=add_button(admin_1_button))
    elif message.text == 'Назад':
        await Register.admin_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))
    elif message.text == 'Убрать пользователя в бан-лист':
        await message.answer('Укажите username пользоватеся : \n(Напимер : @test)')
        await Register.ban.set()


@dp.message_handler(state=Register.ban, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer(BAN(message.text) )
    await Register.admin_start.set()
    await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))

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
    await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))


@dp.message_handler(state=Register.deleted, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    DELETE_SUGGESTION(message.text)
    await message.answer(f"Изменения приняты:")
    for i in GET_SUGGESTIONS():
        await message.answer('❌ '+f'{i}')
    await Register.admin_start.set()
    await message.answer(f"Меню:", reply_markup=add_button(admin_menu_button()))