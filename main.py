import os
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

DISCORD_BOT_TOKEN='Nzg4NTQ3OTg4NjQ1MDg1MTk0.X9lGiw.5-IXfdCxC5xqNgCfrqYw0p8ilH8'
bot.run(DISCORD_BOT_TOKEN)

