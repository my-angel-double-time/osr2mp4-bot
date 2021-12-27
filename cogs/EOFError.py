import discord
from discord.ext import commands


class EOFError(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["EOF"])
    async def EOFError(self,ctx):
        embed = discord.Embed(
            title = "EOFError()",
            description = "Old issue, update your app.",
            colour = discord.Color.from_rgb(234,84,247)
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/919284502751223808/EOFError.png")
        await ctx.send(embed=embed)
        
        
def setup(client):
    client.add_cog(EOFError(client))