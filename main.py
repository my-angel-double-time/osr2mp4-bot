import os
import asyncio
import discord
from discord.ext import commands

#Load Bot Tokens
from constants import *

intents = discord.Intents.default()
intents.members = True

bot_token = OSR2MP4_TOKEN 
prefix = None

if bot_token == OSR2MP4_TOKEN:
    prefix = "o!"
elif bot_token == NATSUMI_TOKEN:
    prefix = "!"
else:
    prefix = "o@"
    
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
client.remove_command('Help')

#where cogs are firstly stored
initial_extensions = []

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    print("----------------------------")
    print("osr2mp4 bot initialized.")
    print(f"Client Running As: {client.user}")
    print("----------------------------")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{prefix}help"))
    clearConsole()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send (f"Command not found, type `{prefix}help` to get a list of the available commands.")
        


#Loading cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])



if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)
        
@client.command()
async def Reload(ctx):
    if (ctx.author.id != OWNER):
        embed = discord.Embed(
            description = "⚠️ This is a bot owner command.",
            colour = discord.Color.from_rgb(255,84,84)
        )      
        await ctx.send(embed=embed)
        return
    
    embed = discord.Embed(
        description = "Reloading Commands! 👍",
        colour = discord.Color.from_rgb(255,255,84)
    )      
    message = await ctx.send(embed=embed)
    
    for extension in initial_extensions:
        client.unload_extension(extension)
        client.load_extension(extension)
     
    await asyncio.sleep(1)
    embed_r = discord.Embed(
        description = "Commands Reloaded! 👌",
        colour = discord.Color.from_rgb(84,255,84)
    )       
    await message.edit(embed=embed_r)  
    print("Reloading...")
    clearConsole()
    
   

    
    

client.run(bot_token)
