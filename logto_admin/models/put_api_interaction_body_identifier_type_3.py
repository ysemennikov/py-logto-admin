from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiInteractionBodyIdentifierType3")


@_attrs_define
class PutApiInteractionBodyIdentifierType3:
    """
    Attributes:
        email (str):
        verification_code (str):
    """

    email: str
    verification_code: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        verification_code = self.verification_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "verificationCode": verification_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        verification_code = d.pop("verificationCode")

        put_api_interaction_body_identifier_type_3 = cls(
            email=email,
            verification_code=verification_code,
        )

        put_api_interaction_body_identifier_type_3.additional_properties = d
        return put_api_interaction_body_identifier_type_3

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
