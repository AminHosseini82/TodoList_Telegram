from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup
from pyrogram import Client, filters, enums
from plugins.login_check import login


@Client.on_message(filters.command(["start"]))
async def start_handler(client: Client, message: Message):
    # if he didn't start the bot, bot shows login successful message.
    await login(client, message)
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text("خوش اومدی!")

    # Show a button to see all work
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text("میخوای چی کار بکنی؟", reply_markup=ReplyKeyboardMarkup(
        [
            ["نمایش لیست کار ها"],
            ["اضافه کردن کار جدید"],
        ]
    ))


@Client.on_message(filters.text)
async def text_handler(client: Client, message: Message):
    # if he didn't start the bot, bot shows login successful message.
    await login(client, message)

    # Show a button to see all work
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text("میخوای چی کار بکنی؟", reply_markup=ReplyKeyboardMarkup(
        [
            ["نمایش لیست کار ها"],
            ["اضافه کردن کار جدید"],
        ]
    ))
