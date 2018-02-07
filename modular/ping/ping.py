"""
ping
"""
@bot.command
async def ping(ctx):
    await bot.say(":ping_pong: pong!!")
    print("user has pinged")