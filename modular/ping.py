"""
ping
"""

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from ephebot import *

bot = commands.Bot(command_prefix=';')

# module name
mod = 'ping'

@bot.command()
async def ping():
    if modlist[mod] != 0: # check if flag is turned off
        await bot.say(":ping_pong: pong!!")
        print("user has pinged")
    else:
        print("module disabled: " + mod)