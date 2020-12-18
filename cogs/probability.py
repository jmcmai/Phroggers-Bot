from discord.ext import commands
import random

class Probability(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description="Returns a random number given number of faces",
                        brief="Rolls a die with input faces")
    async def roll(self, ctx, faces=6):
        num_faces = int(faces)
        n = random.randrange(1, num_faces)
        await ctx.send(n)
    
    @commands.command(description="Flips a coin", brief="Simulates coin flip")
    async def flip(self, ctx):
        face = random.randrange(0,2)
        await ctx.send('heads' if face == 0 else 'tails')

def setup(bot):
    bot.add_cog(Probability(bot))