from bot.bot import run

run([
    "jishaku",
    "bot.cogs.utility.general",
    "bot.cogs.core.weather",
    "bot.cogs.core.info",
    "bot.cogs.core.mod"
], debug=False)
