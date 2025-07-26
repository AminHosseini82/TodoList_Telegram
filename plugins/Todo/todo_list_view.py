from pyrogram import filters, client, Client, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.models import User, session, Todo
from plugins.login_check import login
from pyromod import listen


@Client.on_message(filters.regex("نمایش لیست کار ها"))
async def todo_list(client: Client, message: Message):  # Show all user todolist
    # Check login
    await login(client, message)
    user_id = message.from_user.id

    user = session.query(User).filter_by(user_id=user_id).first()
    todos = user.todos

    # If there is no todos
    if todos is None:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text("شما todo ای ثبت نداری")

    # If todos finds
    else:
        text = "لیست کارهای شما:"
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply_text(text)

        for todo in todos:
            await message.reply_chat_action(enums.ChatAction.TYPING)
            await message.reply_text(todo, reply_markup=InlineKeyboardMarkup(
                [
                    [  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            "ویرایش",
                            callback_data="Edit_todo"
                        ),
                        InlineKeyboardButton(  # Opens a web URL
                            "حذف",
                            callback_data="Delete_todo"
                        ),
                    ],
                ]
            ))


@Client.on_callback_query()
async def edit_todo(client: Client, callback_query):
    # When someone press Edit_todo
    if callback_query.data == "Edit_todo":
        # Get new data
        user_id = callback_query.from_user.id

        user_object = session.query(User).filter_by(user_id=user_id).first()
        old_todo = session.query(Todo).filter_by(users=user_object).first()

        if old_todo:
            # Ask for new title and new description
            new_title = await client.ask(user_id, "لطفا عنوان جدید خود را وارد بکنید.")
            new_description = await client.ask(user_id, "حالا لطفا توضیحات جدید خودتون رو وارد بکنید.")

            # Add old title and description to new one
            old_todo.title = new_title.text
            old_todo.description = new_description.text

            # Add to database
            session.add(old_todo)
            session.commit()

            # show successful message
            await callback_query.message.reply_text("تغییرات جدید title و description جدید شما ذخیره شد.")

        else:
            await callback_query.message.reply_text("اصلا شما همجین Todo ای ندارین.")
