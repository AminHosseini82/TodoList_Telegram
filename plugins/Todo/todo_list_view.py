from pyrogram import filters, client, Client, enums
from pyrogram.types import Message
from database.models import User, session
from plugins.login_check import login

@Client.on_message(filters.regex("نمایش لیست کار ها"))
async def todo_list(client: Client, message: Message):  # Show all user todolist
    # Check login
    await login(client, message)
    user_id = message.from_user.id

    user = session.query(User).filter_by(user_id=user_id).first()
    todos = user.todos

    if todos is None:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text("شما todo ای ثبت نداری")

    else:
        await message.reply_text("یک TODO وجود دارد.")

