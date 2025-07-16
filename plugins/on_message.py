from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.enums import ChatAction



@Client.on_message()
def on_message(client: Client, message: Message):
    message.reply_chat_action(action=ChatAction.TYPING)
    client.send_message(chat_id=7887229801, text=client.copy_message())


