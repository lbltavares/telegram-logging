# -*- coding: utf-8 -*-
""" telegram-logging usage example
"""

import logging
from telegram_logging import TelegramFormatter, TelegramHandler

formatter = TelegramFormatter(
    fmt="[%(asctime)s %(name)s] %(levelname)8s\n\n%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    use_emoji=True,
    # (Optional) If you want to use custom emojis:
    emoji_map={
        logging.DEBUG: "🐛",
        logging.INFO: "💡",
        logging.ERROR: "🚨",
    })

handler = TelegramHandler(bot_token="<Your Telegram Bot Token>",
                          chat_id="<Your Telegram Chat ID>")

handler.setFormatter(formatter)

_log = logging.getLogger(__name__)
_log.addHandler(handler)
_log.setLevel(logging.DEBUG)


def main():
    _log.debug("Debug message")
    _log.info("Info message")
    _log.warning("Warning message")
    _log.error("Error message")
    _log.critical("Critical message")


if __name__ == "__main__":
    main()
