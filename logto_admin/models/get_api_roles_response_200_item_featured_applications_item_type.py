from enum import Enum


class GetApiRolesResponse200ItemFeaturedApplicationsItemType(str, Enum):
    MACHINETOMACHINE = "MachineToMachine"
    NATIVE = "Native"
    PROTECTED = "Protected"
    SPA = "SPA"
    TRADITIONAL = "Traditional"

    def __str__(self) -> str:
        return str(self.value)
