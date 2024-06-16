from enum import Enum


class GetApiRolesIdApplicationsResponse200ItemType(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    NATIVE = "Native"
    PROTECTED = "Protected"
    SPA = "SPA"
    TRADITIONAL = "Traditional"

    def __str__(self) -> str:
        return str(self.value)
