from aiogram.fsm.state import State, StatesGroup

class AddTasks(StatesGroup):
    title = State()
    description = State()
    deadline = State()
    notify = State()
    yes_or_no = State()