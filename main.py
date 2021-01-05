from bot.bot import run

run([
    "jishaku",
    "bot.cogs.utility.general",
    "bot.cogs.core.weather",
    "bot.cogs.core.info"
], debug=False)
