import random
import aiohttp
import discord
from discord.ext import commands
from settings import *
import praw
from utils import check_image
import re

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, 
            client_secret=REDDIT_APP_SECRET, user_agent="PHROGGERS:%s:1.0" % REDDIT_APP_ID)

    @commands.command(description="Returns a random image of a phrog.",
                            brief="Returns a random image of a phrog")
    async def phrog(self, ctx):
        await ctx.send("Looking for a phrog...")
        if self.reddit:
            subreddit = 'frogs'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 50)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title="Phroggers!! :frog:")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random image of a monkee.",
                            brief="Returns a random image of a monkee")
    async def monkee(self, ctx):
        await ctx.send("Looking for a monkee...")
        if self.reddit:
            subreddit = 'monkeys' if random.randint(0, 2) == 0 else 'ape'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":monkey: Embrace monkee")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random image of a birb.", 
                        brief='Returns a random image of a bird')
    async def birb(self, ctx):
        await ctx.send("Looking for a birb...")
        if self.reddit:
            subreddit = 'birbs'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":hatching_chick: Oh look, a birb!")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random image of a dog.",
                            brief='Return a random image of a dog')
    async def dog(self, ctx):
        await ctx.send("Looking for a good boi...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                data = await r.json()

                embed = discord.Embed(title=":dog: Oh look, a doggo!")
                embed.set_image(url=data['message'])
                embed.set_footer(text="Powered by: https://dog.ceo/dog-api/")

                await ctx.send(embed=embed)
    
    @commands.command(description="Returns a random image of a cat.",
                        brief='Return a random image of a cat')
    async def cat(self, ctx):
        await ctx.send("Looking for a cat...")
        if self.reddit:
            subreddit = random.choice(REDDIT_ENABLED_CAT_SUBREDDITS)
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":cat: Oh look, a cat!")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random cute image of an animal.",
                        brief='Return a random image of a cute animal')
    async def cute(self, ctx):
        await ctx.send("Looking for a cute animal...")
        if self.reddit:
            subreddit = 'aww'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":smiling_face_with_3_hearts: owo uwu owu uwo :smiling_face_with_3_hearts:")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")
    
    @commands.command(description="Returns a random image of a fox.", 
                        brief='Return a random image of a fox')
    async def fox(self, ctx):
        await ctx.send("Looking for a fox...")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://randomfox.ca/floof/?ref=apilist.fun") as r:
                data = await r.json()

                embed = discord.Embed(title="Oh look, a fox!")
                embed.set_image(url=data['image'])
                embed.set_footer(text="Powered by: https://randomfox.ca/")

                await ctx.send(embed=embed)

    @commands.command(description="Returns a random food image.",
                        brief='Returns a random image of food')
    async def food(self, ctx):
        await ctx.send("Looking for a dish...")
        if self.reddit:
            subreddit = random.choice(REDDIT_ENABLED_FOOD_SUBREDDITS)
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":drooling_face: Mmmmmmm...")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
            embed.set_footer(text="Powered by: " + submission.url)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random wholesome meme.",
                            brief='Returns a wholesome meme')
    async def wholesome(self, ctx):
        await ctx.send("Looking for a wholesome meme...")
        if self.reddit:
            subreddit = 'wholesomememes'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":smiling_face_with_3_hearts: uwuwuwuwuwuwuwuwuwu")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random meme.",
                        brief='Returns a random meme')
    async def meme(self, ctx):
        await ctx.send("Looking for a meme...")
        if self.reddit:
            subreddit = 'memes'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":frog: Major Phroggers :frog:")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

    @commands.command(description="Returns a random hatsune miku picture.",
                        brief='Returns a random hatsune miku image')
    async def hm(self, ctx):
        await ctx.send("Looking for a picture of Hatsune Miku...")
        if self.reddit:
            subreddit = 'hatsune'
            submissions = self.reddit.subreddit(subreddit).hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                test = next(x for x in submissions if not x.stickied and not x.is_self)
                if check_image(test.url):
                    submission = test
            embed = discord.Embed(title=":flushed:")
            embed.set_image(url=submission.url)
            embed.set_footer(text="Powered by: " + submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error, contact Administrator")

def setup(bot):
    bot.add_cog(Images(bot))