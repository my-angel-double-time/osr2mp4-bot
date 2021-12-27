import discord
from discord.ext import commands


class MemoryError(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["OOM", "OutOfMemory", "RAM", "Memory"])
    async def MemoryError(self, ctx):
        embed = discord.Embed(
            title = "MemoryError()",
            description = "Just means your PC ran out of memory (RAM).",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://media.discordapp.net/attachments/840336835166732290/919284493192429679/OOM.png")
        embed.set_footer(text="Try lowering your settings.") 
        await ctx.send(embed=embed) 


def setup(client):
    client.add_cog(MemoryError(client))