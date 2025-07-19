import asyncio
from disnake.ext import commands
from disnake import Intents

from core.configuration import BOT_TOKEN


async def main() -> None:
    bot = commands.InteractionBot(
        intents=Intents.all(),
    )
    bot.run(BOT_TOKEN)


# asyncio.run(main())
print("Hello, World!")
