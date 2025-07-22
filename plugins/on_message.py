from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from db.new_db import User, session


@Client.on_message(filters.command("infoo"))
async def on_message(client: Client, message: Message):
    user_id1 = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    existing_user = session.query(User).filter_by(user_id=user_id1).first()

    if not existing_user:
        new_user = User(user_id=user_id1, first_name=user_first_name, last_name=user_last_name)
        session.add(new_user)
        session.commit()
        await message.reply_chat_action(ChatAction.TYPING)
        reply_message = f"سلام اطلاعات شما در دیتابیس ذخیره {user_id1}"
        await message.reply_text(reply_message)

    else:
        await message.reply_chat_action(ChatAction.TYPING)
        reply_message = f"سلام خوش برگشتی کاربر {user_id1}"
        await message.reply_text(reply_message)
