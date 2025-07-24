from pyrogram import filters, client, Client, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.models import User, session
from plugins.login_check import login

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

