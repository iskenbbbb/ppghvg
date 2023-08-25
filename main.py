from aiogram.utils import executor
from config import dp
from handlers import start, chat_actions, fsm_form
from database.sql_commands import Database


async def on_start_up(_):
    Database().sql_create_db()


start.register_start_handlers(dp=dp)
fsm_form.register_fsm_form_handlers(dp=dp)
chat_actions.register_chatt_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_start_up)
