from pyrogram import filters, client, Client
from pyrogram.types import Message
from database.models import User, session
from plugins.login_check import login

@Client.on_message(filters.regex("نمایش لیست کار ها"))
async def todo_list(client: Client, message: Message):  # Show all user todolist
    # check login
    await login(client, message)
    user_id = message.from_user.id

    user = session.query(User).filter_by(user_id=user_id).first()
    todos = user.todos

    if not todos:
        await message.reply_text("شما todo ای ثبت نداری")

