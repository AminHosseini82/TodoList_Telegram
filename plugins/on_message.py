from pyrogram import Client, filters, enums
from pyrogram.types import Message
from db.new_db import User , session


@Client.on_message(filters.command("infoo"))
async def get_information(client:Client , message: Message):
    user_id  = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    existing_user = session.query(User).filter_by(user_id=user_id).first()
    # check user is save or not
    if existing_user is None:
        await message.reply_chat_action(action=enums.ChatAction.TYPING)
        password = await client.ask(message.chat.id,
                                    "اطلاعات فعلی شما در حال ثبت است، یک password برای حساب خودون انتخاب بکنید.")
        # saving data
        new_user = User(user_id = user_id , first_name = first_name, last_name = last_name)
        new_user.set_password(password.text)
        session.add(new_user)
        session.commit()
        await message.reply_text("اطلاعات شما ذخیره شد!")

    else:
        await message.reply_chat_action(action=enums.ChatAction.TYPING)
        await message.reply_text("خوش برگشتی!")








































# from pyrogram import Client, filters
# from pyrogram.types import Message
# from pyrogram.enums import ChatAction
# from db.new_db import User, session
#
#
# @Client.on_message(filters.command("infoo"))
# async def on_message(client: Client, message: Message):
#     user_id1 = message.from_user.id
#     user_first_name = message.from_user.first_name
#     user_last_name = message.from_user.last_name
#
#     existing_user = session.query(User).filter_by(user_id=user_id1).first()
#
#     if not existing_user:
#         new_user = User(user_id=user_id1, first_name=user_first_name, last_name=user_last_name)
#         session.add(new_user)
#         session.commit()
#         await message.reply_chat_action(ChatAction.TYPING)
#         reply_message = f"سلام اطلاعات شما در دیتابیس ذخیره {user_id1}"
#         await message.reply_text(reply_message)
#
#     else:
#         await message.reply_chat_action(ChatAction.TYPING)
#         reply_message = f"سلام خوش برگشتی کاربر {user_id1}"
#         await message.reply_text(reply_message)
