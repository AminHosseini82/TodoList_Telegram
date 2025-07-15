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


@Client.on_callback_query()
def text_reply(client: Client, callback_query: CallbackQuery):
    if callback_query.data == "bottem 1":
        callback_query.message.reply_chat_action(action=ChatAction.TYPING)
        callback_query.message.reply_text(
        f"""
        this is the text and from bottem 1
        this is all your information {callback_query}
        """)
        callback_query.answer("🖕")
    else:
        callback_query.message.reply_chat_action(ChatAction.TYPING)
        callback_query.message.reply_text(
        f"""
        this is the text and from bottem 2
        this is the id of message{callback_query.message.id}
        this is the user id {callback_query.message.from_user.id}
        """)
        client.delete_messages(chat_id=callback_query.message.chat.id, message_ids=callback_query.message.id)

        callback_query.answer("🖕")

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
