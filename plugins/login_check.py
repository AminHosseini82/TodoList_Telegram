from pyrogram import Client, enums
from pyrogram.types import Message
from database.models import session, User
from pyromod import listen


async def login(client: Client, message: Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    # query to get user in database
    existing_user = session.query(User).filter_by(user_id=user_id).first()

    # checking user is new or old one.
    if not existing_user:  # user is new
        new_user = User(user_id=user_id, firstname=user_first_name, lastname=user_last_name)
        # # Get User password
        # password = (await client.ask(user_id, "لطفا یک رمز برای حساب خود در نظر بگیرن:")).text
        # new_user.set_password(password)
        session.add(new_user)
        session.commit()
        # Show successful login message.
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text("کاربر جدید ثبت شد!")
    else:
        return
