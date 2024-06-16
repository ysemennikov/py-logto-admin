from enum import Enum


class PatchApiRolesIdResponse200Type(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
