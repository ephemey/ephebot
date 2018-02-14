import discord, asyncio, logging, importlib
from discord.ext import commands
from discord.ext.commands import Bot
from ping import *

# set bot commmand prefix
bot = commands.Bot(command_prefix=';')

modlist = {
    'ping':0,
    
}

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################

# link to invite bot 
# https://discordapp.com/oauth2/authorize?client_id=408460954783711232&scope=bot

# logging
logging.basicConfig(level=logging.INFO)

# ask for token
# token = input('bot token: ')
token = "NDA4NDYwOTU0NzgzNzExMjMy.DVzywA.27Ee8-s06s7PUW7SVHBtpibQ2s4"


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
        if mod in modlist: # check if the module is in config.py dictionary
            if modlist[mod] == 0: # check if the module is disabled
                modlist[mod] += 1 # enable the module
                await bot.say('Enabled ' + mod)
                print('Enabled ' + mod)
            else: # modlist[mod] == 1
                await bot.say(mod + ' is already enabled')
        else: # module is not in config.py dictionary
            await bot.say(mod + ' was not found in config.py')

# disable module
@bot.command()
async def disable(mod = ''):
    mod = str(mod)
    if len(mod) == 0: # check if mod is empty
        await bot.say(';disable <module> to disable') # help
    else:
        if mod in modlist: # check if the module is in config.py dictionary
            if modlist[mod] == 1: # check if the module is enabled
                modlist[mod] -= 1 # disable the module
                await bot.say('Disabled ' + mod)
                print('Disabled ' + mod)
            else: # modlist[mod] == 0
                await bot.say(mod + ' is already disabled')
        else: # module is not in config.py dictionary
            await bot.say(mod + ' was not found in config.py')    

# check if flag is actually enabled
@bot.command()
async def check(mod = ''):
    if len(mod) == 0: # check if mod is empty
        await bot.say(';check <module> to check')
    else:
        if mod in modlist: # check if mod is in config.py modlist
            await bot.say(modlist[mod]) # prints the value for the key 'mod'
        else: # module not in config.py dictionary 
            await bot.say(mod + ' was not found in config.py')

# reload module ..?
@bot.command()
async def reload(mod = ''):
    if len(mod) == 0: # check if mod is empty
        await bot.say(';reload <module> to reload') # help
    else:
        if mod in modlist: # check if the module is in config.py dictionary
            importlib.reload(mod)
            await bot.say('Reloaded ' + mod)
        else: # module is not in config.py dictionary
            await bot.say(mod + ' was not found in config.py')   

# shutdown 
@bot.command()
async def part():
    await bot.say('Bye')
    print('Shutting down...')
    quit()



bot.run(token)