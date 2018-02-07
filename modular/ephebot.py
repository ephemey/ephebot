import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

# ask for token
token = input('bot token: ')

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
    await import arg
    await bot.say("Loaded " + arg)
    print("Loaded " + arg)

bot.run(token)