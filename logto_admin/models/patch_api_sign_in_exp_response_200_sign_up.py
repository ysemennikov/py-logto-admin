from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_sign_in_exp_response_200_sign_up_identifiers_item import (
    PatchApiSignInExpResponse200SignUpIdentifiersItem,
)

T = TypeVar("T", bound="PatchApiSignInExpResponse200SignUp")


@_attrs_define
class PatchApiSignInExpResponse200SignUp:
    """
    Attributes:
        identifiers (List[PatchApiSignInExpResponse200SignUpIdentifiersItem]):
        password (bool):
        verify (bool):
    """

    identifiers: List[PatchApiSignInExpResponse200SignUpIdentifiersItem]
    password: bool
    verify: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifiers = []
        for identifiers_item_data in self.identifiers:
            identifiers_item = identifiers_item_data.value
            identifiers.append(identifiers_item)

        password = self.password

        verify = self.verify

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifiers": identifiers,
                "password": password,
                "verify": verify,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifiers = []
        _identifiers = d.pop("identifiers")
        for identifiers_item_data in _identifiers:
            identifiers_item = PatchApiSignInExpResponse200SignUpIdentifiersItem(identifiers_item_data)

            identifiers.append(identifiers_item)

        password = d.pop("password")

        verify = d.pop("verify")

        patch_api_sign_in_exp_response_200_sign_up = cls(
            identifiers=identifiers,
            password=password,
            verify=verify,
        )

        patch_api_sign_in_exp_response_200_sign_up.additional_properties = d
        return patch_api_sign_in_exp_response_200_sign_up

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
