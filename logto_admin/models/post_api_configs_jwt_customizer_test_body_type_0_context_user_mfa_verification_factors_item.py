from enum import Enum


class PostApiConfigsJwtCustomizerTestBodyType0ContextUserMfaVerificationFactorsItem(str, Enum):
    BACKUPCODE = "BackupCode"
    TOTP = "Totp"
    WEBAUTHN = "WebAuthn"

    def __str__(self) -> str:
        return str(self.value)
