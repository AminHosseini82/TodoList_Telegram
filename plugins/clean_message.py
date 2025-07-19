from pyrogram import Client, filters, enums
from pyrogram.types import Message

@Client.on_message(filters.command("clean"))
async def clean_messages(client: Client, message:Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text(
        "این یک پیام موقت است! بعد از چند ثانیه ناپدید می‌شود.",
    )
    # Get all messages in the chat and delete them one by one
    async for msg in client.get_chat_history("me"):
        await client.delete_messages(chat_id="me", message_ids=msg.id)