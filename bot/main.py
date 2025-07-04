from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

import modules.auth
import modules.upload
import modules.timer
import modules.folders
import modules.stats
import modules.support
import modules.panel

app = Client("media_cloud_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ثبت ماژول‌ها
modules.auth.register(app)
modules.upload.register(app)
modules.timer.register(app)
modules.folders.register(app)
modules.stats.register(app)
modules.support.register(app)
modules.panel.register(app)

print("🤖 ربات با موفقیت اجرا شد.")
app.run()
