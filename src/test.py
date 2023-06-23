from pprint import pprint
from bot.inner_bot import Bot
from methods.get_me import GetMe
from methods.get_user_profile_photos import (
    GetUserProfilePhotos,
)


bot = Bot("5603622755:AAGW1Dmj72BsdwsJngxn-U5yMPfoqMCBxfI")
pprint(GetMe(bot).call())
pprint(GetUserProfilePhotos(bot, user_id=742596099).call())
