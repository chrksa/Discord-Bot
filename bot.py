#bot.py 
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path='/home/chris/DiscordBot/.env')
# loads .env with following variables 

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
        for guild in client.guilds:
                print (guild.name)
                if int(guild.id) == int(GUILD):
                        print(f'{guild.name} is in client.guilds')
                        break

        
        print(f'{client.user} has connected to Discord! WUHU')
        print(f'{client.user} is connected to {guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

@client.command()
async def topG(ctx):
        print('not finished yet')

#@client.command()
 
        

client.run(TOKEN)
