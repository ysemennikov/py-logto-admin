from enum import Enum


class PatchApiSignInExpBodyMfaFactorsItem(str, Enum):
    BACKUPCODE = "BackupCode"
    TOTP = "Totp"
    WEBAUTHN = "WebAuthn"

    def __str__(self) -> str:
        return str(self.value)
