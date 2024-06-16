from enum import Enum


class GetApiRolesResponse200ItemType(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
