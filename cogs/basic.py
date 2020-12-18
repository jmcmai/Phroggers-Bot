from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description="Returns 'pong'", brief="Returns 'pong'")
    async def ping(self, ctx):
        await ctx.send("Pong")
    
    @commands.command(description="Returns what the user says", brief="Returns arguments")
    async def say(self, ctx, *args):
        await ctx.send(' '.join(args))

def setup(bot):
    bot.add_cog(Basic(bot))