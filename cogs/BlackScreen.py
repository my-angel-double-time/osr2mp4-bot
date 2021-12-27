import discord
from discord.ext import commands


class BlackScreen(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def BlackScreen(self, ctx):
        embed = discord.Embed(
            title = "Video is black screen",
            description = "This is due to the `-crf 0`, which is hard to decode.",
            colour = discord.Color.from_rgb(234, 84, 247)
        )
        embed.add_field(name="If it is high FPS:", value="Just resample using either Vegas or bs-cli. (If you are using bs-cli, choose other -crf value when resampling).", inline=True)
        embed.add_field(name="If it is 60 FPS:", value="Chances are, you are using Windows Media Player, try a different player, like MPC-BE / MPC-HC.", inline=True)
        embed.set_footer(text="Type o!resampletutorial to see how to resample a video using Vegas") 
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840395769555320872/blackscreen.png") 
        await ctx.send(embed=embed)        
        
        
        
        
def setup(client):
    client.add_cog(BlackScreen(client))