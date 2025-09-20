from aiogram import types,F,Bot, Dispatcher,dispatcher,Router
# from main import dp
from aiogram_i18n.context import I18nContext
from aiogram.fsm.context import FSMContext
from task import select_task
from button import status_button,main_menu

my_plans_router = Router()

@my_plans_router.message(lambda message,i18n: message.text == i18n("my_tasks"))
async def my_task(message:types.Message,i18n:I18nContext,state:FSMContext):
    await message.answer(i18n("Plans"),reply_markup=status_button(i18n))
    
@my_plans_router.message(lambda message,i18n:message.text == i18n("pending"))
async def pending_tasks(message:types.Message,i18n:I18nContext):
    user_id = message.from_user.id
    tasks = select_task(user_id,"pending")
    if tasks:
        for task in tasks:
            text = f"""
            {i18n('description_text')}: {task[2]}
            {i18n('deadline_text')}: {task[3]}
            {i18n('notification_text')}: {task[4]}
            """
            await message.answer(text)
    else:
        await message.answer(i18n("no_tasks"))

@my_plans_router.message(lambda message,i18n:message.text == i18n("done"))
async def done_tasks(message:types.Message,i18n:I18nContext):
    user_id = message.from_user.id
    tasks = select_task(user_id,"done")
    if tasks:
        for task in tasks:
            text = f"""
            {i18n('description_text')}: {task[2]}
            {i18n('deadline_text')}: {task[3]}
            {i18n('notification_text')}: {task[4]}
            """
            await message.answer(text)
    else:
        await message.answer(i18n("no_tasks"))

@my_plans_router.message(lambda message,i18n:message.text == i18n("back"))
async def back_main(message:types.Message,i18n:I18nContext):
    await message.answer(i18n("start_text"),reply_markup=main_menu(i18n))