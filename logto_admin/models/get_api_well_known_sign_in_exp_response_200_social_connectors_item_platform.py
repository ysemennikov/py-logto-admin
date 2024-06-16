from enum import Enum


class GetApiWellKnownSignInExpResponse200SocialConnectorsItemPlatform(str, Enum):
    NATIVE = "Native"
    UNIVERSAL = "Universal"
    WEB = "Web"

    def __str__(self) -> str:
        return str(self.value)
