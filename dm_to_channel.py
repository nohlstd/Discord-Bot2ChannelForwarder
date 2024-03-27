import discord
from discord.ext import commands

# Replace 'your_token_here' with your bot's token
TOKEN = 'BOT TOKEN HERE'

# Replace 'your_channel_id_here' with the ID of the channel you want to forward messages to
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

bot.run(TOKEN)
