
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

# @bot.command(pass_context=True)
# async def info(ctx, user: discord.Member):
#     await bot.say("The users name is: {}".format(user.name))
#     await bot.say("The users ID is: {}".format(user.id))
#     await bot.say("The users status is: {}".format(user.status))
#     await bot.say("The users highest role is: {}".format(user.top_role))
#     await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Bye, {}.".format(user.name))
    await bot.kick(user)


@bot.event
async def on_message(message):
    print(message)
    if message.content == "cookie":
        print('cookie')
        await bot.say(message.channel, ":cookie:")

@bot.event
async def on_message2(message):
    if message.content == "!!nsfw":
        await bot.say(message.channel, "NSFW NSFW NSFW NSFW NSFW NSFW NSFW NSFW NSFW")

bot.run("NDA4NDYwOTU0NzgzNzExMjMy.DVadMQ.XR_SaTOX9DzljLGtOr5CV1MoN80")
