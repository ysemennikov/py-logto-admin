from enum import Enum


class GetApiSsoConnectorsIdResponse200ProviderType(str, Enum):
    OIDC = "oidc"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
