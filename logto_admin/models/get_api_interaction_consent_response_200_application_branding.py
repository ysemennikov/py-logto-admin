from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiInteractionConsentResponse200ApplicationBranding")


@_attrs_define
class GetApiInteractionConsentResponse200ApplicationBranding:
    """
    Attributes:
        logo_url (Union[Unset, str]):
        dark_logo_url (Union[Unset, str]):
        favicon (Union[Unset, str]):
    """

    logo_url: Union[Unset, str] = UNSET
    dark_logo_url: Union[Unset, str] = UNSET
    favicon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logo_url = self.logo_url

        dark_logo_url = self.dark_logo_url

        favicon = self.favicon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if dark_logo_url is not UNSET:
            field_dict["darkLogoUrl"] = dark_logo_url
        if favicon is not UNSET:
            field_dict["favicon"] = favicon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        logo_url = d.pop("logoUrl", UNSET)

        dark_logo_url = d.pop("darkLogoUrl", UNSET)

        favicon = d.pop("favicon", UNSET)

        get_api_interaction_consent_response_200_application_branding = cls(
            logo_url=logo_url,
            dark_logo_url=dark_logo_url,
            favicon=favicon,
        )

        get_api_interaction_consent_response_200_application_branding.additional_properties = d
        return get_api_interaction_consent_response_200_application_branding

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
