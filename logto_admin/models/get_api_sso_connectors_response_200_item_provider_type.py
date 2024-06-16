from enum import Enum


class GetApiSsoConnectorsResponse200ItemProviderType(str, Enum):
    OIDC = "oidc"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
