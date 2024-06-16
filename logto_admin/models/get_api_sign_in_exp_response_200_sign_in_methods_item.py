from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_sign_in_exp_response_200_sign_in_methods_item_identifier import (
    GetApiSignInExpResponse200SignInMethodsItemIdentifier,
)

T = TypeVar("T", bound="GetApiSignInExpResponse200SignInMethodsItem")


@_attrs_define
class GetApiSignInExpResponse200SignInMethodsItem:
    """
    Attributes:
        identifier (GetApiSignInExpResponse200SignInMethodsItemIdentifier):
        password (bool):
        verification_code (bool):
        is_password_primary (bool):
    """

    identifier: GetApiSignInExpResponse200SignInMethodsItemIdentifier
    password: bool
    verification_code: bool
    is_password_primary: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier.value

        password = self.password

        verification_code = self.verification_code

        is_password_primary = self.is_password_primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "password": password,
                "verificationCode": verification_code,
                "isPasswordPrimary": is_password_primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = GetApiSignInExpResponse200SignInMethodsItemIdentifier(d.pop("identifier"))

        password = d.pop("password")

        verification_code = d.pop("verificationCode")

        is_password_primary = d.pop("isPasswordPrimary")

        get_api_sign_in_exp_response_200_sign_in_methods_item = cls(
            identifier=identifier,
            password=password,
            verification_code=verification_code,
            is_password_primary=is_password_primary,
        )

        get_api_sign_in_exp_response_200_sign_in_methods_item.additional_properties = d
        return get_api_sign_in_exp_response_200_sign_in_methods_item

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
