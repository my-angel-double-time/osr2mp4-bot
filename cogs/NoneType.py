import discord
from discord.ext import commands


class NoneType(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["Type", "NotSTD", "Gamemodes", "UnsuportedGamemode"])
    async def NoneType(self, ctx):
        embed = discord.Embed(
            title = "TypeError(\"object of type 'NoneType' has no len()\")",
            description = "You are trying to convert a non standard replay; unfortunately osr2mp4 does not support the other 3 game modes.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://media.discordapp.net/attachments/840336835166732290/840698650475757598/NoneType.png") 
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(NoneType(client))