from environs import Env
from aiogram import Bot, Dispatcher, types,F,Router
import logging
from aiogram.types import Message
from aiogram.filters import Command,CommandStart
from environs import Env
import asyncio
from task import create_tables, insert_table,insert_user,update_task
from button import main_menu
from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from states import AddTasks
from language import language_router
from aiogram.fsm.context import FSMContext
from inline import alarm_inline
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from my_plans import my_plans_router
import re

env = Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

i18n_middleware.setup(dispatcher=dp)

async def send_reminder(user_id:int,task_id:int,description:str,i18n:I18nContext):
    try:
        await bot.send_message(user_id,f"{i18n('notification_time')}: {description}")
        update_task(task_id,"done")
    except Exception as e:
        print(f"Failed to send reminder to user {user_id}: {e}")




@dp.message(CommandStart())
async def cmd_start(message:Message,i18n:I18nContext):
    try:
        insert_user(message.from_user.id,message.from_user.username)
    except: 
        pass
    await  i18n.set_locale(message.from_user.language_code)
    await message.answer(i18n("start_text"),reply_markup=main_menu(i18n))

@dp.message(lambda  message,i18n: message.text == i18n("add_task"))
async def add_plan(message:Message,state:FSMContext,i18n:I18nContext):
    await message.answer(i18n("add_description"))
    await state.set_state(AddTasks.description)


@dp.message(AddTasks.description)
async def description_text(message:types.Message,state:FSMContext,i18n:I18nContext):
    await state.update_data(description_text=message.text)
    await message.answer(i18n("add_deadline"))
    await state.set_state(AddTasks.deadline)


@dp.message(AddTasks.deadline)
async def date(message:Message,state:FSMContext,i18n: I18nContext ):
    await state.update_data(date=message.text)
    await message.answer(i18n("notification"))
    await state.set_state(AddTasks.notify)

@dp.message(AddTasks.notify)
async def time(message:Message,state:FSMContext,i18n:I18nContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    text = f"""
                {i18n('checking')}
    {i18n('description_text')}: {data['description_text']}
    {i18n('deadline_text')}: {data['date']}
    {i18n('notification_text')}: {data['time']}
"""
    await message.answer(text,reply_markup=alarm_inline())
    await state.set_state(AddTasks.yes_or_no)


@dp.callback_query(F.data.in_(["yes", "no"]), AddTasks.yes_or_no)
async def user_decision(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if callback.data == "yes":
        description = data["description_text"]
        day = data.get("date")
        time = data.get("time")

        # если даты нет -> ставим сегодняшнюю
        # Проверяем, содержит ли дата только допустимые символы (цифры и "-")
        date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

        # Если дата пустая, некорректная или содержит буквы, используем текущую дату
        if not day or day.strip() == "" or not date_pattern.match(day):
            day = datetime.now().strftime("%Y-%m-%d")

        try:
            plan_dt = datetime.strptime(f"{day} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            await callback.message.answer("❌ Неправильный формат времени.")
            return

        task_id = insert_table(callback.from_user.id, description, day, time)

        scheduler.add_job(
            send_reminder,
            "date",
            run_date=plan_dt,
            args=[callback.from_user.id, task_id, description, i18n]
        )

        await callback.message.answer(i18n("task_added"))

    else:
        await callback.message.answer(i18n("task_deleted"))

    await callback.answer()
    await state.clear()


        
async def main():
    create_tables()
    dp.include_router(language_router)
    dp.include_router(my_plans_router)
    scheduler.start()
    await dp.start_polling(bot)








if __name__ == "__main__":
    asyncio.run(main())