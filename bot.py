import os
import sys

import discord
from dotenv import load_dotenv

from features.message import message as msg

load_dotenv()

if os.getenv('TOKEN_FILE') is not None:
    with open(os.getenv('TOKEN_FILE'), 'r', encoding='utf-8') as file:
        TOKEN = file.read().strip()

elif os.getenv('TOKEN') is not None:
    TOKEN = os.getenv('TOKEN')

else:
    print("No token found")
    sys.exit(1)

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
