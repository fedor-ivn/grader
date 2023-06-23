from uri.uri import URI


class TelegramApiURI(URI):
    def __init__(
        self, api_uri: str = "https://api.telegram.org/"
    ) -> None:
        self._api_uri = api_uri

    def construct_uri(self) -> str:
        return self._api_uri
