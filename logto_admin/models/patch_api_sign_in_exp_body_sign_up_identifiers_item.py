from enum import Enum


class PatchApiSignInExpBodySignUpIdentifiersItem(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
