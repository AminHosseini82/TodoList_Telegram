from collections import defaultdict
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import json
import pyromod.listen

async def join_channels   (client: Client, message: Message):
    try:
        member = await client.get_chat_member("amin_test_1", "me")

        if member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            raise Exception("Not a member")
    except:
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join in Channel📢", url="amin_test_1")]]
        )
        await message.reply_text(
            "You must join in channel to use the bot",
            reply_markup=keyboard
        )
        return

join_filter = filters.create(join_channels)

def Tree():
    return defaultdict(Tree)


user_pocket = Tree()


@Client.on_message(filters.text & ~filters.command('start'))
async def message_handler(client: Client, message: Message):
    if user_pocket[message.from_user.id]['step'] == 1:
        # add to database
        with open("db/users.json", "r+") as file:
            user_db = json.load(file)  # convert json to dic
            user_db[message.from_user.id] = message.text
            file.seek(0)
            json.dump(user_db, file, indent=4)

        await message.reply_text("your info save in database")


@Client.on_message(filters.command("start"),filters.command("join_filter"))
async def start_handler(client: Client, message: Message):
    await message.reply_text("سلام نام خودت را وارد کنید.")
    user_pocket[message.from_user.id]["step"] = 1  # userpocket = { "65165161" : {'step' = 1}}
