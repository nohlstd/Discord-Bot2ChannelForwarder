import discord
from discord.ext import commands
import datetime

TOKEN = 'TOKEN HERE'
CHANNEL_ID = Channel ID Here

intents = discord.Intents.default()
intents.messages = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        channel = bot.get_channel(CHANNEL_ID)        
        await channel.send(message.content)

    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message.author.name}: {message.content}\n")

    await bot.process_commands(message)

bot.run(TOKEN)
