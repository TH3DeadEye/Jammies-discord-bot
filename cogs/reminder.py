import discord 
from discord.ext import commands
import asyncio
import datetime
import time

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    reminder_list = []
    @commands.command()
    async def reminder(self , ctx , time , *, message):
        await ctx.send(f"reminder has been set for {time}")
        await asyncio.sleep(int(time))
        await ctx.send(f"@{ctx.author.name} {message}")
        #append all the reminder to a list
        self.reminder_list.append(f"{time} {message}")

    @commands.command()
    async def reminder_list(self , ctx):
        await ctx.send(f"reminder list: {self.reminder_list}")


def setup(bot):
    bot.add_cog(Reminder(bot))