__authors__ = 'aejb'

## requires d.py 1.0
## requires python3.6
import discord
from discord.ext import commands
import traceback
import sys
import asyncio
from time import gmtime, strftime


def gettoken():
    token_file = open("/home/mbp/every-day/token.txt", "r")
    token_string = token_file.read()
    token_token = token_string.split("\n")
    bot_token = str(token_token[0])
    return bot_token


bot_token = gettoken()

description = "ed!"
bot = commands.Bot(command_prefix=["ed!"], description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    user = await bot.fetch_user(173498062260404225)
    ctx = await user.send("How are you feeling today?\nFormat is <1 awful ~ great 5>|<today's events>")
    try:
        def check_if_dm(ctx):
            return ctx.author == user and ctx.channel == user.dm_channel
        response = await bot.wait_for("message", check=check_if_dm)
    except asyncio.TimeoutError:
        print("no response")
    else:
        to_csv = response.content.split("|")
        date_add = "\""+strftime("%d %b %Y", gmtime())+"\""
        write_string = "\n"+date_add+",\""+to_csv[0]+"\",\""+to_csv[1]+"\""
        with open('2020.csv','a') as fd:
            fd.write(write_string)

        response_string = "Recorded today, "+date_add+" as feeling "+to_csv[0]+", having done the following: \n"+to_csv[1]
        await user.send(response_string)
        await bot.close()
        exit()


bot.run(bot_token)
