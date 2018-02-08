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
@bot.command
async def enable(module):
    if module in config: # check if the module is in config.py dictionary
        if config[module] == 0: # check if the module is disabled
            config[module] = 1 # enable the module
            await bot.say('Enabled ' + module)
            print('Enabled ' + module)
        else: # config[module] == 1
            await bot.say(module + ' is already enabled')
    else: # module is not in config.py dictionary
        await bot.say(module + ' was not found in config.py')





# disable module

# reload module ..?

# bot restart command ..?



bot.run(token)