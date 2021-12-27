import discord
from discord.ext import commands


class BeatmapHitsounds(commands.Cog):
    def __init__(self, client):
        self.client = client
        
                
    @commands.command(aliases=["BeatmapWithNoHitsound", "Beatmap", "MapWithoutHitsound", "MapWithNoHitsound"])
    async def BeatmapHitsounds(self, ctx):
        embed = discord.Embed(
            title = "Map does not play the hitclap, hitfinish and whistle",
            description = "You may have enabled 'Ignore beatmap hitsounds' option on osr2mp4, disabling it should fix this problem.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840684173383041044/maphitsounds.png")
        await ctx.send(embed=embed)          
        
        
        
def setup(client):
    client.add_cog(BeatmapHitsounds(client))