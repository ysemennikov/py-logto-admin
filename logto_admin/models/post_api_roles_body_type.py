from enum import Enum


class PostApiRolesBodyType(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
