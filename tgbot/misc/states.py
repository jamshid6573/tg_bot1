from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMuz(StatesGroup):
    gold = State()

class FSMrus(StatesGroup):
    gold = State()

class FSMsom(StatesGroup):
    som = State()

class FSMsomRU(StatesGroup):
    som = State()