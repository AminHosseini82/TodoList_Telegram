from collections import defaultdict
from pyrogram import Client, filters
from pyrogram.types import Message
import json
import pyromod.listen

def Tree():
    return defaultdict(Tree)

user_pocket = Tree()

@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text("سلام نام خودت را وارد کنید.")
    user_pocket[message.from_user.id]["step"]= 1  # userpocket = { "65165161" : {'step' = 1}}
    
    
@Client.on_message(filters.text)
async def message_handler(client: Client, message: Message):
    if user_pocket[message.from_user.id]['step'] == 1:
        # add to database
        with open ("db/users.json", "r+") as file:
            print(json.load(file))
        