from asyncio.windows_events import NULL
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import lyricsgenius
from LoopSystem import Loop_System
load_dotenv()
TOKEN = os.getenv('TOKEN')
geniusKey = "URYL2IOIx69b2C43KbAKNCGLhAa9yY-bidzUdn3TILjI1MNFu2GlLUFh-0xmWDZk"
bot = commands.Bot(command_prefix='!')
genius = lyricsgenius.Genius(geniusKey)


@bot.event
async def on_ready():
    print("I'm online")


@bot.command()
async def isGay(ctx, *, funny):
    if(funny == "Soham"):
        await ctx.send("%s is gay" % funny)
    else:
        await ctx.send("%s is straight" % funny)


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def lyricfind(ctx, *, query):
    details = query.split("#")
    artist = genius.search_artist(details[0], max_songs=0)
    song = artist.song(details[1])
    if(song.lyrics == NULL):
        await ctx.send("Lyric failed to load")
    else:
        await ctx.channel.send(song.lyrics)
    return

bot.run('MTAwMDc3NzAxMDg2NTUwNDI1Ng.GN2UCH.AoaqRqwP5n4_CozqdbwbwZcTK_qjF3aqrKKsiA')
