from enum import Enum


class GetApiDomainsResponse200ItemStatus(str, Enum):
    ACTIVE = "Active"
    ERROR = "Error"
    PENDINGSSL = "PendingSsl"
    PENDINGVERIFICATION = "PendingVerification"

    def __str__(self) -> str:
        return str(self.value)
