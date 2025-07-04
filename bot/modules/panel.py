from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_USERNAME

admins = [OWNER_USERNAME]
panel_config = {
    "support_enabled": True,
    "welcome_text": "سلام دانش‌آموز گلم خوش آمدی 💚"
}

def register(app):

    @app.on_message(filters.command("set_welcome") & filters.user(admins))
    async def set_welcome(client, message: Message):
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.reply("❗️ لطفاً متن خوش‌آمد را وارد کن:\n`/set_welcome متن خوش‌آمد`")
            return
        panel_config["welcome_text"] = args[1]
        await message.reply("✅ پیام خوش‌آمد به‌روزرسانی شد.")

    @app.on_message(filters.command("toggle_support") & filters.user(admins))
    async def toggle_support(client, message: Message):
        current = panel_config.get("support_enabled", True)
        panel_config["support_enabled"] = not current
        status = "فعال" if not current else "غیرفعال"
        await message.reply(f"⚙️ بخش پشتیبانی اکنون `{status}` است.")

    @app.on_message(filters.command("add_admin") & filters.user(admins))
    async def add_admin(client, message: Message):
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.reply("❗️ استفاده صحیح: `/add_admin username`")
            return
        new_admin = args[1].lstrip("@")
        if new_admin in admins:
            await message.reply("⚠️ این کاربر قبلاً ادمین است.")
            return
        admins.append(new_admin)
        await message.reply(f"✅ @{new_admin} به لیست ادمین‌ها اضافه شد.")
