from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums

@Client.on_message(filters.command(["start"]))
async def start_handler(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text("Hi world")
