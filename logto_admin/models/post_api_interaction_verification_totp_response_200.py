from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiInteractionVerificationTotpResponse200")


@_attrs_define
class PostApiInteractionVerificationTotpResponse200:
    """
    Attributes:
        secret (str):
        secret_qr_code (str):
    """

    secret: str
    secret_qr_code: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secret = self.secret

        secret_qr_code = self.secret_qr_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
                "secretQrCode": secret_qr_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        secret = d.pop("secret")

        secret_qr_code = d.pop("secretQrCode")

        post_api_interaction_verification_totp_response_200 = cls(
            secret=secret,
            secret_qr_code=secret_qr_code,
        )

        post_api_interaction_verification_totp_response_200.additional_properties = d
        return post_api_interaction_verification_totp_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
