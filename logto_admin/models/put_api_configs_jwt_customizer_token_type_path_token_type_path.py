from enum import Enum


class PutApiConfigsJwtCustomizerTokenTypePathTokenTypePath(str, Enum):
    ACCESS_TOKEN = "access-token"
    CLIENT_CREDENTIALS = "client-credentials"

    def __str__(self) -> str:
        return str(self.value)
