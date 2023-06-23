from dacite import from_dict

from methods.method import Method
from bot.inner_bot import Bot
from content import JsonContent
from methods.raw_method import RawMethod
from tg_types.user.profile_photos import ProfilePhotos
from uri.method_uri import MethodURI


class GetUserProfilePhotos(Method[ProfilePhotos]):
    def __init__(self, bot: Bot, user_id: int) -> None:
        self._bot = bot
        self.user_id = user_id

    def call(self) -> ProfilePhotos:
        instance = from_dict(
            data_class=ProfilePhotos,
            data=RawMethod(
                MethodURI(
                    "getUserProfilePhotos", self._bot
                ),
                JsonContent({"user_id": self.user_id}),
            ).call(),
        )
        return instance  # type: ignore
