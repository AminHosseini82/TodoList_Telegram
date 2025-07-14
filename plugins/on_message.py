from pyrogram import Client, filters
from pyrogram.types import Message, KeyboardButton, ReplyKeyboardMarkup


@Client.on_message()
def on_message(client: Client, message: Message):
    message.reply_text("this message isn't in app and from on_message app",
                       reply_markup=ReplyKeyboardMarkup(
                           [
                               [
                                   "ammin" , "kskskksks"
                               ],
                               ["far"],
                               [
                                   "asdasdasd", "asdasdasdasd"
                               ]
                           ]
                       ))
