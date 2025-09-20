from aiogram import Bot, Dispatcher, types,F,Router
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext
from  button import main_menu,language_menu

language_router = Router()

@language_router.message(lambda message,i18n: message.text ==i18n("language"))
async def language_button(message:types.Message,i18n:I18nContext):
    await message.answer(i18n("lang"),reply_markup=language_menu(i18n))



@language_router.message(lambda message,i18n:message.text ==i18n("Uzbek"))
async def uz_l(message:types.Message,i18n:I18nContext):
     await i18n.set_locale("uz")
     await message.answer(i18n("language_changed"),reply_markup=main_menu(i18n))

@language_router.message(lambda message,i18n:message.text == i18n("Russia"))
async def ru_l(message:types.Message,i18n:I18nContext):
     await i18n.set_locale("ru")
     await message.answer(i18n("language_changed"),reply_markup=main_menu(i18n))


@language_router.message(lambda message,i18n:message.text == i18n("English"))
async def en_l(message:types.Message,i18n:I18nContext):
     await i18n.set_locale("en")
     await message.answer(i18n("language_changed"),reply_markup=main_menu(i18n))

@language_router.message(lambda message,i18n:message.text == i18n("back"))
async def back_main(message:types.Message,i18n:I18nContext):
    await message.answer(i18n("start_text"),reply_markup=main_menu(i18n))