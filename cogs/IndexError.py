import discord
from discord.ext import commands
import asyncio


class IndexError(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["ListOutOfRange", "OutOfRange", "Failed", "FailedReplay"])
    async def IndexError(self, ctx):
        embed = discord.Embed(
            title = "IndexError('list index out of range')",
            description = "This is mostly related with failed replays, unfortunately osr2mp4 does not have an appropriate support for it, if you want to render a failed replay, reduce the end-time to the moment where you failed (the end-time is measured in seconds).",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_footer(text="React the ➡️ to see a gif of how you can achieve this fix.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840721171578486794/indexerror.png") 
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("⬅️")
        await msg.add_reaction("➡️")
        
        def check_left(reaction, user):
            return user.id == ctx.message.author.id and str(reaction.emoji) == "➡️"
        def check_right(reaction, user):
            return user.id == ctx.message.author.id and str(reaction.emoji) == "⬅️"
        
        while True:          
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check_left)
            except asyncio.TimeoutError:
                await msg.remove_reaction("⬅️", self.client.user)
                await msg.remove_reaction("➡️", self.client.user)
                break
            else:
                #imgur because better than that fucking ugly gif          
                await msg.edit(content="https://imgur.com/CK0Bs1H", embed=None)
                try: 
                    reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check_right)
                except asyncio.TimeoutError:
                    await msg.remove_reaction("⬅️", self.client.user)
                    await msg.remove_reaction("➡️", self.client.user)
                    break
                else:
                    await msg.edit(content=None, embed=embed)


def setup(client):
    client.add_cog(IndexError(client))