import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')


class EDITH(discord.Client):
    async def on_ready(self):
        print("connected")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower() == "hello" or message.content.lower() == "hi" or message.content.lower() == "hey":
            await message.reply("Hi " + message.author.display_name, mention_author=True)

        if message.content.startswith("!rolladice"):
            num = random.randint(1, 6)
            await message.reply(num, mention_author=True)

        if message.content.startswith("!tossacoin"):
            num = random.randint(0, 1)
            if num == 0:
                await message.reply("H", mention_author=True)
            else:
                await message.reply("T", mention_author=True)

        if message.content.startswith("!delete"):
            await message.delete()

        if message.content.startswith("!pin"):
            await message.pin()


client = EDITH()

client.run(TOKEN)
