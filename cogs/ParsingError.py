import discord
import asyncio
from discord.ext import commands


class ParsingError(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["Skinerror", "Skin.ini", "Skinini"])
    async def ParsingError(self, ctx):
        embed = discord.Embed(
            title = "Source contains parsing errors",
            description = "If your error looks like the image below it is mostly related to custom ''skin.ini'' file. \n\n"+
    		"To fix that go to your skin.ini (it is located inside of your skin folder)" + 
    		" and make the format (not the values) [look like this.](https://cdn.discordapp.com/attachments/840336835166732290/840717816436228106/correct_skin.ini_format.png)",
            colour = discord.Color.from_rgb(234, 84, 247) 
        )
        embed.set_image(url="https://media.discordapp.net/attachments/840336835166732290/840718192044933141/skinshit.png"),
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
                await msg.edit(content="https://cdn.discordapp.com/attachments/840336835166732290/919293752676352090/ParsingError_FIX.mp4", embed=None)
                try: 
                    reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check_right)
                except asyncio.TimeoutError:
                    await msg.remove_reaction("⬅️", self.client.user)
                    await msg.remove_reaction("➡️", self.client.user)
                    break
                else:
                    await msg.edit(content=None, embed=embed)


def setup(client):
    client.add_cog(ParsingError(client))