import botpy
from botpy.types.message import Message

appid = "102092294"
token = "ISulT691dyqyFzu5X85IGaXcwIGvyKB8"
appSecret = "qWCtaHyfM3lTBtbJ1jSBudM5oYI2mWG0"


class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        # print(message)
        await self.api.post_message(channel_id=message.channel_id, content="message")


def run():
    print("start run")
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid, appSecret)
