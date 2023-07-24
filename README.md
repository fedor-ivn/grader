[![EO principles respected
here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![](https://tokei.rs/b1/github/fedor-ivn/grader)](https://github.com/fedor-ivn/grader)
[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

# EOBot

EOBot is a python library which allows to interact with telegram bot API. The
main distinguishing feature of this library is that it was written using the
methods and techniques from the 'Elegant Objects' book by Yegor Bugayenko. Thus
the name - Elegant Objects Bot.

The library was used to create the bot for cli tasks solutions grading. The contents of the `grader` package, which was created and used for that purpose can be found in the [grader](https://github.com/fedor-ivn/grader/grader) folder of the project.

## Getting started

The eobot library contents are located in the [eobot](https://github.com/fedor-ivn/grader/eobot) folder of the project. 

Several bot implementation examples were added in the [examples](https://github.com/fedor-ivn/grader/eobot/examples) folder to demonstrate the main features of the bot separately.

There are 4 examples used as the showcase of each of the implemented features:
1. echo.py - receiving/sending of text messages;
2. document_echo.py - receiving/reading the documents;
3. buttons.py - creating the keyboard buttons;
4. grader_test.py - grading of the cli tasks solutions.

To run the provided examples, create the .env file in the root folder and add the BOT_TOKEN value. Then, install all dependencies using `poetry shell` command and run `PYTHONPATH="$PYTHONPATH:$PWD/eobot" python eobot/examples/<EXAMPLE_NAME>.py`.

## Writing your first bot

### Prerequisites

To create a bot instance, you will need to provide its API key to the .env file
to the location from which you will run the code. The API key may be obtained
from the [BotFather](https://t.me/botfather).

### A simple echo bot

Using the key, create an instance of the bot:

```python
from eobot.bot.bot import Bot

bot = Bot(DotenvToken("BOT_TOKEN", DotEnv(".env")))
```

In this example, we will make the bot to reply as defined in `Echo()` on any
text message it will receive. To define this class, you will need to inherit it
from the `OnTextMessage` class:

```python
from eobot.tgtypes.message.text import TextMessage
from eobot.update.message.text import OnTextMessage
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from eobot.arguments.message.text import PlainText

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
from polling import Polling, PollingConfig
from event_loop import EventLoop
from update.events import Events

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

That's it, the bot will now start the polling and will behave as defined in the method call.

## General Documentation

### Types

The types are listed in
[tgtypes](https://github.com/fedor-ivn/grader/eobot/tgtypes) folder. They are in line with the [Telegram API's definition of the types](https://core.telegram.org/bots/api#available-types)

### Methods

The methods are listed in
[methods](https://github.com/fedor-ivn/grader/eobot/methods) folder
of the package. They are renamed to follow the common Python naming conventions.
E.g. `getMe` is renamed to `get_me`.

### Grader

The project includes the `grader` poetry package, which can be installed using the `poetry install command`. The tests are contstructed by a sequence of criteria using the `SequentialCriteria` object, which are later used to test the output of the `.sh` file.

### Logger

The project includes the custom implementation of the logging package using the `logging` python library to satisfy the EO principles. It could be installed using `poetry install command`

`Log` object could be passed to each method in order to log it. If no logging required, the method gets `NoLog` object.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.

## LICENCE

[MIT](https://choosealicense.com/licenses/mit/)
<!-- todo: add counter https://shields.io/category/size -->
