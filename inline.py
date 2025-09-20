from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram_i18n import I18nContext


def alarm_inline() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✅', callback_data="yes"),
                InlineKeyboardButton(text='❌', callback_data="no"),
            ]
        ]
        
    )