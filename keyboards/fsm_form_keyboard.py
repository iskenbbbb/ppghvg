from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )

    markup.add(
        my_profile_button
    )
    return markup


async def new_start():
    markup = InlineKeyboardMarkup()
    signup_button = InlineKeyboardButton(
        "Регистрация",
        callback_data="signup"
    )

    markup.add(
        signup_button
    )
    return markup
