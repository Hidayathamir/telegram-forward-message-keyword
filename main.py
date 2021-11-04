import re
from typing import Set
from decouple import config
from telethon import TelegramClient
from telethon.events import NewMessage

api_id = config("api_id", cast=int)
api_hash = config("api_hash")
session = config("session", default="anon")
client: TelegramClient = TelegramClient(session, api_id, api_hash)
senders = [
    -1001192119485,
    -1001174862895,
    -1001060222929,
    -1001075783540,
]
receiver = -1001495000790

keywords = [
    "python",
    "backend",
    "junior",
    "developer",
]


def set_has_keyword(set_msg: Set[str]) -> bool:
    return any(keyword in set_msg for keyword in keywords)


def get_only_alpanumber(msg_text: str) -> str:
    return re.sub("[^0-9a-zA-Z ]", "", msg_text)


@client.on(NewMessage(incoming=True, chats=senders))
async def forward(event: NewMessage.Event) -> None:
    msg_text = event.message.text
    msg_text = get_only_alpanumber(msg_text)
    set_msg_text = set(msg_text.split())
    if set_has_keyword(set_msg_text):
        await client.send_message(receiver, event.message)


def main() -> None:
    print("running")
    client.start()
    client.run_until_disconnected()


if __name__ == "__main__":
    main()
