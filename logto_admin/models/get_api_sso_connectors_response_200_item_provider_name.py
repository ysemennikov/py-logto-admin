from enum import Enum


class GetApiSsoConnectorsResponse200ItemProviderName(str, Enum):
    AZUREAD = "AzureAD"
    AZUREADOIDC = "AzureAdOidc"
    GOOGLEWORKSPACE = "GoogleWorkspace"
    OIDC = "OIDC"
    OKTA = "Okta"
    SAML = "SAML"

    def __str__(self) -> str:
        return str(self.value)
