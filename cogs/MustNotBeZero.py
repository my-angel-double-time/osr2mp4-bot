import discord
from discord.ext import commands


class MustNotBeZero(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command(aliases=["Arg3"])
    async def MustNotBeZero(self, ctx):
        embed = discord.Embed(
            title = "ValueError('range() arg 3 must not be zero')",
            description = "This is related to an old FPS cap osr2mp4 used to have, updating your app should fix it.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840411386755678258/arg3.png")
        embed.set_footer(text="Use #fixes version if you are having problems when updating.") 
        await ctx.send(embed=embed)                
        
        
def setup(client):
    client.add_cog(MustNotBeZero(client))