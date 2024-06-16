from enum import Enum


class PatchApiSignInExpResponse200MfaPolicy(str, Enum):
    MANDATORY = "Mandatory"
    USERCONTROLLED = "UserControlled"

    def __str__(self) -> str:
        return str(self.value)
