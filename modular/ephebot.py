import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import importlib
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
    await importlib.import_module(arg)
    await importlib.invalidate_caches()
    await bot.say("Loaded " + arg)
    print("Loaded " + arg)

    # something something module not found exception

# unload module
@bot.command()
async def unload(arg):
    await del arg
    await bot.say(arg + "unloaded")
    print(arg + "unloaded")

    # something something module not loaded exception

#reload module
@bot.command()
async def reload(arg):
    await importlib.reload(arg)
    await importlib.invalidate_caches()
    await bot.say("Reloaded " + arg)
    print("Reloaded " + arg)

    # something something module not found exception

# bot restart command ..?



bot.run(token)