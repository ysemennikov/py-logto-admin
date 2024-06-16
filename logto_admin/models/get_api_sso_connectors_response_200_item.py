from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_sso_connectors_response_200_item_provider_name import (
    GetApiSsoConnectorsResponse200ItemProviderName,
)
from ..models.get_api_sso_connectors_response_200_item_provider_type import (
    GetApiSsoConnectorsResponse200ItemProviderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_sso_connectors_response_200_item_branding import GetApiSsoConnectorsResponse200ItemBranding
    from ..models.get_api_sso_connectors_response_200_item_config import GetApiSsoConnectorsResponse200ItemConfig
    from ..models.get_api_sso_connectors_response_200_item_provider_config import (
        GetApiSsoConnectorsResponse200ItemProviderConfig,
    )


T = TypeVar("T", bound="GetApiSsoConnectorsResponse200Item")


@_attrs_define
class GetApiSsoConnectorsResponse200Item:
    """
    Attributes:
        id (str):
        provider_name (GetApiSsoConnectorsResponse200ItemProviderName):
        connector_name (str):
        config (GetApiSsoConnectorsResponse200ItemConfig): arbitrary
        domains (List[str]):
        branding (GetApiSsoConnectorsResponse200ItemBranding):
        sync_profile (bool):
        created_at (float):
        name (str):
        provider_type (GetApiSsoConnectorsResponse200ItemProviderType):
        provider_logo (str):
        provider_logo_dark (str):
        provider_config (Union[Unset, GetApiSsoConnectorsResponse200ItemProviderConfig]):
    """

    id: str
    provider_name: GetApiSsoConnectorsResponse200ItemProviderName
    connector_name: str
    config: "GetApiSsoConnectorsResponse200ItemConfig"
    domains: List[str]
    branding: "GetApiSsoConnectorsResponse200ItemBranding"
    sync_profile: bool
    created_at: float
    name: str
    provider_type: GetApiSsoConnectorsResponse200ItemProviderType
    provider_logo: str
    provider_logo_dark: str
    provider_config: Union[Unset, "GetApiSsoConnectorsResponse200ItemProviderConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        provider_name = self.provider_name.value

        connector_name = self.connector_name

        config = self.config.to_dict()

        domains = self.domains

        branding = self.branding.to_dict()

        sync_profile = self.sync_profile

        created_at = self.created_at

        name = self.name

        provider_type = self.provider_type.value

        provider_logo = self.provider_logo

        provider_logo_dark = self.provider_logo_dark

        provider_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_config, Unset):
            provider_config = self.provider_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "providerName": provider_name,
                "connectorName": connector_name,
                "config": config,
                "domains": domains,
                "branding": branding,
                "syncProfile": sync_profile,
                "createdAt": created_at,
                "name": name,
                "providerType": provider_type,
                "providerLogo": provider_logo,
                "providerLogoDark": provider_logo_dark,
            }
        )
        if provider_config is not UNSET:
            field_dict["providerConfig"] = provider_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_sso_connectors_response_200_item_branding import (
            GetApiSsoConnectorsResponse200ItemBranding,
        )
        from ..models.get_api_sso_connectors_response_200_item_config import GetApiSsoConnectorsResponse200ItemConfig
        from ..models.get_api_sso_connectors_response_200_item_provider_config import (
            GetApiSsoConnectorsResponse200ItemProviderConfig,
        )

        d = src_dict.copy()
        id = d.pop("id")

        provider_name = GetApiSsoConnectorsResponse200ItemProviderName(d.pop("providerName"))

        connector_name = d.pop("connectorName")

        config = GetApiSsoConnectorsResponse200ItemConfig.from_dict(d.pop("config"))

        domains = cast(List[str], d.pop("domains"))

        branding = GetApiSsoConnectorsResponse200ItemBranding.from_dict(d.pop("branding"))

        sync_profile = d.pop("syncProfile")

        created_at = d.pop("createdAt")

        name = d.pop("name")

        provider_type = GetApiSsoConnectorsResponse200ItemProviderType(d.pop("providerType"))

        provider_logo = d.pop("providerLogo")

        provider_logo_dark = d.pop("providerLogoDark")

        _provider_config = d.pop("providerConfig", UNSET)
        provider_config: Union[Unset, GetApiSsoConnectorsResponse200ItemProviderConfig]
        if isinstance(_provider_config, Unset):
            provider_config = UNSET
        else:
            provider_config = GetApiSsoConnectorsResponse200ItemProviderConfig.from_dict(_provider_config)

        get_api_sso_connectors_response_200_item = cls(
            id=id,
            provider_name=provider_name,
            connector_name=connector_name,
            config=config,
            domains=domains,
            branding=branding,
            sync_profile=sync_profile,
            created_at=created_at,
            name=name,
            provider_type=provider_type,
            provider_logo=provider_logo,
            provider_logo_dark=provider_logo_dark,
            provider_config=provider_config,
        )

        get_api_sso_connectors_response_200_item.additional_properties = d
        return get_api_sso_connectors_response_200_item

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
