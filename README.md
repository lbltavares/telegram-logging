# telegram-logging

Simple Telegram logging with zero dependencies!

https://pypi.org/project/telegram-logging/

<div align="center">
    <img src="https://user-images.githubusercontent.com/34322384/142000274-8de885b7-b16d-4d77-b861-38ec9a35afef.png">
</div>

## Usage:
➡️ See a full example in [examples/usage.py](https://github.com/lbltavares/telegram-logging/blob/main/examples/usage.py)

🤖 [How to create a Telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

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
*You can get a list of all available handler params [here](https://core.telegram.org/bots/api#sendmessage)

### Use it:

```
import logging

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


logger.info("Hi, here is some information")
```


### Default Emojis:

Emoji | Level
------|--------
  ⚪️  | DEBUG 
  🔵  | INFO 
  🟠  | WARNING
  🔴  | ERROR
  🔥  | CRITICAL
  

You can use your own set of emojis:

![telegram](https://user-images.githubusercontent.com/34322384/142038851-7ed8cf04-df2c-4705-8066-6e21e817d186.gif)


```
formatter = TelegramFormatter(
    format="[%(asctime)s %(name)s] %(levelname)8s\n\n%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    use_emoji=True,
    emoji_map={
        logging.DEBUG: "🐛",
        logging.INFO: "💡",
        logging.ERROR: "🚨",
    })
```
