from enum import Enum


class PatchApiSignInExpBodyMfaPolicy(str, Enum):
    MANDATORY = "Mandatory"
    USERCONTROLLED = "UserControlled"

    def __str__(self) -> str:
        return str(self.value)
