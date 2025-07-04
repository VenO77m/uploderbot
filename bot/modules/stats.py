from pyrogram import filters
from pyrogram.types import Message

# نمونه داده ساختگی (می‌تونه بعداً از دیتابیس خونده شه)
popular_files = [
    "🎞 کلیپ انگیزشی",
    "📄 جزوه جمع‌بندی دینی",
    "🧠 فایل صوتی روان‌شناسی"
]

newest_files = [
    "📚 فایل تازه بارگذاری‌شده ۱",
    "🎧 ضبط جدید زبان",
    "📸 تمرین تصویری"
]

def register(app):

    @app.on_message(filters.command("popular"))
    async def show_popular(client, message: Message):
        text = "🔥 پربازدیدترین فایل‌ها:\n\n" + "\n".join(popular_files)
        await message.reply(text)

    @app.on_message(filters.command("newest"))
    async def show_newest(client, message: Message):
        text = "🆕 جدیدترین فایل‌ها:\n\n" + "\n".join(newest_files)
        await message.reply(text)
