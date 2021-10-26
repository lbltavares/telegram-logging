import logging


class TelegramFormatter(logging.Formatter):
    """
    TelegramFormatter.
    """

    EMOJI_MAP = {
        logging.DEBUG: "\u26aa",
        logging.INFO: "\U0001f535",
        logging.WARNING: "\U0001F7E0",
        logging.ERROR: "\U0001F534",
        logging.CRITICAL: "\U0001f525",
    }

    def __init__(self, fmt=None, datefmt=None, use_emoji=True, emojis=None):
        super().__init__(fmt, datefmt)
        self.use_emoji = use_emoji
        self.emojis = emojis or self.EMOJI_MAP

    def format(self, record):
        if self.use_emoji and record.levelno in self.emojis:
            record.levelname = self.emojis[record.levelno]
        return super().format(record)


class TelegramHandler(logging.Handler):
    """ 
    Envia registros de log pelo telegram: 
    https://core.telegram.org/bots/api#sendmessage
    """

    def __init__(self, token, chat_id, timeout=5, **params):
        """
        :token: token do bot do telegram\n
        :chat_id: id do chat do telegram\n
        :params: https://core.telegram.org/bots/api#sendmessage
        """
        logging.Handler.__init__(self)
        self.token = token
        self.chat_id = chat_id
        self.timeout = timeout
        self.kwargs = params

    def emit(self, record):
        from urllib import request, parse, error
        try:
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            params = {
                "chat_id": self.chat_id,
                "text": self.format(record),
            }
            params.update(self.kwargs)
            data = parse.urlencode(params).encode()
            # POST
            req = request.Request(url, data=data)
            request.urlopen(req, timeout=self.timeout)
        except error.URLError:
            pass
        except Exception as e:
            self.handleError(record)
