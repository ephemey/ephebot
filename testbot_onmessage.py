import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

token = 'NDA4NDYwOTU0NzgzNzExMjMy.DVadMQ.XR_SaTOX9DzljLGtOr5CV1MoN80'
nsfw_msg = ':pepeRAGE: :pepeRAGE: :pepeRAGE: :regional_indicator_n: :regional_indicator_s: :regional_indicator_f: :regional_indicator_w: :pepeRAGE: :pepeRAGE: :pepeRAGE:'

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print("Username: " + bot.user.name)
    print("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!!")
    print("user has pinged")


@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    # respond if NSFW content is posted and labeled '!!nsfw'
    if '!!nsfw' in message.content:
        await bot.send_message(message.channel, nsfw_msg)


bot.run(token)

