"""
function
"""

import discord, asyncio, logging
from discord.ext import commands
from discord.ext.commands import Bot
from config import *


@bot.command()
async def function():
    await bot.say("say something")
    print("said something")