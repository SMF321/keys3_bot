from aiogram.dispatcher.filters.state import State, StatesGroup


class Register (StatesGroup):  # создаю класс где буду хранить данные
    admin_start = State()
    viewing_and_editing_requests = State()
    created_chat = State()
    created_chat1 = State()


##############################

    user_start = State()
    info_for_user = State()
    project_list = State()
    info_about_work = State()
    info_about_concrete_work = State()
    questionnaire = State()
    fio = State()
    organization = State()
    mobile_phone = State()
    quesion = State()
