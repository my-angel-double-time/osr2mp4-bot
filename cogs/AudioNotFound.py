import discord
from discord.ext import commands


class AudioNotFound(commands.Cog):
    def __init__(self, client):
        self.client = client
        
                
    @commands.command(aliases=["ANF"])
    async def AudioNotFound(self, ctx):
        embed = discord.Embed(
            title = "Audio Not Found Error",
            description = "Chances are, either you are trying to render a replay without the map audio.mp3 or FFmpeg can't access the `audio.mp3`.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.add_field(name="If there is no .mp3:", value="Most obvious one, drop the mp3 file inside the map folder.", inline=True)
        embed.add_field(name="If there is already an mp3:", value="Try moving your osr2mp4 folder to the Programs File folder", inline=True)
        embed.set_footer(text="Program Files is usually located in your C: drive directory.")
        await ctx.send(embed=embed)        
        
        
        
def setup(client):
    client.add_cog(AudioNotFound(client))