from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiSignInExpResponse200PasswordPolicyCharacterTypes")


@_attrs_define
class GetApiSignInExpResponse200PasswordPolicyCharacterTypes:
    """
    Attributes:
        min_ (float):  Default: 1.0.
    """

    min_: float = 1.0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min": min_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min")

        get_api_sign_in_exp_response_200_password_policy_character_types = cls(
            min_=min_,
        )

        get_api_sign_in_exp_response_200_password_policy_character_types.additional_properties = d
        return get_api_sign_in_exp_response_200_password_policy_character_types

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
