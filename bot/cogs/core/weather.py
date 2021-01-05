from py_owm import Weather
from discord import Member
from discord.ext import commands
from pathlib import Path
from random import choice

from bot.bot import Bot

with Path("./data/cities.txt").open() as f:
    cities = [city.strip() for city in f.readlines()]

def format_weather(w: Weather):
    data = f"In {w.name}, {w.sys['country']} it's {w.get_human_weather()},\n"
    data += f"the temperature is {round(w.temp - 273.15, 3)}C, the humidity is {w.humidity},\n"
    data += f"and the wind speed is {round(w.wind['speed'], 3)} mph."
    return data


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
