from pyrogram import Client
from pyrogram.raw.types import message
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.enums import ChatAction



@Client.on_message()
def on_message(client: Client, message: Message):
    message.reply_chat_action(action=ChatAction.TYPING)
    if message.text == "خلیج عربی":
        client.send_message(chat_id=7887229801, text="خلیج فارس")
        message.reply_chat_action
    else:
        client.send_message(chat_id=7887229801, text=message.text)


