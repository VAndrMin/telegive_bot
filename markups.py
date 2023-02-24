from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNELS

btnProfile = KeyboardButton('Profile')
profilekeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(btnProfile)

def showChannels():
    keyboard = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[1])
        keyboard.insert(btn)

    btnDoneSub = InlineKeyboardButton(text="Я підписався", callback_data="subchanneldone")
    keyboard.insert(btnDoneSub)
    return keyboard