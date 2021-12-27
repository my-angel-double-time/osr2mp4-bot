import discord
from discord.ext import commands


class GlitchyVideo(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["slowvideo"])
    async def GlitchyVideo(self, ctx):
        embed = discord.Embed(
            title = "Video is glitchy / The playback is slow",
            description = "The video itself is fine, it is due to the high FPS recording, resampling should fix it.",
            colour = discord.Color.from_rgb(234, 84, 247)
        )
        embed.set_footer(text="Type o!resampletutorial to see how to resample a video using Vegas")
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840380429361086464/glitchy.png") 
        await ctx.send(embed=embed)
        
        
def setup(client):
    client.add_cog(GlitchyVideo(client))