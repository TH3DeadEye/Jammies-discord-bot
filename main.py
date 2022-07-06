import discord
import os 
from dotenv import load_dotenv
from discord.ui import Button, View

load_dotenv() 
bot = discord.Bot(debug_guilds=[946701951771496508])

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Game(name="with your feelings"))


"""@bot.slash_command() # Create a slash command
async def button(ctx):
    button = Button(label="example", style=discord.ButtonStyle.primary, emoji="😎")
    view = View()
    view.add_item(button)
    await ctx.respond("Hi", view=view)"""


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"{filename} loaded")

bot.run(os.getenv('TOKEN'))

