from enum import Enum


class GetApiRolesIdResponse200Type(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
