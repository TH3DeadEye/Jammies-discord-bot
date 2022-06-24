from distutils.sysconfig import PREFIX
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv



load_dotenv()
bot = commands.Bot(command_prefix="?")

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

        
if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(os.getenv('TOKEN'))