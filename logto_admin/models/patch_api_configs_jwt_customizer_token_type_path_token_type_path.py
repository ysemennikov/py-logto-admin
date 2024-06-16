from enum import Enum


class PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath(str, Enum):
    ACCESS_TOKEN = "access-token"
    CLIENT_CREDENTIALS = "client-credentials"

    def __str__(self) -> str:
        return str(self.value)
