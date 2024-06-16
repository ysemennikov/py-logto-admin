from enum import Enum


class PostApiConfigsOidcKeyTypeRotateResponse200ItemSigningKeyAlgorithm(str, Enum):
    EC = "EC"
    RSA = "RSA"

    def __str__(self) -> str:
        return str(self.value)
