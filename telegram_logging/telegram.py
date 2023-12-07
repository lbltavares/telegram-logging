"""A simple Telegram logging module with Handler and Formatter.
"""

import logging
import requests


class TelegramFormatter(logging.Formatter):
    """TelegramFormatter.
    """

    EMOJI_MAP = {
        logging.DEBUG: "\u26aa",
        logging.INFO: "\U0001f535",
        logging.WARNING: "\U0001F7E0",
        logging.ERROR: "\U0001F534",
        logging.CRITICAL: "\U0001f525",
    }

    def __init__(self,
                 fmt: str = '%(asctime)s - %(levelname)s - %(message)s',
                 datefmt: str = None,
                 use_emoji: bool = True,
                 emoji_map: dict = None):
        """:fmt: str, default: '%(asctime)s - %(levelname)s - %(message)s'\n
        :datefmt: str, default: None\n
        :use_emoji: bool, default: True\n
        :emoji_map: dict, default: None\n
        """
        super().__init__(fmt, datefmt)
        self.use_emoji = use_emoji
        self.emojis = self.EMOJI_MAP
        if emoji_map:
            self.emojis.update(emoji_map)

    def format(self, record):
        if self.use_emoji and record.levelno in self.emojis:
            record.levelname = self.emojis[record.levelno]
        return super().format(record)


class TelegramHandler(logging.Handler):
    """Send log messages to Telegram.
    https://core.telegram.org/bots/api#sendmessage
    """
    def __init__(self,
                 bot_token: str,
                 chat_id: str,
                 timeout: int = 5,
                 notification_level=logging.DEBUG,
                 **params):
        """:bot_token: Telegram bot_token\n
        :chat_id: Telegram chat_id\n
        :timeout: Timeout for Telegram API call\n
        :notification_level: logging level below which notification will be disabled\n
        :params: https://core.telegram.org/bots/api#sendmessage
        """
        logging.Handler.__init__(self)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.timeout = timeout
        self.kwargs = params
        self.kwargs["parse_mode"] = "HTML"
        self.notification_level = notification_level

    def emit(self, record):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": self.format(record),
        }
        if(record.levelno < self.notification_level):
            params['disable_notification'] = True
        params.update(self.kwargs)
        try:
            resp = requests.get(url, params=params, timeout=self.timeout)
        except Exception as e:
            print(f"Exception in sending TG msg. Exception: {e}")
