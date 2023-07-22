[![](https://tokei.rs/b1/github/fedor-ivn/grader)](https://github.com/fedor-ivn/grader)
[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

# EOBot

EOBot is a python library which allows to interact with telegram bot API. The
main distinguishing feature of this library is that it was writed using the
methods and techniques from the 'Elegant Objects' book by Yegor Bugayenko. Thus
the name - Elegant Objects Bot.

## Installation

Use poetry to install the eobot library - TODO

## Writing your first bot

Several bot implementation examples were added in the
[examples](https://github.com/fedor-ivn/grader/tree/pytbot/eobot) folder to
demonstrate the main features of the bot separately.

### Prerequisites

To create a bot instance, you will need to provide its API key to the .env file
to the location from which you will run the code. The API key may be obtained
from the [BotFather](https://t.me/botfather).

### A simple echo bot

Using the key, create an instance of the bot:

```python
bot = Bot(DotenvToken("BOT_TOKEN", DotEnv(".env")))
```

In this example, we will make the bot to reply as defined in `Echo()` on any
text message it will receive. To define this class, you will need to inherit it
from the `OnTextMessage` class:

```python
class Echo(OnTextMessage):
    def __init__(self, log: AbstractLog = NoLog()) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> bool:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                text=PlainText(message.text.value),
            )
        )
        return True
```
Then, start the bot polling, defining the reply on the text message as follows:

```python
bot.start(
    Polling(
        EventLoop(
            Events(
                on_text_message=[
                    Echo(),
                ],
            ),
        ),
        PollingConfig(),
    ),
)
```

That's it, the bot will now start the polling.

## General Documentation

### Types

The types are listed in
[tgtypes](https://github.com/fedor-ivn/grader/tree/pytbot/eobot/tgtypes) folder
- TODO

### Methods

The methods are listed in
[methods](https://github.com/fedor-ivn/grader/tree/pytbot/eobot/methods) folder
of the package, they are renamed to follow the common Python naming conventions.
E.g. `getMe` is renamed to `get_me`.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.

## LICENCE

[MIT](https://choosealicense.com/licenses/mit/)
<!-- todo: add counter https://shields.io/category/size -->
