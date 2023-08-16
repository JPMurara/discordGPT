import os

import disnake
from dotenv import load_dotenv

from bot import Bot

"""
We set the intents to ensure only we can dictate the bot. We only really want to listen
to the events required
"""
intents = disnake.Intents.default()
intents.members = True

bot = Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if __name__ == "__main__":
    bot.load_extensions("./cogs")
    bot.run(BOT_TOKEN) 