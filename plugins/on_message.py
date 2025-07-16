from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatAction
import pyromod.listen


@Client.on_message()
async def on_message(client: Client, message: Message):
    await message.reply_chat_action(action=ChatAction.TYPING)
    await message.reply_text(f"your message: {message.text}")
