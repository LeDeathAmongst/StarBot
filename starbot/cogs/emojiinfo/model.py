import json
from Star-Utils import Cog
import discord
from starbot.core import commands, data_manager


class PartialEmoji(discord.PartialEmoji):
    """Represents a "partial" emoji. Subclasses `discord.PartialEmoji`

    .. container:: operations

        .. describe:: x == y

            Checks if two emoji are the same.

        .. describe:: x != y

            Checks if two emoji are not the same.

        .. describe:: hash(x)

            Return the emoji's hash.

        .. describe:: str(x)

            Returns the emoji rendered for discord.

    Attributes
    -----------
    name: Optional[:class:`str`]
        The custom emoji name, if applicable, or the unicode codepoint
        of the non-custom emoji. This can be ``None`` if the emoji
        got deleted (e.g. removing a reaction with a deleted emoji).
    animated: :class:`bool`
        Whether the emoji is animated or not.
    id: Optional[:class:`int`]
        The ID of the custom emoji, if applicable.
    group: Optional[:class:`str`]
        The group name of the emoji if it is a native emoji.
    """

    def __init__(self, *, name: str, animated: bool = False, id: int | None = None, group: str | None = None, aliases: list | None = None) -> None: # pylint: disable=redefined-builtin
        super().__init__(name=name, animated=animated, id=id)
        self.group = group
        self.aliases = aliases

    @classmethod
    def from_str(cls, coginstance: Cog, value: str) -> "PartialEmoji":
        """Converts a Discord string representation of an emoji to a :class:`PartialEmoji`.

        The formats accepted are:

        - ``a:name:id``
        - ``<a:name:id>``
        - ``name:id``
        - ``<:name:id>``

        If the format does not match then it is assumed to be a unicode emoji.

        .. versionadded:: 2.0

        Parameters
        ------------
        value: :class:`str`
            The string representation of an emoji.

        Returns
        --------
        :class:`PartialEmoji`
            The partial emoji from this string.
        """
        match = cls._CUSTOM_EMOJI_RE.match(value)
        if match is not None:
            groups = match.groupdict()
            animated = bool(groups['animated'])
            emoji_id = int(groups['id'])
            name = groups['name']
            return cls(name=name, animated=animated, id=emoji_id)

        path: data_manager.Path = data_manager.bundled_data_path(coginstance) / "emojis.json"
        with open(path, "r", encoding="UTF-8") as file:
            emojis: dict = json.load(file)
        emoji_aliases = []
        emoji_group = None
        for dict_name, group in emojis.items():
            for k, v in group.items():
                if v == value:
                    emoji_group = dict_name
                    if k not in emoji_aliases:
                        emoji_aliases.append(k)
        return cls(name=value, animated=False, id=None, group=emoji_group, aliases=emoji_aliases)
