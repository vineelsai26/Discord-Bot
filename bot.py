import discord
import os
from dotenv import load_dotenv
from features.message import message as msg

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("connected")


@client.event
async def on_message(message):
    if message.author != client.user:
        await msg(message)


client.run(TOKEN)
