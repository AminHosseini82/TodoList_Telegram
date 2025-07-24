from pyrogram import Client, filters, enums
from pyrogram.types import Message
from plugins.login_check import login
from pyromod import listen
from database.models import *


@Client.on_message(filters.regex("اضافه کردن کار جدید"))
async def create_todo(client: Client, message: Message, messaeg=None):
    # check login
    await login(client, message)
    user_id = message.from_user.id

    # Ask title and descriptions for a TodoWork
    await message.reply_chat_action(enums.ChatAction.TYPING)
    title = await client.ask(user_id, "لطفا عنوان کاری رو وارد بکن.")
    await message.reply_chat_action(enums.ChatAction.TYPING)
    descriptions = await client.ask(user_id, "لطفا توضیحاتی برای کار خودتون وارد بکنید.")

    # Add TodoWork and save it in database.
    new_todo = Todo(title=title.text, description=descriptions.text, user_id=user_id)
    session.add(new_todo)
    session.commit()

    # Show successful message.
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text("Todo شما ثبت شد")




