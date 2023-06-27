class NetworkException(Exception):
    def __init__(self) -> None:
        super().__init__("Service is not reachable")


class UnexpectedResponseException(Exception):
    def __init__(self) -> None:
        super().__init__("Unexpected response is received")


class OutOfServiceException(Exception):
    def __init__(self) -> None:
        super().__init__("Service is currently unavailable")


class ApiMethodException(Exception):
    def __init__(
        self, description: str, error_code: int
    ) -> None:
        self._description = description
        self._error_code = error_code
        super().__init__(self._description)


class NoUpdatesException(Exception):
    def __init__(self) -> None:
        super().__init__("This time there are no updates")


class TokenNotFoundError(Exception):
    def __init__(self, description: str) -> None:
        super().__init__(description)
