"""
ping
"""

@bot.command()
async def ping():
    await bot.say(":ping_pong: pong!!")
    print("user has pinged")