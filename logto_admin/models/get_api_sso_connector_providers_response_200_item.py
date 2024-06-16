from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_sso_connector_providers_response_200_item_provider_name import (
    GetApiSsoConnectorProvidersResponse200ItemProviderName,
)
from ..models.get_api_sso_connector_providers_response_200_item_provider_type import (
    GetApiSsoConnectorProvidersResponse200ItemProviderType,
)

T = TypeVar("T", bound="GetApiSsoConnectorProvidersResponse200Item")


@_attrs_define
class GetApiSsoConnectorProvidersResponse200Item:
    """
    Attributes:
        provider_name (GetApiSsoConnectorProvidersResponse200ItemProviderName):
        provider_type (GetApiSsoConnectorProvidersResponse200ItemProviderType):
        logo (str):
        logo_dark (str):
        description (str):
        name (str):
    """

    provider_name: GetApiSsoConnectorProvidersResponse200ItemProviderName
    provider_type: GetApiSsoConnectorProvidersResponse200ItemProviderType
    logo: str
    logo_dark: str
    description: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_name = self.provider_name.value

        provider_type = self.provider_type.value

        logo = self.logo

        logo_dark = self.logo_dark

        description = self.description

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerName": provider_name,
                "providerType": provider_type,
                "logo": logo,
                "logoDark": logo_dark,
                "description": description,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider_name = GetApiSsoConnectorProvidersResponse200ItemProviderName(d.pop("providerName"))

        provider_type = GetApiSsoConnectorProvidersResponse200ItemProviderType(d.pop("providerType"))

        logo = d.pop("logo")

        logo_dark = d.pop("logoDark")

        description = d.pop("description")

        name = d.pop("name")

        get_api_sso_connector_providers_response_200_item = cls(
            provider_name=provider_name,
            provider_type=provider_type,
            logo=logo,
            logo_dark=logo_dark,
            description=description,
            name=name,
        )

        get_api_sso_connector_providers_response_200_item.additional_properties = d
        return get_api_sso_connector_providers_response_200_item

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
