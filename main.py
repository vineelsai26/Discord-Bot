import discord
import os
from dotenv import load_dotenv
from threading import Thread
from server import run
from features.message import message as msg

load_dotenv()

TOKEN = os.getenv('TOKEN')


class Bot(discord.Client):
    async def on_ready(self):
        print("connected")

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            await msg(message)


client = Bot()


thread = Thread(target=run)
thread.start()

client.run(TOKEN)
