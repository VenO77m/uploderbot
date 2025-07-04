from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_USERNAME, WELCOME_TEXT
from modules.panel import panel_config

def register(app):

    @app.on_message(filters.command("support"))
    async def send_support(client, message: Message):
        user = message.from_user
        args = message.text.split(maxsplit=1)
        
        if not panel_config.get("support_enabled", True):
            await message.reply("❌ بخش پشتیبانی در حال حاضر غیرفعال است.")
            return

        if len(args) < 2:
            await message.reply("📝 لطفاً پیام خود را وارد کن:\n`/support مشکل من اینه...`")
            return

        support_text = args[1]
        support_msg = (
            f"📩 پیام پشتیبانی جدید:\n"
            f"👤 کاربر: @{user.username or user.id}\n\n"
            f"{support_text}"
        )

        try:
            await client.send_message(OWNER_USERNAME, support_msg)
            await message.reply("✅ پیام شما برای ادمین ارسال شد.")
        except:
            await message.reply("❗️متأسفم، مشکلی در ارسال پیام به مدیر پیش اومد.")
