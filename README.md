
<div align="center">
    <h2>Simple Telegram logging with zero dependencies!</h2>
    <a href="https://pypi.org/project/telegram-logging/"><img src="https://badgen.net/pypi/v/telegram-logging/"></a>
    <a href="https://pypi.org/project/telegram-logging/"><img src="https://img.shields.io/pypi/dm/telegram-logging.svg"></a>
    <img src="https://github.com/lbltavares/telegram-logging/actions/workflows/python-publish.yml/badge.svg?branch=main">
</div>

<div align="center">
    <img src="https://user-images.githubusercontent.com/34322384/142266595-7b98a832-cd1e-4ff4-a1b7-2df8d7010289.png">
</div>

## Usage:

➡️ See a full example in [examples/usage.py](https://github.com/lbltavares/telegram-logging/blob/main/examples/usage.py">examples/usage.py)

[🤖 How to create a Telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

### Install:

```
pip install telegram-logging
```

### Import:

```
from telegram_logging import TelegramHandler, TelegramFormatter
```

### Create a Formatter and a Handler:
```
formatter = TelegramFormatter(
    fmt="[%(asctime)s %(name)s] %(levelname)8s\n\n%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    use_emoji=True)

handler = TelegramHandler(
    token="<Your bot token>",
    chat_id="<Your chat id>")

handler.setFormatter(formatter)
```
*You can get a list of all available handler params [here](https://core.telegram.org/bots/api#sendmessage)*

### Use it:

```
import logging

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


logger.info("Hi, here is some information")
```

## Emojis:

These are the default emojis:

* ⚪️ DEBUG 
* 🔵 INFO 
* 🟠 WARNING
* 🔴 ERROR
* 🔥 CRITICAL
 
You can customize them however you want:

<img style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)" src="https://user-images.githubusercontent.com/34322384/142038851-7ed8cf04-df2c-4705-8066-6e21e817d186.gif">


```
formatter = TelegramFormatter(
    ...
    use_emoji=True,
    emoji_map={
        logging.DEBUG: "🐛",
        logging.INFO: "💡",
        logging.ERROR: "🚨",
    }
)
```

## Notifications:

You can disable telegram notification below certain logging level (https://core.telegram.org/bots/api#sendmessage). 
```
formatter = TelegramFormatter(
    ...
    notification_level=logging.WARNING
)
```
This will disable notification for all logs below `WARNING` level (`DEBUG` and `INFO` will be silently delivered.)