# from pyrogram import Client, filters, enums
# from pyrogram.types import Message, CallbackQuery
# from pyromod import listen
# from database.models import *
#
#
# @Client.on_callback_query()
# async def edit_todo(client: Client, callback_query, message: Message):
#     # When someone press Edit_todo
#     if callback_query.data == "Edit_todo":
#         # Get new data
#         user_id = message.from_user.id
#         new_title = await client.message.ask(user_id, "لطفا عنوان جدید خود را وارد بکنید.")
#         new_description = await client.message.ask(user_id, "حالا لطفا توضیحات جدید خودتون رو وارد بکنید.")
#
#         user_object = session.query(User).filter_by(user_id=user_id).first()
#         old_todo = session.query(Todo).filter_by(users = user_object).first()
#
#         if old_todo is None:
#             # Add old title and description to new one
#             old_todo.title = new_title.text
#             old_todo.description = new_description.text
#
#             # Add to database
#             session.add(old_todo)
#             session.commit()
#
#             # show successful message
#             await message.reply_text("تغییرات جدید title و description جدید شما ذخیره شد.")
#
#         else:
#             await message.reply_text("اصلا شما همجین Todo ای ندارین.")