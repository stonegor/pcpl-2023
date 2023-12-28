from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters.command import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .cat_fact_service import CatFactService

router = Router()
catFactService = CatFactService()

main_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Give me a fact"), KeyboardButton(text="💥")]],
    resize_keyboard=True,
    input_field_placeholder="Choose an option from the menu",
)


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hewwo! pwease choose an option on your Keyboawd!!",
        reply_markup=main_kb,
    )


@router.message(F.text == "Give me a fact")
async def get_cat_fact(message: Message):
    await message.answer(catFactService.get_cat_fact())


@router.message(F.text == "💥")
async def get_cat_sticker(message: Message):
    await message.answer_sticker(
        "CAACAgIAAxkBAAELDqlljYOpmoIoaN7w36gBuOInF8EWIgACGhkAAje1KEj8SIqr6ZeTOTME"
    )
