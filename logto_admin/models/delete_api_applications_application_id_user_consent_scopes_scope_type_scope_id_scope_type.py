from enum import Enum


class DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType(str, Enum):
    ORGANIZATION_RESOURCE_SCOPES = "organization-resource-scopes"
    ORGANIZATION_SCOPES = "organization-scopes"
    RESOURCE_SCOPES = "resource-scopes"
    USER_SCOPES = "user-scopes"

    def __str__(self) -> str:
        return str(self.value)
