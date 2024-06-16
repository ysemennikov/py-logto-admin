from enum import Enum


class GetApiOrganizationInvitationsResponse200ItemStatus(str, Enum):
    ACCEPTED = "Accepted"
    EXPIRED = "Expired"
    PENDING = "Pending"
    REVOKED = "Revoked"

    def __str__(self) -> str:
        return str(self.value)
