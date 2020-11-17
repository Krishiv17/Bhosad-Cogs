from redbot.core import commands


class BhosadUtils(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def lock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576062869012521), send_messages=False)
        """Locks Channel for Level 5"""
        await ctx.send("Locked channel for Level 5 Role")
    async def lock10(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576157664608266), send_messages=False)
        """Locks Channel for Level 10"""
        await ctx.send("Locked channel for Level 10 Role")
    async def lock15(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576225020674455), send_messages=False)
        """Locks Channel for Level 15"""
        await ctx.send("Locked channel for Level 15 Role")
     async def lock20(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(722576297003450368), send_messages=False)
        """Locks Channel for Level 20"""
        await ctx.send("Locked channel for Level 20 Role")
     async def lock30(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(730410382585495622), send_messages=False)
        """Locks Channel for Level 30"""
        await ctx.send("Locked channel for Level 30 Role")
      async def lock40(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(730410698932486195), send_messages=False)
        """Locks Channel for Level 40"""
        await ctx.send("Locked channel for Level 40 Role")


