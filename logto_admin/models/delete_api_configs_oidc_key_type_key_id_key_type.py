from enum import Enum


class DeleteApiConfigsOidcKeyTypeKeyIdKeyType(str, Enum):
    COOKIE_KEYS = "cookie-keys"
    PRIVATE_KEYS = "private-keys"

    def __str__(self) -> str:
        return str(self.value)
