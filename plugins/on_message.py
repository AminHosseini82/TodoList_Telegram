import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Client.on_message()
def on_message(client: Client , message: Message):
    if message.text == "shrek":
        message.reply_photo("https://i.ytimg.com/vi/7Bzbckc1IUI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAocaVIIoden2ZUcot7y5sMKz2OdQ",
                            caption="l love shrek")
    else:
        message.reply_text("your massage is not good",reply_markup= InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="shrek", callback_data="shrek")]
            ]
        ))
    #
    # message.reply_photo("https://i.ytimg.com/vi/7Bzbckc1IUI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAocaVIIoden2ZUcot7y5sMKz2OdQ",
    #                     caption="i love sherek")


@Client.on_callback_query()
def shrek(client: Client ,callback_query: CallbackQuery):
    data = callback_query.data

    if data == "shrek":
        callback_query.message.reply_photo(
            "https://i.ytimg.com/vi/7Bzbckc1IUI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAocaVIIoden2ZUcot7y5sMKz2OdQ",
            caption="l love shrek")

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
