import discord
from discord.ext import commands


class DivisionByZero(commands.Cog):
    def __init__(self, client):
        self.client = client
        
                
    @commands.command(aliases=["DivisionBy0", "ZeroDivisionError"])
    async def DivisionByZero(self, ctx):
        embed = discord.Embed(
            title = "ZeroDivisionError('division by zero')division by zero",
            description = "Chances are, you have set your process to 0, you can either change it back to 1 or higher.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://media.discordapp.net/attachments/840336835166732290/840424309636988948/zero.png")
        embed.add_field(name="If you are not using Process 0", value="Super short maps, wrong config values and maps with `CS: 0` can also trigger this error.", inline=True)
        embed.add_field(name="You can use the new progress bar:", value="It is more accurate and will not trigger that error, [you can find it here](https://discord.com/channels/731779243586879548/731827235572678687/794245592905285672).", inline=True)
        await ctx.send(embed=embed)        
        
        
        
def setup(client):
    client.add_cog(DivisionByZero(client))