from enum import Enum


class PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionAuthenticatorAttachment(
    str, Enum
):
    CROSS_PLATFORM = "cross-platform"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
