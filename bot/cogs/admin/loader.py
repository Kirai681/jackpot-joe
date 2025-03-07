from discord.ext import commands

import os

from typing import Optional


class Loader(commands.Cog):
    """
    Handles dynamic loading, unloading and reloading of other cogs.

    Attributes:
        bot (commands.Bot): The instance of the bot loading the cog.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """
        Initializes the Loader cog.

        Args:
            bot (commands.Bot): The instance of the bot loading the cog.
        """
        self.bot = bot

    def find_cog_file(self, cog_name: str) -> Optional[str]:
        """
        Search for a cog file by its name.

        Args:
            cog_name (str): The name of the cog to search for.

        Returns:
            str or None: The path to the cog file as a module string (e.g. cogs.admin)
                if found, or None if the file doesn't exist.
        """
        for dirpath, _, filenames in os.walk("./bot/cogs"):
            for filename in filenames:
                if filename.startswith(cog_name.lower()) and filename.endswith(".py"):
                    relative_path = os.path.relpath(
                        os.path.join(dirpath, filename),
                        "./bot",
                    )
                    cog_path = relative_path.replace(
                        os.sep,
                        ".",
                    ).removesuffix(".py")
                    return cog_path
        return None

    @commands.command(name="load", help="Loads a specific cog into the bot.")
    async def load(
        self,
        ctx: commands.Context,
        cog: str = commands.parameter(
            description="The name of the cog to load.",
        ),
    ) -> None:
        """
        Loads a specified cog into the bot if it isn't already loaded.

        Args:
            ctx (commands.Context): The context of the invoked command.
            cog (str): The name of the cog to load.
        """
        await ctx.send(self.find_cog_file(cog))


async def setup(bot: commands.Bot) -> None:
    """
    Asynchronously loads the cog into the bot.

    Args:
        bot (commands.Bot): The instance of the bot loading the cog.
    """
    await bot.add_cog(Loader(bot))
