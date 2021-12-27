import discord
from discord.ext import commands


class CalledProcessError(commands.Cog):
    def __init__(self, client):
        self.client = client
        
                
    @commands.command(aliases=["PermissionError", "Permission", "OutOfSpace", "NoSpaceLeft"])
    async def CalledProcessError(self, ctx):
        embed = discord.Embed(
            title = "CalledProcessError",
            description = "Since there are two reasons that could call process error, you need to understand what is more likely to be happening to you.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.add_field(name="if it happened when finishing the render:", value="osr2mp4 needs about to 2x the size of the video when rendering, if there is no space left in disk, it will raise CalledProcessError.", inline=True)
        embed.add_field(name="If it happened when starting the render:", value="Seems like FFmpeg did not get the permission to start the conversion, moving the osr2mp4 folder to `Program Files` can fix it.", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840421983086444553/pe.png")
        embed.set_footer(text="Program Files is usually located in your C: drive directory.") 
        await ctx.send(embed=embed)       
        
        
        
def setup(client):
    client.add_cog(CalledProcessError(client))