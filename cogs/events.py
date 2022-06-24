import discord 
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="?Help"))
        print(f"{self.bot.user.name} just got online!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to the server!'
        )

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')
        await member.create_dm()
        await member.dm_channel.send(
            f'Goodbye {member.name}, hope to see you again!'
        )
    
    

#setup the extension
def setup(bot):
    bot.add_cog(Greetings(bot))
