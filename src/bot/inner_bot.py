from uri.telegram_api_uri import TelegramApiURI
from uri.uri import URI


class Bot(URI):
    def __init__(
        self, token: str, api_uri: URI = TelegramApiURI()
    ) -> None:
        self._token = token
        self._api_uri = api_uri

    def construct_uri(self) -> str:
        return f"{self._api_uri.construct_uri()}bot{self._token}/"
