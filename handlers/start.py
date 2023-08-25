from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import Database
from keyboards.fsm_form_keyboard import new_start


async def start_button(message: types.Message):
    print(message)
    Database().sql_insert_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await message.reply(text="hi",
                        reply_markup=await new_start())




def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])