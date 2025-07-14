import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


# @Client.on_message()
# def on_message(client: Client, message: Message):
#     message.reply_text("این برنامه فقط برای بوس کردن فرزانه درست شده است😉",
#                        reply_markup=InlineKeyboardMarkup(
#                            [
#                                [InlineKeyboardButton(text = "فرزانه دلش 10 تا بوس آب دار میخواد؟😍" , callback_data = "amin hosseini222") , InlineKeyboardButton(text = "نکنه دلت نمیخواد؟😱" , callback_data = "ds hosseini")],
#                            ]
#                        ))
#
#
# @Client.on_callback_query(filters.regex("amin hosseini222"))
# def amin_hosseini(client: Client, callback_query: CallbackQuery):
#     print(callback_query)


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
