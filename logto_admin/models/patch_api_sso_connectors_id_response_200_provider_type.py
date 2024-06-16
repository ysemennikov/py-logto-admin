from enum import Enum


class PatchApiSsoConnectorsIdResponse200ProviderType(str, Enum):
    OIDC = "oidc"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
