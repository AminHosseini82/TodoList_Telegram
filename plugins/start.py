from collections import defaultdict
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import json
import pyromod.listen
from pyrogram.types.bots_and_keyboards import callback_query


async def join_channels(client: Client, message: Message):
    channel_username = "amin_test_1"  # Better: Store in config
    try:
        member = await client.get_chat_member(channel_username, message.from_user.id)

        if member.status not in [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR
        ]:
            raise ValueError("Not a member")
    except Exception as e:
        keyboard_request = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{channel_username}")],
                [InlineKeyboardButton('Now I Joined! ✅', callback_data='join_channels')]  # ✅ Correct structure
            ]
        )
        await message.reply_text(
            "You must join the channel to use this bot.",
            reply_markup=keyboard_request
        )
        return False  # Explicitly return False to block the command
    return True  # Allow the command if the user is a member


join_filter = filters.create(join_channels)


# -------------------------------------------------------------------------------------------------------

def Tree():
    return defaultdict(Tree)


user_pocket = Tree()


# -----------------------------------------------------------------------------------------------------

@Client.on_callback_query()
async def callback_query_handler(client: Client, query: CallbackQuery):
    channel_username = "amin_test_1"
    try:
        member = await client.get_chat_member(channel_username, query.from_user.id)
        if member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            raise ValueError("Not a member")

        await query.answer("✅ Thanks for joining! You can now use the bot.", show_alert=True)
        await query.message.delete()
    except Exception as e:
        await query.answer("❌ You must join the channel first!", show_alert=True)


# -----------------------------------------------------------------------------------------------------
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


@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    # Check if the user has joined the channel
    is_member = await join_channels(client, message)

    if is_member:
        await message.reply_text("سلام نام خودت را وارد کنید.")
        user_pocket[message.from_user.id]["step"] = 1
