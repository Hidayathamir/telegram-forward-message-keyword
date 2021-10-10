import json

from decouple import config
from telethon import TelegramClient


async def get_dialogs() -> None:
    dialogs = {}
    async for dialog in client.iter_dialogs():
        dialogs[dialog.id] = dialog.name
    with open("dialogs.json", "w", encoding="utf-8") as f:
        json.dump(dialogs, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Remember to use your own values from my.telegram.org!
    api_id = config("api_id", cast=int)
    api_hash = config("api_hash")
    session = config("session", default="anon")
    client = TelegramClient(session, api_id, api_hash)

    with client:
        client.loop.run_until_complete(get_dialogs())
