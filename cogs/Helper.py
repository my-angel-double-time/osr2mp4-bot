import os
import discord
from discord.ext import commands
from constants import GENERAL_VERSION


class Helper(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def Help(self, ctx):
        temp = getHelpList(self)
        helpList = []
        helpText = ""
          
        #I hate this 
        for x in temp:
            helpList.append(str(x))                 
        for command in sorted(helpList):
            helpText += f"`{command}` "
             
        embed = discord.Embed(
            title = "osr2mp4 Command List",
            description = "Here you can see all the available commands.",
            colour = discord.Color.from_rgb(234, 84, 247)
        )
        embed.set_footer(text= f"osr2mp4 bot {GENERAL_VERSION} created by My Angel Double Time") 
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840336835166732290/840336859720056862/OsrLogo.png")
        embed.add_field(name="Usage: o! <command>", value="replace the <command> by some of the commands listed here to get a full explanation.\n`[e.g. o!FOURCC]`\n\nThe commands are **case insensitive ** also, there is no difference in typing `o!MemoryError` or `o!memoryerror`\n\nUse `o!aliases` to display a list of alternative names for a command.", inline=True)
        embed.add_field(name="osr2mp4 Commands:", value=helpText, inline=False)
        embed.add_field(name="Other Commands:", value="`Aliases`", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/840336835166732290/918992004728365056/help.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def Aliases(self, ctx):
        helpList = getHelpList(self)
        commandName = aliases = commandAliases = ""
        aliasesList = []
        
        for command in helpList:
            if command.aliases:
                commandName = f"**{command}:**"
                aliases = " | ".join(command.aliases)        
            aliasesList.append(f"\n{commandName}\n `{aliases}`\n")        
        aliasesList = set(aliasesList)
        
        #Sorting for a consistent order.       
        for x in sorted(aliasesList):
            commandAliases += x
            
        embed = discord.Embed(
            title = "Command Aliases",
            description = "All the available aliases for the osr2mp4 commands (if a command is not showing up here, it does not have an alias). \n\nAliases are also **case insensitive**." +
            "\n\n**[Aliases]**\n" + f"{commandAliases}",
            colour = discord.Color.from_rgb(234, 84, 247)
        )
        await ctx.send(embed=embed)





def getHelpList(self):
    client = self.client
    blackList = [commands.Bot.get_command(client,"Aliases"), commands.Bot.get_command(client,"Restart"), commands.Bot.get_command(client, "Reload"), commands.Bot.get_command(client, "Ban"), commands.Bot.get_command(client, "Clear"), commands.Bot.get_command(client, "Help")]
    commandList = []

    for x in self.client.commands:
        commandList.append(x) 
        
    return [i for i in commandList if i not in blackList]   
        
def setup(client):
    client.add_cog(Helper(client))   
        