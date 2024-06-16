from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiSignInExpResponse200PasswordPolicyLength")


@_attrs_define
class PatchApiSignInExpResponse200PasswordPolicyLength:
    """
    Attributes:
        min_ (float):  Default: 8.0.
        max_ (float):  Default: 256.0.
    """

    min_: float = 8.0
    max_: float = 256.0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min": min_,
                "max": max_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min")

        max_ = d.pop("max")

        patch_api_sign_in_exp_response_200_password_policy_length = cls(
            min_=min_,
            max_=max_,
        )

        patch_api_sign_in_exp_response_200_password_policy_length.additional_properties = d
        return patch_api_sign_in_exp_response_200_password_policy_length

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
