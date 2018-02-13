import discord, asyncio, logging
from discord.ext import commands
from discord.ext.commands import Bot
import config

# logging
logging.basicConfig(level=logging.INFO)

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
@bot.command()
async def enable(mod = ''):
    mod = str(mod)
    if len(mod) == 0: # check if mod is empty
        await bot.say(';enable <module> to enable') # help
    else:
        if mod in config.modlist: # check if the module is in config.py dictionary
            if config.modlist[mod] == 0: # check if the module is disabled
                config.modlist[mod] = 1 # enable the module
                await bot.say('Enabled ' + mod)
                print('Enabled ' + mod)
            else: # modlist[mod] == 1
                await bot.say(mod + ' is already enabled')
        else: # module is not in config.py dictionary
            await bot.say(mod + ' was not found in config.py')


# disable module

# reload module ..?

# bot restart command ..?



bot.run(token)