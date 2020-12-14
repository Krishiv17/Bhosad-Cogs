import asyncio
from redbot.core import checks, commands


class BhosadUtils(commands.Cog):
    """Hehehe"""
    
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command()
    async def unlock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576062869012521), send_messages=True)
        """Unlocks Channel for Level 5"""
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Unlocked channel for Level 5 Role, Locking in 90 Seconds")
        await asyncio.sleep(85)
        await ctx.channel.set_permissions(ctx.guild.get_role(722576062869012521), send_messages=None)
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Locked channel for Level 5 Role")    
        
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command()
    async def unlock10(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576157664608266), send_messages=True)
        """Unlocks Channel for Level 10"""
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Unlocked channel for Level 10 Role, Locking in 90 Seconds")
        await asyncio.sleep(85)
        await ctx.channel.set_permissions(ctx.guild.get_role(722576157664608266), send_messages=None)
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Locked channel for Level 10 Role")   
        
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command()
    async def unlock15(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576225020674455), send_messages=True)
        """Unlocks Channel for Level 15"""
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Unlocked channel for Level 15 Role, Locking in 90 Seconds")
        await asyncio.sleep(85)
        await ctx.channel.set_permissions(ctx.guild.get_role(722576225020674455), send_messages=None)
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Locked channel for Level 10 Role")    
        
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command()
    async def unlock20(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576297003450368), send_messages=True)
        """Unlocks Channel for Level 20"""
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Unlocked channel for Level 20 Role, Locking in 90 Seconds")
        await asyncio.sleep(85)
        await ctx.channel.set_permissions(ctx.guild.get_role(722576297003450368), send_messages=None)
        await ctx.send("<a:a_VerifiedBlue:784282245828575282> Locked channel for Level 20 Role") 
    
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command()
    async def bunlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(755391896838471690), send_messages=True)
        await ctx.channel.set_permissions(ctx.guild.get_role(688660550753714196), send_messages=True)
        """Unlocks Channel for Boosters and Supporters"""
        await ctx.send("<a:nitro:785481730789474304> Unlocked channel for Boosters and HIGH5 Followers, Locking in 15 Seconds")
        await asyncio.sleep(15)
        await ctx.channel.set_permissions(ctx.guild.get_role(755391896838471690), send_messages=None)
        await ctx.channel.set_permissions(ctx.guild.get_role(688660550753714196), send_messages=None)
        await ctx.send("<a:nitro:785481730789474304> Locked Channel for Boosters and HIGH5 Followers, Good Luck") 
    
        
    
        
        
   


