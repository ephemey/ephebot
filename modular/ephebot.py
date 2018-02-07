import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import importlib
import sys
import logging

# logging
logging.basicConfig(level=logging.WARNING)

# ask for token
# token = input('bot token: ')
token = "NDA4NDYwOTU0NzgzNzExMjMy.DVzywA.27Ee8-s06s7PUW7SVHBtpibQ2s4"

# set bot commmand prefix
bot = commands.Bot(command_prefix=';')

# on bot initiation
@bot.event
async def on_ready():
    print("Username: " + bot.user.name)
    print("ID: " + bot.user.id)
    print("Connected")

# load module
@bot.command()
async def load(arg):
    from arg importlib.import_module(*)
    importlib.invalidate_caches()
    await bot.say("Loaded " + arg)
    print("Loaded " + arg)

    # something something module not found exception

# unload module
@bot.command()
async def unload(arg):
    sys.modules.pop(arg)
    await bot.say(arg + "unloaded")
    print(arg + "unloaded")

    # something something module not loaded exception

#reload module
@bot.command()
async def reload(arg):
    importlib.reload(arg)
    importlib.invalidate_caches()
    await bot.say("Reloaded " + arg)
    print("Reloaded " + arg)

    # something something module not found exception

# bot restart command ..?



bot.run(token)