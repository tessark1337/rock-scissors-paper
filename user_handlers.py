from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards import game_kb, yes_no_kb
from services import get_bot_choice, get_winner
from lexicon import LEXICON_RU

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

@router.message(F.text == LEXICON_RU['yes_button'])
async def yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

@router.message(F.text == LEXICON_RU['no_button'])
async def no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])

@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]}  '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)

