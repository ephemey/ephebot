import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print("Username: " + bot.user.name)
    print("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!!")
    print("user has pinged")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Bye, {}.".format(user.name))
    await bot.kick(user)

@bot.event
async def on_message(message):
    if message.content == "cookie":
        print('cookie')
        await bot.say(message.channel, ":cookie:")


bot.run("NDA4NDYwOTU0NzgzNzExMjMy.DVadMQ.XR_SaTOX9DzljLGtOr5CV1MoN80")

