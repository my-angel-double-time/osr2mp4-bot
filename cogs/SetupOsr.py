import discord
from discord.ext import commands


class SetupOsr(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["SelectPaths", "OsuFolder"])
    async def SettingPaths(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/840336835166732290/919291751410319371/setting_osr2mp4_up.mp4")
        

def setup(client):
    client.add_cog(SetupOsr(client))