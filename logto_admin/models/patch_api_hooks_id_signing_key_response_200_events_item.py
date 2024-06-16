from enum import Enum


class PatchApiHooksIdSigningKeyResponse200EventsItem(str, Enum):
    ORGANIZATIONROLE_CREATED = "OrganizationRole.Created"
    ORGANIZATIONROLE_DATA_UPDATED = "OrganizationRole.Data.Updated"
    ORGANIZATIONROLE_DELETED = "OrganizationRole.Deleted"
    ORGANIZATIONROLE_SCOPES_UPDATED = "OrganizationRole.Scopes.Updated"
    ORGANIZATIONSCOPE_CREATED = "OrganizationScope.Created"
    ORGANIZATIONSCOPE_DATA_UPDATED = "OrganizationScope.Data.Updated"
    ORGANIZATIONSCOPE_DELETED = "OrganizationScope.Deleted"
    ORGANIZATION_CREATED = "Organization.Created"
    ORGANIZATION_DATA_UPDATED = "Organization.Data.Updated"
    ORGANIZATION_DELETED = "Organization.Deleted"
    ORGANIZATION_MEMBERSHIP_UPDATED = "Organization.Membership.Updated"
    POSTREGISTER = "PostRegister"
    POSTRESETPASSWORD = "PostResetPassword"
    POSTSIGNIN = "PostSignIn"
    ROLE_CREATED = "Role.Created"
    ROLE_DATA_UPDATED = "Role.Data.Updated"
    ROLE_DELETED = "Role.Deleted"
    ROLE_SCOPES_UPDATED = "Role.Scopes.Updated"
    SCOPE_CREATED = "Scope.Created"
    SCOPE_DATA_UPDATED = "Scope.Data.Updated"
    SCOPE_DELETED = "Scope.Deleted"
    USER_CREATED = "User.Created"
    USER_DATA_UPDATED = "User.Data.Updated"
    USER_DELETED = "User.Deleted"
    USER_SUSPENSIONSTATUS_UPDATED = "User.SuspensionStatus.Updated"

    def __str__(self) -> str:
        return str(self.value)
