from enum import Enum


class PutApiInteractionMfaBodyType1AuthenticatorAttachment(str, Enum):
    CROSS_PLATFORM = "cross-platform"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
