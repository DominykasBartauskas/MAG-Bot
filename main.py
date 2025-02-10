import os

import discord
from dotenv import load_dotenv

# Load the Discord token from the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set Discord client
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


client.run(TOKEN)
