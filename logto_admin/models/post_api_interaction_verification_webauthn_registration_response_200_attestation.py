from enum import Enum


class PostApiInteractionVerificationWebauthnRegistrationResponse200Attestation(str, Enum):
    DIRECT = "direct"
    ENTERPRISE = "enterprise"
    INDIRECT = "indirect"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
