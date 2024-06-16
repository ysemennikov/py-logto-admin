from enum import Enum


class GetApiSignInExpResponse200SignInMethodsItemIdentifier(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
