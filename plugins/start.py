from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from database.models import User, session


@Client.on_message(filters.command(["start"]))
async def start_handler(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    # await message.reply_text("Hi world")
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    # exsisting_user = session.query(User).filter(User.id == user_id).first()
    existing_user = session.query(User).filter_by(user_id = user_id).first()

    # checking user is new or old one.
    if not existing_user:  # user is new
        new_user = User(user_id = user_id, firstname=user_first_name, lastname=user_last_name)
        new_user.set_password("123456")
        session.add(new_user)
        session.commit()
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text("کاربر جدید ثبت شد!")

    else:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text("خوش اومدی!")






