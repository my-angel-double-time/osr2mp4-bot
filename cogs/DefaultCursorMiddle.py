import discord
from discord.ext import commands


class DefaultCursorMiddle(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["DefaultCursor", "BuggyCursor"])
    async def DefaultCursorMiddle(self, ctx):
        embed = discord.Embed(
            title = "Default cursor-middle showing on replay",
            description = "Seems like your osr2mp4 app did not update properly, try using [#fixes](https://discord.com/channels/731779243586879548/731827235572678687/800229131274944543) version.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840701412807016519/cursormiddle.png") 
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(DefaultCursorMiddle(client))