from pyrogram import Client, filters, enums
from pyrogram.types import Message
import pyromod.listen
    

@Client.on_message(filters.command("info"))
async def information_clinet(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    name_awnser = await client.ask(chat_id=message.from_user.id, text="Send my Your Name:")

    # try to find age is int or not
    age_flage = False
    while not age_flage:
        # Check if the input is a valid integer
        await message.reply_chat_action(enums.ChatAction.TYPING)
        age_awnser = await client.ask(chat_id=message.from_user.id, text="Send me Your age:")
        if age_awnser.text.isdigit():
            break
        else:
            await message.reply_text("Your age must be a number. Please try again.")

    await message.reply_text(f"Your age is {age_awnser.text} and your name is {name_awnser.text}")
