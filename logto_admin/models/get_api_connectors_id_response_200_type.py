from enum import Enum


class GetApiConnectorsIdResponse200Type(str, Enum):
    EMAIL = "Email"
    SMS = "Sms"
    SOCIAL = "Social"

    def __str__(self) -> str:
        return str(self.value)
