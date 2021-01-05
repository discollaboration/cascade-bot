import discord
from discord.ext import commands
from vcoutils import generate_id_solid
from pathlib import Path

from bot.bot import Bot
from bot.utils.checks import is_dev
from bot.utils.aiotts import AIOTTS

Path("./tmp").mkdir(exist_ok=True)


class Moderation(commands.Cog):
    """A cog for moderation"""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.tts = AIOTTS()

    @commands.command(name="ban", aliases=["yeet"])
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(ban_members=True), is_dev())
    async def lookup(self, ctx: commands.Context, member: discord.Member, *, reason: str = None):
        if not reason:
            return await ctx.send(f"You must provide a ban reason.")
        bid = generate_id_solid(8)
        await self.tts.request(reason, f"./tmp/{bid}.wav")
        await member.send(f"You have been banned from the guild {ctx.guild}, reason:", file=discord.File(f"./tmp/{bid}.wav", filename="reason.wav"))


def setup(bot: Bot):
    bot.add_cog(Moderation(bot))