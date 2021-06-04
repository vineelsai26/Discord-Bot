import discord
import os
from dotenv import load_dotenv
from threading import Thread
from server import run
from message import message as msg

load_dotenv()

TOKEN = os.getenv('TOKEN')


class EDITH(discord.Client):
    async def on_ready(self):
        print("connected")

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            await msg(message)


client = EDITH()


thread = Thread(target=run)
thread.start()

client.run(TOKEN)
