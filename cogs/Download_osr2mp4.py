import discord
from discord.ext import commands


class Download_osr2mp4(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["Download", "osr2mp4","osr2mp4-app", "osrmp4-core"])
    async def Download_osr2mp4(self, ctx):
        embed = discord.Embed(
            title = "osr2mp4 download links",
            description = "Here you can find the links for the core and app version.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.add_field(name="osr2mp4-app [FireRedz Version]", value="A fork from the original app, with some fixes and improvements: [download](https://github.com/FireRedz/osr2mp4-app/releases/tag/v0.4-test)", inline=True)
        embed.add_field(name="osr2mp4-app", value="The version **with** user interface: [download](https://github.com/uyitroa/osr2mp4-app/releases/tag/v0.3)", inline=True)
        embed.add_field(name="osr2mp4-core", value="The version **without** user interface: [download](https://github.com/uyitroa/osr2mp4-core)", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/841001602538143744/osr.png")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Download_osr2mp4(client))