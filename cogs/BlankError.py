import discord
import asyncio
from discord.ext import commands


class BlankError(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["NoDescError", "Dumb_Error", "Skin", "Empty", "Audio"])
    async def BlankError(self, ctx):
        embed = discord.Embed(
            title = "No Description Error / Blank Error",
            description = "You are using a skin with empty audio data.",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840336835166732290/840691701244100638/dumberror1.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/840691703106371594/dumberror2.png")
        embed.add_field(name="Fix:", value="Download [this python file](https://cdn.discordapp.com/attachments/840336835166732290/920846423946317884/CreateAudio.py) and replace on `osr2mp4\libs\pythonlib\Lib\site-packages\osr2mp4\AudioProcess` directory, after that, you can try rendering again." 
                                    + "\n"+"It also applies to the error below since they are the same, just displayed differently.", inline=False)
        embed.set_footer(text="React the ➡️ to see a gif of how you can achieve this fix.") 
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
                gif = discord.Embed(
                title = "No Description Error / Blank Error",
                colour = discord.Color.from_rgb(234, 84, 247) 
                )
                gif.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/920885817273122866/BlankError_FIX.gif")        
                await msg.edit(embed=gif)
                try: 
                    reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check_right)
                except asyncio.TimeoutError:
                    await msg.remove_reaction("⬅️", self.client.user)
                    await msg.remove_reaction("➡️", self.client.user)
                    break
                else:
                    await msg.edit(content=None, embed=embed)
        

def setup(client):
    client.add_cog(BlankError(client))