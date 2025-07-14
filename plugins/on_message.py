from pyrogram import Client, filters
from pyrogram.types import Message, KeyboardButton, ReplyKeyboardMarkup


@Client.on_message()
def on_message(client: Client, message: Message):
    message.reply_text("this message isn't in app and from on_message app",
                       reply_markup=ReplyKeyboardMarkup
                        ([
                           ["سلام test 1" , "asasasas"],
                       ],
                       resize_keyboard = True,
                       one_time_keyboard = False,))
