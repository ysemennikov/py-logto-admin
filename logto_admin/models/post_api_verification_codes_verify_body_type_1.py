from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiVerificationCodesVerifyBodyType1")


@_attrs_define
class PostApiVerificationCodesVerifyBodyType1:
    """
    Attributes:
        phone (str):
        verification_code (str):
    """

    phone: str
    verification_code: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone = self.phone

        verification_code = self.verification_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone": phone,
                "verificationCode": verification_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phone = d.pop("phone")

        verification_code = d.pop("verificationCode")

        post_api_verification_codes_verify_body_type_1 = cls(
            phone=phone,
            verification_code=verification_code,
        )

        post_api_verification_codes_verify_body_type_1.additional_properties = d
        return post_api_verification_codes_verify_body_type_1

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
