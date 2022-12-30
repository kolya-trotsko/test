import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '1946562538:AAFfw_CFeOcDRfoLpQdLeWc_4-Y5zvsjh3A'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_message(message: types.Message):
    r_msg = message.text[::-1]

    await bot.send_message(message.from_user.id, r_msg)

executor.start_polling(dp)