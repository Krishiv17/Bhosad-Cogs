from redbot.core import commands

class RoleUnlocking(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def unlock1(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
