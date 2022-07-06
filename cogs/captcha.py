import discord
import datetime
import random
from discord.ext import commands
from captcha.image import ImageCaptcha
from discord.ext.commands import slash_command


class Captcha(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="verify", description="Verify a captcha")
    async def verify(self, ctx):
        sender = ctx.author
        image = ImageCaptcha(width=280, height=50)
        captcha_text = random.randint(100000, 999999)
        
        captcha_text = str(captcha_text)

        data = image.generate(captcha_text)
        role_has = discord.utils.get(sender.guild.roles, name="Verified")

        if role_has in ctx.author.roles:
           await ctx.respond("You are already verified!", ephemeral = True)

        else:
            await ctx.respond("Please chack your DM's", ephemeral = True)

            image.write(captcha_text, "captcha/captcha.png")
            File_image = discord.File("captcha/captcha.png", filename="captcha.png")
            embed = discord.Embed(
                title="Captcha",
                description="""Please write the following captcha after you clicked the button\n \n 
                **THIS MESSAGE WILL BE DELETED IN 60 SECONDS**\n
                """,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_image(url="attachment://captcha.png")
            embed.timestamp = datetime.datetime.now() + datetime.timedelta(seconds=60)
            
            print(captcha_text)
   
            await sender.send(embed=embed, file = File_image, delete_after=60)

            #checking the captcha
            while True:
                msg = await self.bot.wait_for("message", check=lambda check: check.author.id == ctx.author.id)

                if msg.guild == None:
                    break
                
            if msg.content == captcha_text:
                    userAvatar = ctx.author.avatar.url
                    embed = discord.Embed(
                    title="Verified",
                    description="You are now verified!",
                    color=discord.Color.blue(),
                    timestamp=datetime.datetime.now()
                    )
                
                    embed.set_thumbnail(url=userAvatar)
                    await sender.send(embed=embed)
                    role = discord.utils.get(sender.guild.roles, name="Verified")
                    await sender.add_roles(role)

                   
            else:
                embed = discord.Embed(title="Error", description="Wrong captcha", color=discord.Color.red())
                embed.add_field(name="Try again", value="Please try again by using /verify ")

                await sender.send(embed=embed)
                print("wrong")

def setup(bot):
    bot.add_cog(Captcha(bot))
