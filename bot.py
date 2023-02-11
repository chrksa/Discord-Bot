#bot.py 
import os
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path='/home/chris/DiscordBot/.env')

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord! WUHU')

client.run(TOKEN)
