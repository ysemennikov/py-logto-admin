from enum import Enum


class PostApiInteractionVerificationWebauthnAuthenticationResponse200UserVerification(str, Enum):
    DISCOURAGED = "discouraged"
    PREFERRED = "preferred"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
