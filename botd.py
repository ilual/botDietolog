from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

bot = Bot("5975719857:AAE78_sq1xnsTxR2P-JOdmuYCV36ao3Wz4s")
dp = Dispatcher(bot)

#KL1
Kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
b1 = KeyboardButton("список диет")
b2 = KeyboardButton("помощь")
b3 = KeyboardButton("выбор диеты")
b4 = KeyboardButton("сброс диеты")
b5 = KeyboardButton("о боте")
Kb.add(b1,b2,b3,b4,b5)

@dp.message_handler(commands = ["start"])
async def start_comsnd(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = f"Приветствую, {message.from_user.first_name}. Добро пожаловать в бота диетолога",
                           reply_markup=Kb)

@dp.message_handler(commands = ["help"])
async def help_comsnd(message: types.Message):
    mess = '''/start - начало работы с ботом
/diets - список диет
/help - помощь
/reset - сброс диеты
/fight - выбор диеты и начало похудения
/info - о боте'''
    await bot.send_message(chat_id = message.from_user.id, text = mess)

@dp.message_handler(lambda message: message.text == "список диет")
async def about_sport(message: types.Message):
    await message.reply("в этом списке 10 разных диет, но в будующкм их будет больше. Вы можете прочитать про каждую из них.")

@dp.message_handler(lambda message: message.text == "помощь")
async def about_sport(message: types.Message):
    await message.reply("/help")

@dp.message_handler(lambda message: message.text == "выбор диеты")
async def about_sport(message: types.Message):
    await message.reply("выберете диету которая понравилась вам больше всего")

@dp.message_handler(lambda message: message.text == "сброс диеты")
async def about_sport(message: types.Message):
    await message.reply("Вы точно хотите сбросить вашу диету?")

@dp.message_handler(lambda message: message.text == "о боте")
async def about_sport(message: types.Message):
    await message.reply("Бот диетолог помогает вам выбрать и соблюдать диету")

@dp.message_handler(commands = ["diets"])
async def help_comsnd(message: types.Message):
    mess = ""
    with open("D:/Dietolog/data/diets.txt", "r",encoding='UFT-8') as file:
        mess = file.read()
    await bot.send_message(chat_id = message.from_user.id, text = mess)

@dp.message_handler(commands = ["fight"])
async def help_comsnd(message: types.Message):
    mess = ""
    with open("D:/Dietolog/data/diets.txt", "r",encoding='UFT-8') as file:
        mess = file.read()
    await bot.send_message(chat_id = message.from_user.id, text = mess)

@dp.message_handler(commands = ["reset"])
async def help_comsnd(message: types.Message):
    mess = ""
    with open("D:/Dietolog/data/diets.txt", "r",encoding='UFT-8') as file:
        mess = file.read()
    await bot.send_message(chat_id = message.from_user.id, text = mess)

if __name__ == "__main__":
    executor.start_polling(dispatcher = dp)
