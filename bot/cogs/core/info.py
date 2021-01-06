import discord
import time
import datetime as dt
from humanize import naturaltime
from discord.ext import commands

from bot.bot import Bot
from bot.utils.checks import is_dev
from bot.utils.search import autoget
from bot.utils.embeds import MemberInfo, RoleInfo, UserInfo, ChannelInfo


class Info(commands.Cog):
    """A cog for getting info on various things"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.group(name="info", aliases=["lookup", "?"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(manage_messages=True), is_dev())
    async def lookup(self, ctx: commands.Context, *, item: str):
        item = item.strip("<>#&@!")
        if item.isnumeric():
            item = int(item)

        member = autoget(ctx.guild.members, item)
        if member:
            return await ctx.send(embed=MemberInfo(member))

        channel = autoget(ctx.guild.channels, item)
        if channel:
            return await ctx.send(embed=ChannelInfo(channel))

        role = autoget(ctx.guild.roles, item)
        if role:
            return await ctx.send(embed=RoleInfo(role))

        if type(item) == int:
            try:
                user = await self.bot.fetch_user(item)
                return await ctx.send(embed=UserInfo(user))
            except:
                pass

        await ctx.send(f"Lookup for {item} didnt return any results.")

    @commands.command(name="snowflake", aliases=["sf", "sfi", "sfinfo"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(manage_messages=True), is_dev())
    async def snowflake_info(self, ctx: commands.Context, snowflake: int):
        timestamp = (snowflake >> 22) + 1420070400000
        worker = (snowflake & 0x3E0000) >> 17
        process = (snowflake & 0x1F000) >> 12
        increment = snowflake & 0xFFF

        description = f"Timestamp: {timestamp}\nWorkerID: {worker}\nProcessID: {process}\nIncrement: {increment}\n\n"
        description += f"Creation Time: {naturaltime(dt.datetime.now() - dt.timedelta(seconds=int(time.time() - timestamp // 1000)))}"

        embed = discord.Embed(title="Snowflake Info", colour=0x87CEEB, description=description)
        await ctx.send(embed=embed)

    @commands.command(name="member", aliases=["memberinfo"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(manage_messages=True), is_dev())
    async def member_info(self, ctx: commands.Context, member: discord.Member = None):
        member = member if member else ctx.author
        await ctx.send(embed=MemberInfo(member))

    @commands.command(name="role", aliases=["roleinfo"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(manage_messages=True), is_dev())
    async def role_info(self, ctx: commands.Context, role: discord.Role):
        await ctx.send(embed=RoleInfo(role))

    @commands.command(name="channel", aliases=["channelinfo"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(manage_messages=True), is_dev())
    async def channel_info(self, ctx: commands.Context, channel: discord.TextChannel = None):
        channel = channel if channel else ctx.channel
        await ctx.send(embed=ChannelInfo(channel))

    @commands.command(name="user", aliases=["userinfo"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(manage_messages=True), is_dev())
    async def user_info(self, ctx: commands.Context, user: int):
        try:
            user = await self.bot.fetch_user(user)
            return await ctx.send(embed=UserInfo(user))
        except:
            return await ctx.send(f"Couldn't find that user.")


def setup(bot: Bot):
    bot.add_cog(Info(bot))