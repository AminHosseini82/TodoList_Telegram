from pyrogram import filters, client, Client
from pyrogram.types import Message
from database.models import User, session
from plugins.login_check import login

@Client.on_message(filters.command("test"))
async def todo_list_test(client: Client, message: Message):  # Show all user todolist
    # check login
    await login(client, message)
    user_id = message.from_user.id

    user = session.query(User).filter_by(user_id = user_id).first()
    print(f"this is {user.todos()}")
    await message.reply_text("this this todo list")


