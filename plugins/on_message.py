from tkinter.font import names

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message()
def on_message(client: Client, message: Message):
    message.reply_text("this message isn't in app and from on_message app",
                       reply_markup=InlineKeyboardMarkup(
                           [
                               [InlineKeyboardButton(text = "amin" , callback_data = "amin hosseini") , InlineKeyboardButton(text = "da" , callback_data = "ds hosseini")],
                               [InlineKeyboardButton(text = "fa" , callback_data = "aminss hosseini")],
                           ]
                       ))