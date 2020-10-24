import asyncio
import logging
from datetime import datetime
from os.path import exists
from typing import Optional, Union

import discord
from redbot.core import Config, checks, commands
from redbot.core.commands import Greedy
from redbot.core.utils.chat_formatting import box, pagify
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu

BaseCog = getattr(commands, "Cog", object)



class RoleUtils(commands.Cog):
    """My custom cog"""

def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=694206942165)

        default_guild = {
            "role1": [],           
        }

        self.config.register_guild(**default_guild)
        self.log = logging.getLogger("red.Bhosad-Cogs.roleutils")

    async def red_delete_data_for_user(self, **kwargs):
        """This cog does not store user data"""
        return

    @commands.command()
    @commands.guild_only()
    @checks.mod_or_permissions(manage_channels=True)
    @checks.bot_has_permissions(manage_channels=True)
    async def lock5(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.get_role(get_role1), send_messages=False)
        
        await ctx.send("Locked channel for"get_role1)

    @commands.group(aliases=["lds"])
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    @checks.bot_has_permissions(embed_links=True)
    async def roleset(self, ctx: commands.Context):
        """
        Settings for roles
        """
        pass
    @lockdownset.command(name="showsettings")
    async def show_settings(self, ctx: commands.Context):
        """See Guild Configuration"""
        get_role1 = fetch_all["role1"]

    @lockdownset.command(name="roles")
    async def setrole1(self, ctx: commands.Context, *, role: discord.Role):
        """
        Add a role to lock from sending messages instead of the @everyone role
        Make sure to add the channels that are applicable
        """
        if not role:
            return await ctx.send_help()

        

        guild = ctx.guild
        nondefault = await self.config.guild(guild).nondefault()
        get_role1 = await self.config.guild(guild).role1()
        if get_role1:
            await ctx.send(f"You want to change <@&{get_role1}> to {role.mention}? `[yes|no]`")
            try:
                confirm_change = await ctx.bot.wait_for("message", check=check, timeout=30)
                if confirm_change.content.lower() != "yes":
                    return await ctx.send(
                        f"Looks like we will keep <@&{get_role}> as your role 1."
                    )
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply!")

        await self.config.guild(guild).role1.set(role.id)
        await ctx.send(f"Added {role.mention} as role1")
        spec_chans = await self.config.guild(guild).role1()
        if nondefault is False:
            if spec_chans:
                await self.config.guild(guild).nondefault.set(value=True)
            else:
                return await ctx.send(
                    "Make sure you set up your channels for this role by doing `{}lds asc <..channels..>`".format(
                        ctx.prefix
                    )
                )
