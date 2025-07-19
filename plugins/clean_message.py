import asyncio

from pyrogram import Client, filters, enums
from pyrogram.types import Message

# @Client.on_message(filters.command("clean"))
# async def clean_messages(client: Client, message:Message):
#     await message.reply_chat_action(enums.ChatAction.TYPING)
#     await message.reply_text(
#         "این یک پیام موقت است! بعد از چند ثانیه ناپدید می‌شود.",
#     )
#     # Get all messages in the chat and delete them one by one
#     async for msg in client.get_chat_history("me"):
#         await client.delete_messages(chat_id="me", message_ids=msg.id)


@Client.on_message(filters.command('clean'))
async def clean_history(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text("all message will delete in 3 seconds")
    # 3 seconds wait
    await asyncio.sleep(3)
    # deleted all message in chat.
    async  for mes in client.get_chat_history("me"):
        # await message.reply_chat_action(enums.ChatAction.TYPING)
        await client.delete_messages("me", message_ids=mes.id)

