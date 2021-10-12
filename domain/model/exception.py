class BaseException(Exception):

    def __init__(self, message: str, code: int = 400) -> None:
        self._message = message
        self._code = code

    @property
    def message(self) -> str:
        return self._message

    @property
    def code(self) -> int:
        return self._code


class NotFoundException(BaseException):

    def __init__(self, message: str) -> None:
        super().__init__(message, code=404)
