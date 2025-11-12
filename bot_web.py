from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8225509684:AAEl9aBjlkUi1-xfj-EQ9pm24_a-5yL3-iY"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo(url="https://n8n.srv1047766.hstgr.cloud/webhook/f29fa2c0-b04f-45d7-930f-5256e5c84d0b")  # Replace with your domain
    button = types.KeyboardButton(text="Open Web App", web_app=web_app)
    keyboard.add(button)
    await message.answer("Click below to open the hybrid app:", reply_markup=keyboard)

@dp.message_handler(content_types="web_app_data")
async def get_web_app_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Got this from your web app: {data}")

executor.start_polling(dp)
