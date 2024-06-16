from enum import Enum


class PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserMfaVerificationFactorsItem(str, Enum):
    BACKUPCODE = "BackupCode"
    TOTP = "Totp"
    WEBAUTHN = "WebAuthn"

    def __str__(self) -> str:
        return str(self.value)
