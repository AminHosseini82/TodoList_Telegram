from pyrogram import Client, filters
from pyrogram.types import Message
import pyromod.listen

plugins = dict(root="plugins")

app = Client(
    name="just-test",
    api_id="21980055",
    api_hash="4ec86b7ffa0214843ef9ba7ad4442ffc",
    bot_token="7711350201:AAFxdi3bpLtaCteWFb0KtD93BcFLIXEkXb8",
    plugins=plugins
)

print("ربات در حال اجرا است...")
app.run()
