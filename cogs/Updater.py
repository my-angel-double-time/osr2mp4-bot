import os
import sys
import discord
import requests

from pathlib import Path
from discord.ext import commands
from zipfile import ZipFile
from constants import DISCORD_URL, ZIP_FILE, OWNER


class Updater(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["update"])
    async def Restart(self, ctx, update, updateID = None):
        if ctx.author.id == OWNER:
            await ctx.send("Alright...")
            await ctx.send("<:peppyBorgor:738686633003581510>")
            if (update.casefold() == "-u") and updateID != None:
                await restart_bot(ctx, updateID)
            else:
                await restart_bot()             
        else:
            embed = discord.Embed(
                description = "⚠️ This is a bot owner command.",
                colour = discord.Color.from_rgb(255,84,84)
            )      
            await ctx.send(embed=embed)
            


async def restart_bot(ctx = None, updateID = None):
    if updateID != None:
        await installUpdate(ctx, updateID)

    print("Restarting...")        
    os.execv(sys.executable, ['python'] + sys.argv)



async def installUpdate(ctx, updateID):
    full_url = DISCORD_URL + updateID + '/' + ZIP_FILE
    
    path = os.path.join(Path(__file__).parents[1], ZIP_FILE)
    response = requests.get(full_url)
    print("Downloading Update...")
    
    if response.ok:
        try:
            with open(str(path), 'wb') as file:
                file.write(response.content)
        except Exception as e:
            print(e)
    else:
        await ctx.send(response.text);
                    
    if os.path.exists(path):
        try:
            with ZipFile(path, 'r') as zip_ref:
                #since we are not in the main.py we need to go back one directory in the directory tree 
                #[osr2mp4-bot/cogs/] -> [osr2mp4-bot/]"
                zip_ref.extractall(str(Path(__file__).parents[1]))
            os.remove(path)
        except Exception as e:
            print(e)


def setup(client):
    client.add_cog(Updater(client))