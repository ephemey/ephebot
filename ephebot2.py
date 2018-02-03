import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import logging

token = 'NDA4NDYwOTU0NzgzNzExMjMy.DVadMQ.XR_SaTOX9DzljLGtOr5CV1MoN80'
nsfw_msg = ':pepeRAGE: :pepeRAGE: :pepeRAGE: :regional_indicator_n: :regional_indicator_s: :regional_indicator_f: :regional_indicator_w: :pepeRAGE: :pepeRAGE: :pepeRAGE:'

logging.basicConfig(level=logging.WARNING)

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

# @bot.command(pass_context=True)
# async def meow(ctx):
#     await bot.say("nyaaaa")
#     print("nyaaaaa")

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    # respond if NSFW content is posted and labeled '!!nsfw'
    if '!!nsfw' in message.content:
        await bot.send_message(message.channel, nsfw_msg)

# @bot.command(pass_context=True)
# async def kick(ctx, user: discord.Member):
#     await bot.say(":boot: Bye, {}.".format(user.name))
#     await bot.kick(user)


bot.run(token)

