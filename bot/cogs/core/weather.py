from py_owm import Weather
from discord.ext import commands
from pathlib import Path
from random import choice

from bot.bot import Bot
from bot.utils.weather import format_weather

with Path("./data/cities.txt").open() as f:
    cities = [city.strip() for city in f.readlines()]


class Weather(commands.Cog):
    """A cog for getting the weather."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="weather")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def weather(self, ctx: commands.Context, location: str = None):
        try:
            location = choice(cities) if not location else location
            w = await self.bot.weather.get_by_name(location)
        except:
            return await ctx.send("That's not a valid location!")

        await ctx.send(format_weather(w))


def setup(bot: Bot):
    bot.add_cog(Weather(bot))
