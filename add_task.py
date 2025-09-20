# from states import AddTasks
# from aiogram import Bot, Dispatcher, types,F,Router
# from middlewares.i18n import i18n_middleware
# from aiogram_i18n.context import I18nContext
# from aiogram.fsm.context import FSMContext


# add_router = Router()

# @add_router.message(lambda  message,i18n: message.text == i18n("add_task"))
# async def add_start(message:types.Message,i18n:I18nContext, state:FSMContext):
#     await message.answer(i18n("add_title"))
#     await state.set_state(AddTasks.title)


# @add_router.message(AddTasks.title)
# async def add_title(message:types.Message,state:FSMContext,i18n:I18nContext):
#     await state.update_data(title=message.text)
#     await message.answer(i18n("add_description"))
#     await state.set_state(AddTasks.description)


# @add_router.message(AddTasks.description)
# async def description(message:types.Message,state:FSMContext,i18n:I18nContext):
#     await state.update_data(description=message.text)
#     await message.answer(i18n("add_deadline"))
#     await state.set_state()