from enum import Enum


class PostApiConnectorsResponse200Platform(str, Enum):
    NATIVE = "Native"
    UNIVERSAL = "Universal"
    WEB = "Web"

    def __str__(self) -> str:
        return str(self.value)
