import discord
from discord.ext import commands


class PPCounter(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def PPCounter(self, ctx):
        embed = discord.Embed(
            title = "PP Counter is wrong/outdated!",
            description = "Unfortunately there is not much we can do about this, osr2mp4 uses a third library for the pp counter and it still not updated, probably will not update any time soon either.\n\nAlternatively you can try https://ordr.issou.best/",
            colour = discord.Color.from_rgb(234, 84, 247) 
        ) 
        await ctx.send(embed=embed) 

                
    @commands.command()
    async def Custom_PPCounter(self, ctx):
        embed = discord.Embed(
            title = "If you are looking forward to customize your PP Counter",
            description = "Running the CustomPP.exe will give you that possibility.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840425841150001162/ppcounter.png")
        embed.set_footer(text="Take a look into the #pp-counter-flex too see some templates made by the community.") 
        await ctx.send(embed=embed)       
        
        
def setup(client):
    client.add_cog(PPCounter(client))