import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print("Username: " + bot.user.name)
    print("ID: " + bot.user.id)

# @bot.event
# async def on_message(message):
#     if message.content == "cookie":
#         await bot.send_message(message.channel, ":cookie:")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!!")
    print("user has pinged")

@bot.command(pass_context=True)
async def meow(ctx):
    await bot.say("nyaaaa")
    print("nyaaaaa")

@bot.command(pass_context=True)
async def nsfw(ctx):
    await bot.say("WARNING NSFW WARNING NSFW WARNING NSFW WARNING NSFW WARNING NSFW")
    print("NSFW af")

# @bot.command(pass_context=True)
# async def kick(ctx, user: discord.Member):
#     await bot.say(":boot: Bye, {}.".format(user.name))
#     await bot.kick(user)


bot.run("NDA4NDYwOTU0NzgzNzExMjMy.DVadMQ.XR_SaTOX9DzljLGtOr5CV1MoN80")

