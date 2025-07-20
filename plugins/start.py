from pyrogram import Client, filters
from pyrogram.types import Message
import pyromod.listen


@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    answer = await client.ask(message.from_user.id, "send my your name:")
    await client.send_message(message.from_user.id, f"your name: {answer}")
