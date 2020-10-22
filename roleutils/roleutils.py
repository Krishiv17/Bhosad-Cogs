from redbot.core import commands

class RoleUtils(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def lock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def lock10(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def lock15(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def lock20(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def unlock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def unlock10(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def unlock15(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
    async def unlock20(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(763959609169674250), send_messages=False)
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Locked channel for <@&763959609169674250>")
