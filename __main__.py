from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup

plugins = dict(root="plugins")

app = Client(
    name="just-test",
    api_id="21980055",
    api_hash="4ec86b7ffa0214843ef9ba7ad4442ffc",
    bot_token="7711350201:AAFxdi3bpLtaCteWFb0KtD93BcFLIXEkXb8",
    plugins=plugins
)

@Client.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text("سلام به ربات خوش آمدین!" , reply_markup=ReplyKeyboardMarkup(
        [
            ["hi"],
            ["bye"]
        ]
    ))
    message.reply_text(f"this is the message.id: {message.id}")

    # VIDEO_FILE_ID = "BAACAgQAAxkBAAICN2hr9wKvVb_10moR-qLMWGvUef9GAAI6GAACNzhhU6zK0mwOATCwHgQ"
    # await message.reply_video(
    #     video=VIDEO_FILE_ID,
    #     caption="خوش آمدید! این ویدیوی خوش‌آمدگویی است.",
    #     supports_streaming=True
    # )

print("ربات در حال اجرا است...")
app.run()






