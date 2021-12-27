import discord
from discord.ext import commands


class TheRightArrow(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["RightArrow", "Arrow", "Output", "Extension", "LiterallyAnySymbol"])
    async def TheRightArrow(self, ctx):
        embed = discord.Embed(
            title = "The right arrow - ►",
            description = "Seems like you have named your output file wrongly or with an incorrect extension, check if it is not spelt wrongly, the common extensions are: `.avi / .mkv / .mp4 / .mov` ",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840336835166732290/840727410411569182/THE_RIGHT_SKIN_SHIT.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840715150382334002/square.jpg")
        embed.set_footer(text="It also applies to this error since they are the same, just displayed differently.") 
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(TheRightArrow(client))