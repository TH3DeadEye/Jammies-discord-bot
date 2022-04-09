import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
bot = commands.Bot(command_prefix='?')  # prefix our commands with '.'
#this event will be called when the bot is ready to use 
@bot.event
async def on_ready():
    bot.change_presence(activity=discord.Activity(name ="?Help", type = discord.ActivityType.watching))
    print(f"{bot.user.name} - {bot.user.id}")
    print('Jammies is ready!')


#setting up the commands
@bot.command()
async def clear(ctx , amount = 100):
    channel = ctx.message.channel
    messages = []

    async for message in channel.history(limit=amount):
        messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send("Messages have been cleared")


bot.run(os.getenv('TOKEN'))