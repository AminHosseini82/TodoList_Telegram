from pyrogram import Client, filters
from pyrogram.types import Message
import pyromod.listen


@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    answer = await client.ask(message.from_user.id, "send my your name:")
    await client.send_message(message.from_user.id, f"your name: {answer}")


# # this is test on message
# @Client.on_message(filters.regex("سلام"))
# async def amin_message(cilent, message: Message):
#     await message.reply_text(f"this is the message.id: {message.id}")
#     await message.reply_text(f"information about User: {message}")


# @Client.on_message(filters.command('form'))
# async def on_form(client: Client, message: Message):
#     response = await client.listen(chat_id=message.from_user.id)
#     await message.reply_text(response.text)