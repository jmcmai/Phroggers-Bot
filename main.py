import os
import discord
from discord.ext import commands
from settings import *

bot = commands.Bot(command_prefix='$')

for filename in os.listdir('./cogs'):
    print(filename)
    if filename.endswith(".py") and filename != "__init__.py":
            try:
                cog = "cogs.{}".format(filename.replace('.py', ''))
                bot.load_extension(cog)
            except Exception as e:
                print("{} Can not be loaded".format(filename))
                raise e
            else:
                print("{} has been succesfully Loaded.".format(filename))

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('phroggers! | $help'))

DISCORD_BOT_TOKEN = 'Nzg4NTQ3OTg4NjQ1MDg1MTk0.X9lGiw.4o2BPDzIQ0efH_LhjoxdkEssy_Y'  
bot.run(DISCORD_BOT_TOKEN)

