from enum import Enum


class GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemStatus(str, Enum):
    ACTIVE = "Active"
    ERROR = "Error"
    PENDINGSSL = "PendingSsl"
    PENDINGVERIFICATION = "PendingVerification"

    def __str__(self) -> str:
        return str(self.value)
