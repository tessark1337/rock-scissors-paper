from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)

b1 = KeyboardButton(text=LEXICON_RU['rock'])
b2 = KeyboardButton(text=LEXICON_RU['scissors'])
b3 = KeyboardButton(text=LEXICON_RU['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[b1], [b2], [b3]],
    resize_keyboard=True
)