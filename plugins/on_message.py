from pyrogram import Client
from pyrogram.raw.types import message
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.enums import ChatAction



@Client.on_message()
def on_message(client: Client, message: Message):
    message.reply_text(f"this is your message {message.text}",
                       reply_markup=InlineKeyboardMarkup(
                           [
                               [InlineKeyboardButton(text = "key1" , callback_data = "bottem 1") , InlineKeyboardButton(text = "key2" , callback_data = "bottem 2")],
                           ]
                       ))



