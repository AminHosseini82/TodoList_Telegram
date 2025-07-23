from pyrogram import filters, client, Client
from pyrogram.types import Message
from database.models import User, session
from plugins.login_check import login

@Client.on_message(filters.command("test"))
async def todo_list_test(client: Client, message: Message):  # Show all user todolist
    # check login
    await login(client, message)

    user = session.query(User).filter_by(user_id = message.from_user.id).first()
    todos = user.todos
