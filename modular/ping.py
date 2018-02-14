"""
ping
"""

import discord, asyncio, logging
from discord.ext import commands
from discord.ext.commands import Bot
from config import *

# module name
mod = 'ping'

@bot.command()
async def ping():
    # if code is being executed as main program and flag is not turned off
    if __name__ == "__main__" and modlist[mod] != 0:
        await bot.say(":ping_pong: pong!!")
        print("user has pinged")
    else:
        print("module disabled: " + mod)