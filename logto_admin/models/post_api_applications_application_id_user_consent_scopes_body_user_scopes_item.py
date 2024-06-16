from enum import Enum


class PostApiApplicationsApplicationIdUserConsentScopesBodyUserScopesItem(str, Enum):
    ADDRESS = "address"
    CUSTOM_DATA = "custom_data"
    EMAIL = "email"
    IDENTITIES = "identities"
    PHONE = "phone"
    PROFILE = "profile"
    ROLES = "roles"
    URNLOGTOSCOPEORGANIZATIONS = "urn:logto:scope:organizations"
    URNLOGTOSCOPEORGANIZATION_ROLES = "urn:logto:scope:organization_roles"

    def __str__(self) -> str:
        return str(self.value)
