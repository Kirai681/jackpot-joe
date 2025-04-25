from discord.ext import commands

import os

from typing import Optional

from utils.embed.embed_director import EmbedDirector


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
        try:
            cog_path = self.find_cog_file(cog)
            if not cog_path:
                raise commands.ExtensionNotFound(name=cog)
            await self.bot.load_extension(cog_path)
            embed = EmbedDirector.success(f"Successfully loaded cog `{cog}`.")
            await ctx.send(embed=embed)
        except commands.ExtensionAlreadyLoaded:
            embed = EmbedDirector.error(f"Cog `{cog}` is already loaded.")
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedDirector.error(f"Cog `{cog}` could not be found.")
            await ctx.send(embed=embed)
        except Exception as err:
            embed = EmbedDirector.error(f"Unexpected error: {err}")
            await ctx.send(embed=embed)

    @commands.command(name="unload", help="Unloads a specific cog from the bot.")
    async def unload(
        self,
        ctx: commands.Context,
        cog: str = commands.parameter(
            description="The name of the cog to unload.",
        ),
    ) -> None:
        """
        Unloads a specified cog from the bot if it is currently loaded.

        Args:
            ctx (commands.Context): The context of the invoked command.
            cog (str): The name of the cog to unload.
        """
        try:
            cog_path = self.find_cog_file(cog)
            if not cog_path:
                raise commands.ExtensionNotFound(name=cog)
            await self.bot.unload_extension(cog_path)
            embed = EmbedDirector.success(f"Successfully unloaded cog `{cog}`.")
            await ctx.send(embed=embed)
        except commands.ExtensionNotLoaded:
            embed = EmbedDirector.error(f"Cog `{cog}` isn't currently loaded.")
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedDirector.error(f"Cog `{cog}` could not be found.")
            await ctx.send(embed=embed)
        except Exception as err:
            embed = EmbedDirector.error(f"Unexpected error: {err}")
            await ctx.send(embed=embed)

    @commands.command(name="reload", help="Reloads a specific cog of the bot.")
    async def reload(
        self,
        ctx: commands.Context,
        cog: str = commands.parameter(
            description="The name of the cog to reload.",
        ),
    ):
        """
        Reloads a specified cog of the bot if it is currently loaded.

        Args:
            ctx (commands.Context): The context of the invoked command.
            cog (str): The name of the cog to reload.
        """
        try:
            cog_path = self.find_cog_file(cog)
            if not cog_path:
                raise commands.ExtensionNotFound(name=cog)
            await self.bot.reload_extension(cog_path)
            embed = EmbedDirector.success(f"Successfully reloaded cog `{cog}`.")
            await ctx.send(embed=embed)
        except commands.ExtensionNotLoaded:
            embed = EmbedDirector.error(f"Cog `{cog}` isn't currently loaded.")
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedDirector.error(f"Cog `{cog}` could not be found.")
            await ctx.send(embed=embed)
        except Exception as err:
            embed = EmbedDirector.error(f"Unexpected error: {err}")
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """
    Asynchronously loads the cog into the bot.

    Args:
        bot (commands.Bot): The instance of the bot loading the cog.
    """
    await bot.add_cog(Loader(bot))
