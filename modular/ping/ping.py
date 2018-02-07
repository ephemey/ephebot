"""
ping
"""
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!!")
    print("user has pinged")