import requests

from config import settings


def send_telegram_message(chat_id, text):
    params = {
        "text": text,
        "chat_id": chat_id,
    }
    requests.get(
        f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage", params=params
    )
