import discord
from discord.ext import commands

from dotenv import load_dotenv

import os

load_dotenv()

PREFIX = "?"
TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("'TOKEN' is not set.")
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("'DATABASE_URL' is not set.")


class Bot(commands.Bot):
    """
    A modular Discord bot.
    """

    def __init__(self) -> None:
        """
        Initializes the bot with specified command prefix and enables all intents.
        """
        intents = discord.Intents.all()
        super().__init__(command_prefix=PREFIX, intents=intents)

    async def on_ready(self) -> None:
        """
        Called when bot successfully connects and is ready to operate.
        """
        assert self.user is not None
        print(f"Bot logged in as {self.user.name}.")

    async def setup_hook(self) -> None:
        """
        Called before 'on_ready'.
        """
        for dirpath, _, filenames in os.walk("./bot/cogs"):
            for filename in filenames:
                if not filename.startswith("_") and filename.endswith(".py"):
                    try:
                        relative_path = os.path.relpath(
                            os.path.join(dirpath, filename),
                            "./bot",
                        )
                        cog_path = relative_path.replace(
                            os.sep,
                            ".",
                        ).removesuffix(".py")

                        await self.load_extension(cog_path)
                        print(f"Loaded cog '{filename[:-3]}'.")
                    except Exception as e:
                        print(f"Error while loading cog '{filename[:-3]}': {e}")


if __name__ == "__main__":
    bot = Bot()
    bot.run(TOKEN)
