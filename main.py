import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_ui import UI 
 



load_dotenv()
intense = discord.Intents(message = True, guilds=True, reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix="?", intense = intense)
UI = UI(bot)

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

        
if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(os.getenv('TOKEN'))