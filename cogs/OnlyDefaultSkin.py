import discord
from discord.ext import commands


class OnlyDefaultSkin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["DefaultSkin", "Default"])
    async def OnlyDefaultSkin(self, ctx):
        embed = discord.Embed(
            title = "There is no skin available but Default Skin",
            description = "Either you must have set something wrong when selecting the osu! path or osr2mp4 just did not get it correctly. \n\nSelecting your osu!path again (the root osu! folder not songs/skins folder) and restarting app should fix it.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840748831053578240/default_skin.png") 
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(OnlyDefaultSkin(client))