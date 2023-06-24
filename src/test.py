from bot.inner_bot import Bot
from methods.get_me import GetMe
from methods.get_user_profile_photos import (
    GetUserProfilePhotos,
)
from methods.send_message import SendMessage


bot = Bot("5603622755:AAGW1Dmj72BsdwsJngxn-U5yMPfoqMCBxfI")
# GetMe(bot).call()
# print(GetUserProfilePhotos(bot, user_id=742596099).call())
print(SendMessage(bot=bot, chat_id=742596099, text="Hello!").call())
