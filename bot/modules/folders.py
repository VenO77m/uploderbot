from pyrogram import filters
from pyrogram.types import Message
from collections import defaultdict

user_folders = defaultdict(list)

def register(app):

    @app.on_message(filters.command("create_folder"))
    async def create_folder(client, message: Message):
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.reply("❗️نام پوشه را وارد کن:\n`/create_folder نام_پوشه`")
            return
        
        folder_name = args[1]
        user_id = message.from_user.id

        existing = [f["name"] for f in user_folders[user_id]]
        if folder_name in existing:
            await message.reply("⚠️ پوشه‌ای با این نام قبلاً ساختی!")
            return

        user_folders[user_id].append({"name": folder_name, "files": []})
        await message.reply(f"📁 پوشه `{folder_name}` ساخته شد.")

    @app.on_message(filters.command("list_folders"))
    async def list_folders(client, message: Message):
        folders = user_folders.get(message.from_user.id, [])
        if not folders:
            await message.reply("📂 هنوز هیچ پوشه‌ای نداری.")
            return
        text = "📁 پوشه‌های شما:\n" + "\n".join(f"- {f['name']}" for f in folders)
        await message.reply(text)
