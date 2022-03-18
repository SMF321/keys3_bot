from aiogram import types
from aiogram.dispatcher import FSMContext
import re

from loader import dp

from states.bot_states import Register
from keyboards.default.bot_button import user_menu_button, add_button, help_button,back_button_or_not
from utils.db_api.main import GET_SUGGESTIONS, GET_DESCRIPTION,POST_USER_DATA, POST_USER,UPDATE__USER_DATA_USER


@dp.message_handler(state=Register.user_start, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == user_menu_button[0]:
        await message.answer(f"тут какаято инфа. Далее возврат в меню")
        await Register.user_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    elif message.text == user_menu_button[1]:
        await message.answer(f"Тут какая-то вступительная фраза перед ознакомлением с проектами, эта фраза тут необходима",reply_markup=add_button(help_button))
        await Register.project_list.set()
        # await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    elif message.text == user_menu_button[2]:
        await message.answer(f"тут будет колин запрос к бд")
        await Register.user_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))


@dp.message_handler(state=Register.project_list, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    await message.answer('Список действующих пердложений:', reply_markup=add_button(GET_SUGGESTIONS()))
    await Register.info_about_work.set()


@dp.message_handler(state=Register.info_about_work, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == GET_SUGGESTIONS()[0]:
        await message.answer(GET_DESCRIPTION(message.text),reply_markup=add_button(back_button_or_not))
        await Register.info_about_concrete_work.set()
        
    elif message.text == GET_SUGGESTIONS()[1]:
        await message.answer(GET_DESCRIPTION(message.text),reply_markup=add_button(back_button_or_not))
        await Register.info_about_concrete_work.set()
    elif message.text == GET_SUGGESTIONS()[2]:
        await message.answer(GET_DESCRIPTION(message.text),reply_markup=add_button(back_button_or_not))
        await Register.info_about_concrete_work.set()

@dp.message_handler(state=Register.info_about_concrete_work, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == back_button_or_not[1]:
        await Register.user_start.set()
        await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    elif message.text == back_button_or_not[0]:
        await message.answer('Представьтесь:\n(Например : Иванов Иван Иванович)')
        await Register.fio.set()



@dp.message_handler(state=Register.fio, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    match = re.search(
        r'[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', rf'{message.text}')
    try:
        if match.group(0):
            try:
                POST_USER(message.chat.id,message.text)
                POST_USER_DATA(message.chat.id,message.text,message.chat.username)
            except:
                UPDATE__USER_DATA_USER(message.chat.id,message.text,message.chat.username)
            await message.answer('Напишите что-то о себе чтоб вас взли в этот проект...')
            await Register.organization.set()
            # try:
                # POST_USER(message.chat.id, message.text)
            # except:
                # POST_EDIT_FIO(message.chat.id, message.text)
    except:
        await message.answer(f"Попробуйте еще раз:\n(Например : Иванов Иван Иванович)")
        await Register.fio.set()




@dp.message_handler(state=Register.organization, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    # TODO kolya and ser
    await message.answer('Оставьте нам свой номер телефона.\nЭто необходимо чтоб добвить Вас в группу-обсцждение.\nОбязуемся не делисться Вашими персональными данными.\n(Например : +71234567890)')
    await Register.quesion.set()


@dp.message_handler(state=Register.quesion, content_types=types.ContentTypes.ANY)
async def fio_regular(message: types.Message, state: FSMContext):
    match1 = re.search(
        r'(\+7|8)\d{10}$', rf'{message.text}')
    try:
        if match1.group(0):
            # POST_PHONE(message.chat.id, message.text)
            await message.answer('Спасибо за Ваш вопрос, мы свяжемся с Вами в ближайшее время.\nЕсли Вас добавят в группу не удивляйтесь')
            await Register.user_start.set()
            await message.answer(f"Меню:", reply_markup=add_button(user_menu_button))
    except:
        await message.answer('Оставьте нам свой номер телефона.\nЭто необходимо чтоб добвить Вас в группу-обсцждение.\nОбязуемся не делисться Вашими персональными данными.\n(Например : +71234567890)')
        await Register.quesion.set()
    
