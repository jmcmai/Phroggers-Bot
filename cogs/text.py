import aiohttp
import discord
from discord.ext import commands
from utils import get_agent, text_to_owo, get_frog_facts, get_8ball_answer, get_sad_face

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Change depending on error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        print(e)
        await ctx.send("Check command with $help.")

    @commands.command(description='Changes all text to owo-text', 
                        brief='Changes text to owo-text')
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content)[4:])

    @commands.command(description='Returns a random joke', brief="Returns a random joke")
    async def dadjoke(self, ctx):
        await ctx.send("Looking for a random joke...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://icanhazdadjoke.com/slack") as r:
                data = await r.json()
                embed = discord.Embed(description=data['attachments'][0]['text'])
                await ctx.send(embed=embed)

    @commands.command(description="Returns a random word", brief="Returns a random word")
    async def word(self, ctx):
        await ctx.send("Looking for a random word...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random-word-api.herokuapp.com/word") as r:
                data = await r.json()
                descrip = 'Your random word is: {}'.format(data[0])
                embed = discord.Embed(description=descrip)
                await ctx.send(embed=embed)

    @commands.command(description="Returns a random insult", brief="Returns a random insult")
    async def insult(self, ctx, member: discord.Member = None):
        await ctx.send("Looking for a random insult...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://evilinsult.com/generate_insult.php?lang=en&type=json") as r:
                data = await r.json()
                if member != None:
                    if member.nick != None:
                        text = '{} Eat that, {}!'.format(data['insult'], member.nick)
                    else:
                        text = '{} Eat that, {}!'.format(data['insult'], member.name)
                else:
                    text = format(data['insult'])
                embed = discord.Embed(description=text)
                await ctx.send(embed=embed)

    # @commands.command(description="Returns a random fun fact", brief="Returns a random fun fact")
    # async def funfact(self, ctx):
    #     await ctx.send("Looking for a fun fact...")
    #     async with aiohttp.ClientSession() as cs:
    #         async with cs.get("https://uselessfacts.jsph.pl/random.json?language=en") as r:
    #             data = await r.json()
    #             embed = discord.Embed(description=data['text'])
    #             await ctx.send(embed=embed)

    @commands.command(description="Returns a random number fact", 
                        brief="Returns a random number fact")
    async def numfact(self, ctx):
        await ctx.send("Looking for a number fact...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://numbersapi.com/random?json") as r:
                data = await r.json()
                embed = discord.Embed(description=data['text'])
                await ctx.send(embed=embed)

    @commands.command(description="Returns a random dog fact", 
                            brief="Returns a random dog fact")
    async def dogfact(self, ctx):
        await ctx.send("Looking for a dog fact...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog-api.kinduff.com/api/facts") as r:
                data = await r.json()
                embed = discord.Embed(description=data['facts'][0])
                await ctx.send(embed=embed)

    @commands.command(description="Returns a random cat fact",
                            brief="Returns a random cat fact")
    async def catfact(self, ctx):
        await ctx.send("Looking for a cat fact...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://catfact.ninja/fact") as r:
                data = await r.json()
                embed = discord.Embed(description=data['fact'])
                await ctx.send(embed=embed)

    @commands.command(description="Returns a random phrog fact",
                            brief="Returns a random phrog fact")
    async def phrogfact(self, ctx):
        await ctx.send("Looking for a phrog fact...")
        answer = get_frog_facts()
        embed = discord.Embed(description=answer)
        await ctx.send(embed=embed)

    @commands.command(description="Returns a random 8-ball answer",
                            brief="Returns a random 8-ball answer")
    async def eightball(self, ctx):
        answer = get_8ball_answer()
        await ctx.send(":8ball:" + answer)

    @commands.command(description="Returns sadness",
                            brief="Returns sadness")
    async def cry(self, ctx):
        answer = get_sad_face()
        await ctx.send(answer)

    @commands.command(description="Returns a hug", brief="Returns a hug")
    async def hug(self, ctx, member: discord.Member = None):
        if member != None:
            if member.nick != None:
                text = '༼つ ் ▽ ் ༽つ ⊂( **{}** ⊂)'.format(member.nick)
            else:
                text = '༼つ ் ▽ ் ༽つ ⊂( **{}** ⊂)'.format(member.name)
        else:
            text = '༼つ ் ▽ ் ༽つ ⊂(´・ω・｀⊂)'

        embed = discord.Embed(description=text)
        await ctx.send(embed=embed)

    @commands.command(description="Returns a random Valorant agent",
                            brief="Returns a random Valorant agent")
    async def agent(self, ctx):
        answer = get_agent()
        embed = discord.Embed(description="Your agent is {}.".format(answer))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Text(bot))