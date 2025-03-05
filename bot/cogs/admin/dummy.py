from discord.ext import commands


class Dummy(commands.Cog):
    """
    A placeholder (dummy) cog for testing purposes.

    This cog serves as a template for new cogs. It doesn't implement any
    commands or listeners but ensures that the bot can successfully load cogs.

    Attributes:
        bot (commands.Bot): The instance of the bot loading the cog.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """
        Initializes the Dummy cog.

        Args:
            bot (commands.Bot): The instance of the bot loading the cog.
        """
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    """
    Asynchronously loads the cog into the bot.

    Args:
        bot (commands.Bot): The instance of the bot loading the cog.
    """
    await bot.add_cog(Dummy(bot))
