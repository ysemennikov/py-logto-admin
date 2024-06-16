from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiSignInExpResponse200Color")


@_attrs_define
class PatchApiSignInExpResponse200Color:
    """
    Attributes:
        primary_color (str):
        is_dark_mode_enabled (bool):
        dark_primary_color (str):
    """

    primary_color: str
    is_dark_mode_enabled: bool
    dark_primary_color: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary_color = self.primary_color

        is_dark_mode_enabled = self.is_dark_mode_enabled

        dark_primary_color = self.dark_primary_color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primaryColor": primary_color,
                "isDarkModeEnabled": is_dark_mode_enabled,
                "darkPrimaryColor": dark_primary_color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        primary_color = d.pop("primaryColor")

        is_dark_mode_enabled = d.pop("isDarkModeEnabled")

        dark_primary_color = d.pop("darkPrimaryColor")

        patch_api_sign_in_exp_response_200_color = cls(
            primary_color=primary_color,
            is_dark_mode_enabled=is_dark_mode_enabled,
            dark_primary_color=dark_primary_color,
        )

        patch_api_sign_in_exp_response_200_color.additional_properties = d
        return patch_api_sign_in_exp_response_200_color

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
