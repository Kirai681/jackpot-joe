import discord
from discord import Embed

from utils.embed.embed_builder import EmbedBuilder

from typing import Optional


class EmbedDirector:
    """
    A director class for predefined embeds.
    """

    def __init__(self) -> None:
        raise TypeError("This class cannot be instantiated.")

    @staticmethod
    def success(
        message: str,
        title: str = "Success",
        footer: Optional[str] = None,
        icon_url: Optional[str] = None,
    ) -> Embed:
        """
        Creates a success embed.

        Args:
            message (str): The message in the description field.
            title (str, optional): The title of the embed. Defaults to `Success`.
            footer (Optional[str]): The text of the footer. Defaults to None.
            icon_url (Optional[str]): The URL of the footer icon. Defaults to None.

        Returns:
            Embed: The success embed.
        """
        builder = EmbedBuilder(
            title=title,
            description=message,
            color=discord.Color.green(),
        )
        if footer:
            builder.set_footer(text=footer, icon_url=icon_url)
        return builder.build()

    @staticmethod
    def error(
        message: str,
        title: str = "Error",
        footer: Optional[str] = None,
        icon_url: Optional[str] = None,
    ) -> Embed:
        """
        Creates an error embed.

        Args:
            message (str): The message in the description field.
            title (str, optional): The title of the embed. Defaults to `Error`.
            footer (Optional[str]): The text of the footer. Defaults to None.
            icon_url (Optional[str]): The URL of the footer icon. Defaults to None.

        Returns:
            Embed: The error embed.
        """
        builder = EmbedBuilder(
            title=title,
            description=message,
            color=discord.Color.red(),
        )
        if footer:
            builder.set_footer(text=footer, icon_url=icon_url)
        return builder.build()
