import discord
from discord.ext import commands


class XVID(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["TheCodec", "TroublesomeShit"])
    async def XVID(self, ctx):
        embed = discord.Embed(
            title = "XVID for High FPS",
            description = "XVID really, really does not work well for high FPS. It may be faster, but the quality is nothing compared to x264.\n\nTo fix this, and to allow high FPS:\nEnable the \"FFmpeg Video Writer\" in your osr2mp4 settings. If you're missing ffmpeg or your files do not look like [this,](https://cdn.discordapp.com/attachments/840336835166732290/840707062492561428/videowriter.png) then you should download [this](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full-shared.7z), extract the files, and move all of the files in the **bin** folder to the root of your osr2mp4 folder.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840705982749212712/XVID.jpg") 
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(XVID(client))