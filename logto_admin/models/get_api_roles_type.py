from enum import Enum


class GetApiRolesType(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
