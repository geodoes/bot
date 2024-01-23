import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from texts import prices, hello, services
from keyboards import keyboard_pagination, keyboard_help
import keyboards

# TOKEN = "5981385948:AAFanZJHTSB06sYa7htLfEdxdQAvEjCZCz8" MAIN GIS
TOKEN = "6918495864:AAHdnlUy0qx58rkS1x_5OgcL61dOqvWlnuE"

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer(hello, reply_markup=keyboard_pagination(), parse_mode=ParseMode.HTML)


@dp.callback_query(keyboards.MyPagination.filter(F.action.in_(["price", "services", "maps", "help", "data"])))
async def process_butons(call: CallbackQuery, callback_data: keyboards.MyPagination):
    if callback_data.action == "price":
        page = 1
        await call.message.answer(text=prices, parse_mode=ParseMode.HTML, reply_markup=keyboard_pagination(page))
    if callback_data.action == "services":
        page = 2
        await call.message.answer(text=services, parse_mode=ParseMode.HTML, reply_markup=keyboard_pagination(page))
    if callback_data.action == "site":
        page = 3
        await call.message.answer(text="Вы будете перенаправлены на сайт", reply_markup=keyboard_pagination(page))
    if callback_data.action == "help":
        page = 4
        await call.message.answer(text="Выберете действие", parse_mode=ParseMode.HTML, reply_markup=keyboard_help(page))
    if callback_data.action == "data":
        page = 5
        await call.message.answer(text="Следующий шаг", parse_mode=ParseMode.HTML, reply_markup=keyboard_help(page))



@dp.callback_query(keyboards.MyPagination.filter(F.action.in_(["fileexchange"])),F.document)
async def resend_file(call: CallbackQuery, callback_data: keyboards.MyPagination,):
    if call.document:
        await call.forward(359888384)
    else:
        print("Not a document")
    await call.answer(text="Прикрепите файл 📎")



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
