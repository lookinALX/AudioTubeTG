import config
import asyncio
from bot import bot

if __name__ == "__main__":
    TOKEN = config.token
    bot = bot.TelegramBot(TOKEN)
    asyncio.run(bot.run())
