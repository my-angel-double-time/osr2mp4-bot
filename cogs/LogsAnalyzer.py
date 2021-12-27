import asyncio
import discord

from constants import keywords, samekeyvalues
from discord.ext import commands

class LogsAnalyzer(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        ctx = await self.client.get_context(message)
        
        if message.attachments:
            for i, file in enumerate(message.attachments):
                if message.attachments[i].filename.endswith(".log"):
                    log_text = await file.read()             
                    command = getcommand(log_text.decode("utf-8"))
                    
                    #await file.save("log.txt")
                    #with open("log.txt", 'rb') as f:
                    #   log_text = f.read()
                    #    command = getcommand(str(log_text))
                    
                    if command != None:
                        embed = discord.Embed(
                            title = "Possible issue found!",
                            description = f"✨At least one issue was found while reading logs\n\nShowing possible fix for:\n`{command}` in `{message.attachments[i].filename}`",
                            colour= discord.Color.from_rgb(255,255,84) 
                        )
                        await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        await ctx.invoke(self.client.get_command(command))
                        
                        #break the loop so we dont spam shit if theres the same keyword in another log
                        break
        else:
            command = getcommand(message.content)
            if command != None:
                embed = discord.Embed(
                    title = "Possible issue found!",
                    description = f"✨At least one issue was found while reading logs\n\nShowing possible fix for:\n`{command}`",
                    colour= discord.Color.from_rgb(255,255,84) 
                )
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.invoke(self.client.get_command(command))
                    
                
            


def getcommand(log_text):
    command = None  
    for i, key in enumerate(keywords):       
        #Each key is a list with 2 values, the string key and the string value, key[0] returns the key while key[1] returns the value
        if key[0] in log_text:
            command = "BlankError" if any(secondary_key in log_text for secondary_key in samekeyvalues) else keywords[i][1]        
    return command

def setup(client):
    client.add_cog(LogsAnalyzer(client))