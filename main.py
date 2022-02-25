#load libraries
import os
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()

bot = Bot("!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def  ping(ctx):
    await ctx.send("pong")
    print(ctx.message.author.name + " has pinged the bot")

bot.run(os.getenv('TOKEN'))