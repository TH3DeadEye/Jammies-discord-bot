from turtle import color
import discord 
from discord.ext import commands
import datetime

class mod_commands(commands.Cog):
    def __init__(self, bot):
         self.bot = bot
    
    @commands.command()
    async def clear(self , ctx , ammount=100):
        if ctx.author.guild_permissions.administrator:
            if ammount > 100:
                await ctx.send("You can only delete 100 messages at once")
            else:     
                await ctx.channel.purge(limit=ammount)
                await ctx.send(f"{ammount} messages have been deleted")
        else:
            await ctx.send("You don't have the permission to use this command")

    @commands.command()
    async def ban(self, ctx, user: discord.Member, * , reason=None):
            #ban command
            await ctx.guild.ban(user, reason=reason)
            await user.send(f"you have been banned in {ctx.guild} for {reason}")
            await ctx.send(f"{user} has been banned for {reason}")

    @commands.command()
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        #dm the moderator who banned the user
        await ctx.author.send(
            embed = discord.Embed(
            title = f"{member} has been kicked from {ctx.guild}",
            description = f"Reason: {reason}",
            color = discord.Color.purple()
            )
        )
        #craete a embed for the kick command and send it to the user 
        embed = discord.Embed(
        title="You have been kicked from the server", 
        description=f"You have been kicked from the server for {reason} you can try and join again in 2 months", 
        color= discord.Color.purple()
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Kicked by {ctx.author}")
        await member.send(embed=embed)

            
        

def setup(bot):
    bot.add_cog(mod_commands(bot))