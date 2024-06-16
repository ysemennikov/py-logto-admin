from enum import Enum


class PatchApiConnectorsIdResponse200Type(str, Enum):
    EMAIL = "Email"
    SMS = "Sms"
    SOCIAL = "Social"

    def __str__(self) -> str:
        return str(self.value)
