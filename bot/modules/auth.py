from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import FORCED_CHANNELS, WELCOME_TEXT
from modules.upload import shared_files, uploads

def register(app):

    async def check_membership(client, user_id):
        for channel in FORCED_CHANNELS:
            try:
                member = await client.get_chat_member(channel, user_id)
                if member.status in ["kicked", "left"]:
                    return False
            except:
                return False
        return True

    @app.on_message(filters.private & filters.command("start"))
    async def start(client, message: Message):
        args = message.text.split(maxsplit=1)
        user_id = message.from_user.id

        is_member = await check_membership(client, user_id)
        if not is_member:
            buttons = [
                [InlineKeyboardButton("📢 عضویت در " + ch, url=f"https://t.me/{ch}")]
                for ch in FORCED_CHANNELS
            ]
            buttons.append([InlineKeyboardButton("🔁 بررسی عضویت", callback_data="check_again")])
            await message.reply(
                "📛 برای استفاده از ربات، لطفاً ابتدا در کانال‌ها عضو شو:",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

        if len(args) > 1:
            code = args[1]
            if code in shared_files:
                file_info = shared_files[code]
                file_id = file_info["file_id"]
                file_type = file_info["type"]

                if file_type == "document":
                    sent = await message.reply_document(file_id)
                elif file_type == "video":
                    sent = await message.reply_video(file_id)
                elif file_type == "audio":
                    sent = await message.reply_audio(file_id)
                elif file_type == "photo":
                    sent = await message.reply_photo(file_id)
                else:
                    await message.reply("❌ نوع فایل پشتیبانی نمی‌شود.")
                    return

                uploads[file_id] = {
                    "chat_id": sent.chat.id,
                    "msg_id": sent.id
                }
                return

        await message.reply(f"👋 {WELCOME_TEXT}")

    @app.on_callback_query(filters.regex("check_again"))
    async def check_again_callback(client, callback):
        is_member = await check_membership(client, callback.from_user.id)
        if is_member:
            await callback.message.edit("✅ عضویت تأیید شد! حالا می‌تونی از ربات استفاده کنی.")
        else:
            await callback.answer("❌ هنوز عضو همه کانال‌ها نشدی!", show_alert=True)
