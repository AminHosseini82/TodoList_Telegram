from pyrogram import Client, enums
from pyrogram.types import Message
from database.models import session, User


async def login(client: Client, message: Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    # query to get user in database
    existing_user = session.query(User).filter_by(user_id=user_id).first()

    # checking user is new or old one.
    if not existing_user:  # user is new
        new_user = User(user_id=user_id, firstname=user_first_name, lastname=user_last_name)
        # set a simple password for now
        # Todo: get user password from him.
        new_user.set_password("123456")
        # save in database
        session.add(new_user)
        session.commit()
        # Show successful login message.
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text("کاربر جدید ثبت شد!")
