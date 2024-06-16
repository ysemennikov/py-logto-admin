from enum import Enum


class GetApiSignInExpResponse200MfaPolicy(str, Enum):
    MANDATORY = "Mandatory"
    USERCONTROLLED = "UserControlled"

    def __str__(self) -> str:
        return str(self.value)
