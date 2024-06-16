from enum import Enum


class PutApiOrganizationInvitationsIdStatusBodyStatus(str, Enum):
    ACCEPTED = "Accepted"
    REVOKED = "Revoked"

    def __str__(self) -> str:
        return str(self.value)
