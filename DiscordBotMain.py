from asyncio.windows_events import NULL
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import lyricsgenius
from LoopSystem import Loop_System
from QueueSystem.Queue_System import QueueSystem as qs
load_dotenv()
TOKEN = os.getenv('TOKEN')
geniusKey = "URYL2IOIx69b2C43KbAKNCGLhAa9yY-bidzUdn3TILjI1MNFu2GlLUFh-0xmWDZk"
bot = commands.Bot(command_prefix='!')
genius = lyricsgenius.Genius(geniusKey)


@bot.event
async def on_ready():
    print("I'm online")


bot.run('MTAwMDc3NzAxMDg2NTUwNDI1Ng.GN2UCH.AoaqRqwP5n4_CozqdbwbwZcTK_qjF3aqrKKsiA')
