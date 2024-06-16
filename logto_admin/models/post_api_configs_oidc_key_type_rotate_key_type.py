from enum import Enum


class PostApiConfigsOidcKeyTypeRotateKeyType(str, Enum):
    COOKIE_KEYS = "cookie-keys"
    PRIVATE_KEYS = "private-keys"

    def __str__(self) -> str:
        return str(self.value)
