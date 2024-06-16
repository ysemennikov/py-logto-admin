from enum import Enum


class PostApiInteractionBindMfaBodyType1AuthenticatorAttachment(str, Enum):
    CROSS_PLATFORM = "cross-platform"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
