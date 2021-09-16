import logging
from typing import Dict, Union

import discord


# consistency with the `discord` namespaced logging
log = logging.getLogger(__name__)

# default timeout parameter for menus in seconds
DEFAULT_TIMEOUT = 180.0

# type definition for the keyword-arguments that are
# used in both Message.edit and Messageable.send
SendKwargsType = Dict[str, Union[str, discord.Embed, None]]

# type definition for possible page formats
PageFormatType = Union[str, discord.Embed, SendKwargsType]

# type definition for emoji parameters
EmojiType = Union[str, discord.Emoji, discord.PartialEmoji]
