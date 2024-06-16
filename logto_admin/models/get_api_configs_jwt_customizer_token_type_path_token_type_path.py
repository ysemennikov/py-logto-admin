from enum import Enum


class GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath(str, Enum):
    ACCESS_TOKEN = "access-token"
    CLIENT_CREDENTIALS = "client-credentials"

    def __str__(self) -> str:
        return str(self.value)
