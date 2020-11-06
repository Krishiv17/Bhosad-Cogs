from redbot.core import commands


class BhosadUtils(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def lock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """Locks Channel for Level 5"""
        await ctx.send("Locked channel for Level 5 Role")
    async def lock10(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """Locks Channel for Level 10"""
        await ctx.send("Locked channel for Level 10 Role")
    async def lock15(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """Locks Channel for Level 15"""
        await ctx.send("Locked channel for Level 15 Role")


