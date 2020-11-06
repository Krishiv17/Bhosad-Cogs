from redbot.core import commands


class BhosadUtils(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def lock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """Unlocks Channel for Level 5"""
        # Your code will go here
        await ctx.send("Locked channel for Level 5 Role")
