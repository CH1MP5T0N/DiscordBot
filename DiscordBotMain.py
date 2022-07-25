from dotenv import load_dotenv
import discord
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    # db.connectDatabase()
    print("I'm online")


@bot.command()
async def isGay(ctx, *, funny):
    if(funny == "Soham"):
        await ctx.send("%s is gay" % funny)
    else:
        await ctx.send("%s is straight" % funny)


load_dotenv('.env')
bot.run(os.getenv('TOKENKARAOKE'))
