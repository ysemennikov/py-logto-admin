from enum import Enum


class PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionUserVerification(str, Enum):
    DISCOURAGED = "discouraged"
    PREFERRED = "preferred"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
