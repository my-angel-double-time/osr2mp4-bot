import discord
from discord.ext import commands


class FOURCC(commands.Cog):
    def __init__(self, client):
        self.client = client
        
                
    @commands.command()
    async def FOURCC(self, ctx):
        embed = discord.Embed(
            title = "Cannot start writing video, make sure your video fourcc codec is correct and...",
            description = "The better fix is enabling FFmpeg Video Writer, to enable it make sure you did update your app, _or if you are getting problems updating it: _ [use this version.](https://discord.com/channels/731779243586879548/731827235572678687/800229131274944543)",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.add_field(name="Enabling FFmpeg Writer:", value="You must have an FFmpeg build, download and extract everything inside the **bin** folder to the osr2mp4 folder. [Get FFmpeg Build Here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full-shared.7z)", inline=True)
        embed.add_field(name="Using the #fixes version:", value="You already have the FFmpeg build there, you are ready to go.", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840407174642794506/fourcc.gif")
        await ctx.send(embed=embed)        
        
        
        
def setup(client):
    client.add_cog(FOURCC(client))