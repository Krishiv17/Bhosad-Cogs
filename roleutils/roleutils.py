from redbot.core import commands

class RoleUtils(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def lock1(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
