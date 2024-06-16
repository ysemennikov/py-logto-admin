from enum import Enum


class PatchApiSignInExpResponse200SignInMethodsItemIdentifier(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
