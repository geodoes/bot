from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MyPagination(CallbackData, prefix="pg"):
    action: str
    page: int

def keyboard_pagination(page : int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Ценообразование",callback_data=MyPagination(action = "price", page = page).pack()),
        InlineKeyboardButton(text="Услуги", callback_data=MyPagination(action="services", page=page).pack()),
        InlineKeyboardButton(text="Мое хранилище", callback_data=MyPagination(action="data", page=page).pack()),
        InlineKeyboardButton(text="Перейти на сайт",url=f'https://gsengr.ru', callback_data=MyPagination(action="site", page=page).pack()),
        InlineKeyboardButton(text="Помощь/Консультация", callback_data=MyPagination(action="help", page=page).pack()),

    )
    builder.adjust(2,2)

    return builder.as_markup()
