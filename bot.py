import discord
import os
from dotenv import load_dotenv
from features.message import message as msg

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print("connected")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await msg(message)


client.run(TOKEN)
