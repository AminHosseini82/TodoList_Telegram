# from pyrogram import Client, filters
# from pyrogram.types import Message
# from pyrogram.enums import ChatAction


# @Client.on_message(~filters.command("start") & filters.text)
# async def on_message(client: Client, message: Message):
#     await message.reply_chat_action(action=ChatAction.TYPING)
#     await message.reply_text(f"your message: {message.text}")
