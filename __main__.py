import os
from pyrogram import Client, filters
from pyrogram.types import Message
import pyromod.listen

plugins = dict(root="plugins")

# BOT_TOKEN = os.environ.get("BOT_TOKEN", "7711350201:AAFxdi3bpLtaCteWFb0KtD93BcFLIXEkXb8")
APP_ID = os.environ.get("APP_ID", "21980055")
API_HASH = os.environ.get("API_HASH", "4ec86b7ffa0214843ef9ba7ad4442ffc")

app = Client(
    name="self bot",
    api_id=APP_ID,
    api_hash=API_HASH,
    # bot_token=BOT_TOKEN,
    plugins=plugins
)

print("ربات در حال اجرا است...")
app.run()
