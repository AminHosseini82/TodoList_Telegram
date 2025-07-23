from pyrogram import filters, client, Client
from pyrogram.types import Message
from database.models import User, session
from plugins.login_check import login

@Client.on_message(filters.regex("نمایش لیست کار ها"))
async def todo_list(client: Client, message: Message):
    await login(client, message)
    await message.reply_text("hi this is todo_list")


