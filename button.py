from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram_i18n.context import I18nContext

def main_menu (i18n:I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(text=_("my_tasks")),
                KeyboardButton(text=_("add_task"))
            ],
            [
                KeyboardButton(text=_("language"))

            ]
         


        ],
        resize_keyboard=True




    )

def language_menu (i18n:I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard = [

            [
                KeyboardButton(text=_("Uzbek")),
                KeyboardButton(text=_("Russia"))
            ],   

            [
                KeyboardButton(text=_("English")),
                KeyboardButton(text=_("back"))

            ]



        ],
        resize_keyboard=True
    )



def status_button(i18n:I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(text=_("pending")),
                KeyboardButton(text=_("done"))
            ],[

                KeyboardButton(text=_("back"))
            ]


        ],resize_keyboard=True
    )