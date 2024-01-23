import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ContentType

from aiogram.types import Message

# TOKEN = "5981385948:AAFanZJHTSB06sYa7htLfEdxdQAvEjCZCz8"
TOKEN = "6918495864:AAHdnlUy0qx58rkS1x_5OgcL61dOqvWlnuE"

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(F.document)
async def het_doc(message: Message):
    if message.document:
        await message.forward(359888384)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
