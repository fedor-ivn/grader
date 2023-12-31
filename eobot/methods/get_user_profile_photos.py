from dacite import from_dict

from methods.method import Method
from eobot.bot.bot import Bot
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tgtypes.user.profile_photos import ProfilePhotos
from uri.method_uri import MethodURI
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class GetUserProfilePhotos(Method[ProfilePhotos]):
    def __init__(
        self,
        bot: Bot,
        user_id: int,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._bot = bot
        self.user_id = user_id
        self._log = log

    def call(self, bot: URI) -> ProfilePhotos:
        instance = from_dict(
            data_class=ProfilePhotos,
            data=RawMethod(
                JsonRequestContent(
                    {"user_id": self.user_id}
                ),
            ).call(MethodURI("getUserProfilePhotos", bot)),
        )
        self._log.debug("GetUserProfilePhotos method call")
        return instance  # type: ignore
