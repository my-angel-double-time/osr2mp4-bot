import discord
import datetime
from discord.ext import commands


#this is so retard i know
memberCount  = 0
firstUserTime = None
alreadyWarned = False
memberList = []

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
            
        
    #Attempt to detecting/warning about raids   
    @commands.Cog.listener()
    async def on_member_join(self, member):
        global memberCount, firstUserTime, alreadyWarned, memberList
    
        memberList.append(member)
        memberCount += 1
    
        if firstUserTime == None:
            #Time when the first user joined
            firstUserTime = datetime.datetime.now()
        
        await resetCounter()
       
        if memberCount > 9 and alreadyWarned == False:
            channel = self.client.get_channel(731852409432965140)#change to osr2mp4 channel  (mute-me channel id: 731852409432965140)
            await channel.send("<@&733833040991748128> The fuck man, there is probably some retards in the server\n(`{}` users joined the server in the last 60 seconds, possibly raid warning!)".format(memberCount))
            await channel.send("<@210422953907585036> Wake up!, mother fucker.")
            await channel.send("If you want me to ban them, use `o!ban` (without any argument, this command will only work in a time span of 60 seconds")
            alreadyWarned = True
         
                        
    @commands.command(aliases=["prune", "purge"])
    @commands.has_permissions(manage_messages=True)
    async def Clear(self, ctx, amount : int):
        if amount < 1 or amount > 1000:
            await ctx.send(f"You cannot clear `{amount}` messages.")
            return
            
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send (f"`{amount}` messages has been deleted.", delete_after=5)
    @Clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
            await ctx.send ("Please specify the number of messages to clear `e.g. o!clear 20`")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")
            
    @commands.command(aliases=["bonk"])
    @commands.has_permissions(ban_members=True)     
    async def Ban(self, ctx, user: discord.Member = None, *, reason=None):
        global memberList
        if ctx.channel.id != 731852409432965140:#change to osr2mp4 channel  (mute-me channel id: 731852409432965140)
            if user is None:
                await ctx.send("Please mention someone to ban!")
            if reason is None:
                reason = "Reason was not specified."
            await user.ban(reason=reason)
            embed = discord.Embed(
                      title = f"{user} Banned!",
                      description = f"Reason: {reason}",
                      colour = discord.Color.from_rgb(255, 84, 84)
                 )
            await ctx.send(embed=embed)
        else:
            nUsers = len(memberList)
            if nUsers > 9:
                for m in memberList:
                    await m.ban(reason=reason)   
                await ctx.send("`{}` Users Banned!".format(nUsers), delete_after=3)
            else:
                if user is None:
                    await ctx.send("The operation has timed out.\n(are you trying to ban someone? Use `o!ban @usermention` instead).")
                if reason is None:
                    reason = "Reason was not specified."
                await user.ban(reason=reason)
                await ctx.send("`{}` Banned!".format(user), delete_after=3)
    @Ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")
  
  
  
            
async def resetCounter():
        global memberCount, firstUserTime, alreadyWarned, memberList
   
        currentTime = datetime.datetime.now()
        difference = currentTime - firstUserTime
    
        #It has been timed out, let's reset the global variables to their default values.
        if difference.seconds > 60:
            memberCount = 0
            firstUserTime = None
            alreadyWarned = False
            memberList = []
            
def setup(client):
    client.add_cog(Moderation(client))