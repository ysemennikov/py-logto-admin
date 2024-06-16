from enum import Enum


class GetApiWellKnownSignInExpResponse200MfaPolicy(str, Enum):
    MANDATORY = "Mandatory"
    USERCONTROLLED = "UserControlled"

    def __str__(self) -> str:
        return str(self.value)
