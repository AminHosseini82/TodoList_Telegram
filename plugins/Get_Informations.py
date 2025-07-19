from pyrogram import Client, filters, enums
from pyrogram.types import Message
import pyromod.listen
    

# @Client.on_message(filters.command("info"))
# async def information_clinet(client: Client, message: Message):
#     await message.reply_chat_action(enums.ChatAction.TYPING)
#     name_awnser = await client.ask(chat_id=message.from_user.id, text="Send my Your Name:")

#     # try to find age is int or not
#     age_flage = False
#     while not age_flage:
#         # Check if the input is a valid integer
#         await message.reply_chat_action(enums.ChatAction.TYPING)
#         age_awnser = await client.ask(chat_id=message.from_user.id, text="Send me Your age:")
#         if age_awnser.text.isdigit():
#             break
#         else:
#             await message.reply_text("Your age must be a number. Please try again.")

#     await message.reply_text(f"Your age is {age_awnser.text} and your name is {name_awnser.text}")


@Client.on_message(filters.command("info"))
async def get_information(client:Client , message: Message):
    await message.reply_chat_action(action=enums.ChatAction.TYPING)
    client_name = await client.ask(chat_id = message.from_user.id, text= "Send me your name:")
    
    # find this is a number or not
    while True:
        await message.reply_chat_action(action=enums.ChatAction.TYPING)
        client_age =await client.ask(chat_id = message.from_user.id, text= "Send me your age:")
        
        if client_age.text.isdigit():
            break
        else:
            await message.reply_text("Your age must be a number. Please try again.")
            client_age =await client.ask(chat_id = message.from_user.id, text= "Send me your age:")

    await message.reply_text(f"your age is {client_age.text} and your name is {client_name.text}")
    