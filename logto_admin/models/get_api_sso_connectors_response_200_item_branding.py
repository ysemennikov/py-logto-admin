from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiSsoConnectorsResponse200ItemBranding")


@_attrs_define
class GetApiSsoConnectorsResponse200ItemBranding:
    """
    Attributes:
        display_name (Union[Unset, str]):
        logo (Union[Unset, str]):
        dark_logo (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    dark_logo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        logo = self.logo

        dark_logo = self.dark_logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if dark_logo is not UNSET:
            field_dict["darkLogo"] = dark_logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        logo = d.pop("logo", UNSET)

        dark_logo = d.pop("darkLogo", UNSET)

        get_api_sso_connectors_response_200_item_branding = cls(
            display_name=display_name,
            logo=logo,
            dark_logo=dark_logo,
        )

        get_api_sso_connectors_response_200_item_branding.additional_properties = d
        return get_api_sso_connectors_response_200_item_branding

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
