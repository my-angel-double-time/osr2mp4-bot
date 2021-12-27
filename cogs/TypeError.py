import discord
from discord.ext import commands


class TypeError(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def TypeError(self, ctx):
        embed = discord.Embed(
            title = "TypeError(''Scalar value for argument 'color' is longer than 4'')",
            description = "See `o!parsingerror` command.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840727549125853185/skinshit2.png") 
        await ctx.send(embed=embed)   


def setup(client):
    client.add_cog(TypeError(client))