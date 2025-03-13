import discord

from typing import Optional
from typing import Self


class EmbedBuilder:
    """
    Makes creating Embeds a bit cleaner in code.

    Attributes:
        embed (discord.Embed): The Embed being built.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        color: discord.Color = discord.Color.blurple(),
    ) -> None:
        """
        Initializes the builder.

        Args:
            title (Optional[str]): The title of the embed. Defaults to None.
            description (Optional[str]): The description of the embed. Defaults to None.
            color (discord.Color): The color of the embed. Defaults to `discord.Color.blurple()`.
        """
        self.embed = discord.Embed(title=title, description=description, color=color)

    def set_author(self, name: str, icon_url: Optional[str] = None) -> Self:
        """
        Set the author of the embed.

        Args:
            name (str): The name of the author.
            icon_url (Optional[str]): The URL of the author's icon. Defaults to None.

        Returns:
            Self: The EmbedBuilder instance.
        """
        self.embed.set_author(name=name, icon_url=icon_url)
        return self

    def set_footer(self, text: str, icon_url: Optional[str]) -> Self:
        """
        Set the footer of the embed.

        Args:
            text (str): The footer text.
            icon_url (Optional[str]): The URL of the footer icon. Defaults to None.

        Returns:
            Self: The EmbedBuilder instance.
        """
        self.embed.set_footer(text=text, icon_url=icon_url)
        return self

    def add_field(self, name: str, value: str, inline: bool = True) -> Self:
        """
        Add a field to the embed.

        Args:
            name (str): The name of the field.
            value (str): The value of the field.
            inline (bool): Whether the field should be inline. Defaults to True.

        Returns:
            Self: The EmbedBuilder instance.
        """
        self.embed.add_field(name=name, value=value, inline=inline)
        return self

    def build(self) -> discord.Embed:
        """
        Finalize and return the constructed embed.

        Returns:
            discord.Embed: The constructed embed.
        """
        return self.embed
