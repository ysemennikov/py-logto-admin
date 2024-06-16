from enum import Enum


class PatchApiSsoConnectorsIdResponse200ProviderName(str, Enum):
    AZUREAD = "AzureAD"
    AZUREADOIDC = "AzureAdOidc"
    GOOGLEWORKSPACE = "GoogleWorkspace"
    OIDC = "OIDC"
    OKTA = "Okta"
    SAML = "SAML"

    def __str__(self) -> str:
        return str(self.value)
