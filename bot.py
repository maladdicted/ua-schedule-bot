import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Telegram bot token
TOKEN = getenv("BOT_TOKEN")

# Dispatcher for handling events
dp = Dispatcher()

# Inline keyboard
kb_list = [
  [KeyboardButton(text="Понеділок"), KeyboardButton(text="Вівторок")],
  [KeyboardButton(text="Середа"), KeyboardButton(text="Четвер")],
  [KeyboardButton(text="П'ятниця"), KeyboardButton(text="Субота")],
]

kb_markup = ReplyKeyboardMarkup(
  keyboard=kb_list,
  resize_keyboard=True,
  input_field_placeholder="Вибери день тижня 👇"
)

# Monday url inline buttons
mon_list = [[
  InlineKeyboardButton(text="1️⃣", url="https://meet.google.com/aeg-mkfg-wtb"),
  InlineKeyboardButton(text="2️⃣", url="https://meet.google.com/rog-fzcb-fjb"),
  InlineKeyboardButton(text="3️⃣", url="https://meet.google.com/yev-bqkk-zbo"),
  InlineKeyboardButton(text="4️⃣", url="https://meet.google.com/miw-bhyc-cuw"),
]]

mon_markup = InlineKeyboardMarkup(inline_keyboard=mon_list)

# Tuesday url inline buttons
tue_list = [[
  InlineKeyboardButton(text="🅰️", url="https://meet.google.com/ija-dpdx-yxo"),
  InlineKeyboardButton(text="2️⃣", url="https://meet.google.com/jkj-hufa-btb"),
  InlineKeyboardButton(text="3️⃣", url="https://meet.google.com/jkj-hufa-btb"),
  InlineKeyboardButton(text="4️⃣", url="https://meet.google.com/rog-fzcb-fjb"),
]]

tue_markup = InlineKeyboardMarkup(inline_keyboard=tue_list)

# Wednesday url inline buttons
wed_list = [[
  InlineKeyboardButton(text="1️⃣", url="https://meet.google.com/rdn-owjq-spf"),
  InlineKeyboardButton(text="2️⃣", url="https://meet.google.com/syi-gpek-nyf"),
  InlineKeyboardButton(text="3️⃣", url="https://meet.google.com/fnm-oibj-wrm"),
  InlineKeyboardButton(text="4️⃣", url="https://meet.google.com/ija-dpdx-yxo"),
]]

wed_markup = InlineKeyboardMarkup(inline_keyboard=wed_list)

# Thursday url inline buttons
thu_list = [[
  InlineKeyboardButton(text="1️⃣", url="https://meet.google.com/qys-rwbx-cch"),
  InlineKeyboardButton(text="🅰️", url="https://meet.google.com/fnm-oibj-wrm"),
  InlineKeyboardButton(text="🅱️", url="https://meet.google.com/jkj-hufa-btb"),
  InlineKeyboardButton(text="3️⃣", url="https://meet.google.com/bus-vxaa-mnk"),
  InlineKeyboardButton(text="4️⃣", url="https://meet.google.com/mpj-kneu-gxa"),
]]

thu_markup = InlineKeyboardMarkup(inline_keyboard=thu_list)

# Friday url inline buttons
fri_list = [[
  InlineKeyboardButton(text="2️⃣", url="https://meet.google.com/miw-bhyc-cuw"),
  InlineKeyboardButton(text="3️⃣", url="https://meet.google.com/oda-asnh-vtq"),
]]

fri_markup = InlineKeyboardMarkup(inline_keyboard=fri_list)

@dp.message(F.text, CommandStart())
async def start(msg: Message) -> None:
  """
  Start command handler
  
  This function handles the `/start` command &
  sends a welcome message with a keyboard to choose day of the week
  """
  await msg.answer(f"Привіт, <b>{msg.from_user.full_name}</b>! 👋", parse_mode="HTML")
  await msg.answer("Я підкажу розклад 🗓️", reply_markup=kb_markup)
  
@dp.message(F.text == "Понеділок")
async def monday(msg: Message) -> None:
  """
  Monday message handler

  This function handles the `Понеділок` message &
  sends a message with a schedule for Monday
  """
  await msg.reply(
    "1️⃣ Всесвітня історія\n"
    "🕣 08:30 – 09:30\n\n"
    "2️⃣ Українська література\n"
    "🕤 09:40 – 10:40\n\n"
    "3️⃣ Географія\n"
    "🕚 11:10 – 12:10\n\n"
    "4️⃣ Математика\n"
    "🕧 12:20 – 13:20",
    reply_markup=mon_markup,
  )

@dp.message(F.text == "Вівторок")
async def tuesday(msg: Message) -> None:
  """
  Tuesday message handler

  This function handles the `Вівторок` message &
  sends a message with a schedule for Tuesday
  """
  await msg.reply(
    "🅰️ Захист України\n"
    "🕣 08:30 – 09:30\n\n"
    "2️⃣ Історія України\n"
    "🕤 09:40 – 10:40\n\n"
    "3️⃣ Громадянська освіта\n"
    "🕚 11:10 – 12:10\n\n"
    "4️⃣ Українська мова\n"
    "🕧 12:20 – 13:20",
    reply_markup=tue_markup,
  )

@dp.message(F.text == "Середа")
async def wednesday(msg: Message) -> None:
  """
  Wednesday message handler
  
  This function handles the `Середа` message &
  sends a message with a schedule for Wednesday
  """
  await msg.reply(
    "1️⃣ Інформатика\n"
    "🕣 08:30 – 09:30\n\n"
    "2️⃣ Іноземна мова\n"
    "🕤 09:40 – 10:40\n\n"
    "3️⃣ Фізика та астрономія\n"
    "🕚 11:10 – 12:10\n\n"
    "4️⃣ Захист України\n"
    "🕧 12:20 – 13:20",
    reply_markup=wed_markup,
  )

@dp.message(F.text == "Четвер")
async def thursday(msg: Message) -> None:
  """
  Thursday message handler
  This function handles the `Четвер` message &
  sends a message with a schedule for Thursday
  """
  await msg.reply(
    "1️⃣ Філософія\n"
    "🕣 08:30 – 09:30\n\n"
    "🅰️ Фізика та астрономія\n"
    "🅱️ Громадянська освіта\n"
    "🕤 09:40 – 10:40\n\n"
    "3️⃣ Хімія\n"
    "🕚 11:10 – 12:10\n\n"
    "4️⃣ Правознавство\n"
    "🕧 12:20 – 13:20",
    reply_markup=thu_markup,
  )

@dp.message(F.text == "П'ятниця")
async def friday(msg: Message) -> None:
  """
  Friday message handler

  This function handles the `П'ятниця` message &
  sends a message with a schedule for Friday
  """
  await msg.reply(
    "1️⃣ Фізична культура\n"
    "🕣 08:30 – 09:30\n\n"
    "2️⃣ Математика\n"
    "🕤 09:40 – 10:40\n\n"
    "3️⃣ Біологія та екологія\n"
    "🕚 11:10 – 12:10",
    reply_markup=fri_markup,
  )

@dp.message(F.text == "Субота")
async def saturday(msg: Message) -> None:
  """
  Saturday message handler

  This function handles the `Субота` message &
  sends a message with a schedule for Saturday
  """
  await msg.reply("В розробці... 📝")

async def main() -> None:
  # Create bot instance
  bot = Bot(token=TOKEN)

  # Skip all incomings
  await bot.delete_webhook(drop_pending_updates=True)
  
  # Start polling for updates
  await dp.start_polling(bot)

if __name__ == "__main__":
  # Enables logging
  logging.basicConfig(level=logging.INFO, stream=sys.stdout)

  # Run the main function
  asyncio.run(main())
