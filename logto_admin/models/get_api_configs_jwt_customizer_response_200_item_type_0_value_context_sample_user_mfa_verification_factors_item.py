from enum import Enum


class GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserMfaVerificationFactorsItem(str, Enum):
    BACKUPCODE = "BackupCode"
    TOTP = "Totp"
    WEBAUTHN = "WebAuthn"

    def __str__(self) -> str:
        return str(self.value)
