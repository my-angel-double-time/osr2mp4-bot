import discord
from discord.ext import commands


class Vegas(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["VegasError", "VegasWrongExtension"])
    async def VegasCantOpenVideo(self, ctx):
        embed = discord.Embed(
            title = "None of the files dropped on Vegas Pro could be opened",
            description = "That is problably because you are using either XVID codec at high FPS or are using x264/x265 but with `.avi` extension.\n\nYou can fix it by reencoding in x264/x265 with `.mp4` extension.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840751181239812117/avi_extension.png") 
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["how_to_resample_using_VEGAS", "resampletutorial"])
    async def VegasTutorial(self, ctx):
        await ctx.send("**How to resample using VEGAS:** https://youtu.be/sBio8ClNrYE?t=51")     


def setup(client):
    client.add_cog(Vegas(client))