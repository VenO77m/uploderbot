from pyrogram import filters
from pyrogram.types import Message
import random
import string
import json
import os

uploads = {}  # برای حذف خودکار
shared_files = {}  # code → {file_id, type}

def generate_code(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def load_shared_files():
    if os.path.exists("shared_files.json"):
        with open("shared_files.json", "r") as f:
            return json.load(f)
    return {}

def save_shared_files():
    with open("shared_files.json", "w") as f:
        json.dump(shared_files, f)

shared_files.update(load_shared_files())

def register(app):

    @app.on_message(filters.private & filters.user("Pooyaspd") & (filters.document | filters.video | filters.audio | filters.photo))
    async def admin_upload(client, message: Message):
        file = message.document or message.video or message.audio or message.photo

        if message.document:
            file_type = "document"
        elif message.video:
            file_type = "video"
        elif message.audio:
            file_type = "audio"
        elif message.photo:
            file_type = "photo"
        else:
            await message.reply("❌ نوع فایل پشتیبانی نمی‌شود.")
            return

        file_id = file.file_id
        code = generate_code()
        shared_files[code] = {
            "file_id": file_id,
            "type": file_type
        }
        save_shared_files()

        bot_username = (await client.get_me()).username
        link = f"https://t.me/{bot_username}?start={code}"
        await message.reply(f"✅ فایل ذخیره شد.\n📎 لینک اشتراک:\n{link}")
