from pyrogram import Client, filters
from pyrogram.types import Message


# this is test on message
@Client.on_message(filters.regex("سلام"))
def amin_message(cilent , message: Message):
    message.reply_text(f"this is the message.id: {message.id}")
    message.reply_text(f"information about User:" )

