from enum import Enum


class GetApiSsoConnectorProvidersResponse200ItemProviderType(str, Enum):
    OIDC = "oidc"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
