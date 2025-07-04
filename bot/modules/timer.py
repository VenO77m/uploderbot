from apscheduler.schedulers.background import BackgroundScheduler
from pyrogram.errors import MessageDeleteForbidden
from modules.upload import uploads
from config import FILE_LIFETIME_SECONDS

scheduler = BackgroundScheduler()

def register(app):

    def delete_expired_messages():
        to_delete = list(uploads.items())
        for file_id, data in to_delete:
            try:
                app.delete_messages(data["chat_id"], data["msg_id"])
            except MessageDeleteForbidden:
                pass
            except:
                continue
            del uploads[file_id]

    scheduler.add_job(delete_expired_messages, "interval", seconds=FILE_LIFETIME_SECONDS)
    scheduler.start()
