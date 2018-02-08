import discord, asyncio, logging
from discord.ext import commands
from discord.ext.commands import Bot

import config

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

# enable module
async def enable(module):
    if module.flag == true:



# disable module

# reload module ..?

# bot restart command ..?



bot.run(token)