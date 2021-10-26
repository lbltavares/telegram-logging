# telegram-logging

A simple Telegram logging module with Handler and Formatter.

https://pypi.org/project/telegram-logging/0.14/

## Usage:

### Import:

```
from telegram_logging import TelegramHandler, TelegramFormatter
```


### Handler:
```
TelegramHandler( token="<Your bot token>",
                    chat_id="<Your chat id>",
                    parse_mode="HTML")
```
*You can get a list of all available params here: https://core.telegram.org/bots/api#sendmessage

### Formatter:
```
TelegramFormatter(
    fmt="[%(asctime)s %(name)s] %(levelname)8s\n\n%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    use_emoji=True
)
```

### Emojis:

- ⚪️ = DEBUG 
- 🔵 = INFO 
- 🟠 = WARNING
- 🔴 = ERROR
- 🔥 = CRITICAL

You can also use your own set of emojis:

```
TelegramFormatter(
    fmt="[%(asctime)s %(name)s] %(levelname)8s\n\n%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    use_emoji=True,
    emojis={
        logging.DEBUG:    "🐛",
        logging.INFO:     "💬",
        logging.WARNING:  "❕",
        logging.ERROR:    "🚨",
        logging.CRITICAL: "🔥"
    }
)
```
