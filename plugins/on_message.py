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





# @Client.on_callback_query()
# async def on_callback_query(client: Client, callback_query: CallbackQuery):
#     data = callback_query.data
#
#     if data == "amin hosseini":
#         await callback_query.message.reply_text("بوس 😘")
#         flag_am = True
#         for i in range(15):
#             if flag_am:
#                 await callback_query.message.reply_text("شروع بوس آب دار😘")
#                 flag_am = False
#             await callback_query.message.reply_text("بوس 😘")
#
#     elif data == "ds hosseini":
#         await callback_query.answer("خیال کردی میتونی در بری؟؟🤠😘")
#         flag_ds = True
#         for i in range(15):
#             if flag_ds:
#                 await callback_query.message.reply_text("دیگه بوس رو باید بشی نمیشه🤣")
#                 flag_ds = False
#             await callback_query.message.reply_text("بوس 😘")
