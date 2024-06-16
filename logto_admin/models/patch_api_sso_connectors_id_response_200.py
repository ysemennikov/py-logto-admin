from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_sso_connectors_id_response_200_provider_name import (
    PatchApiSsoConnectorsIdResponse200ProviderName,
)
from ..models.patch_api_sso_connectors_id_response_200_provider_type import (
    PatchApiSsoConnectorsIdResponse200ProviderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_sso_connectors_id_response_200_branding import PatchApiSsoConnectorsIdResponse200Branding
    from ..models.patch_api_sso_connectors_id_response_200_config import PatchApiSsoConnectorsIdResponse200Config
    from ..models.patch_api_sso_connectors_id_response_200_provider_config import (
        PatchApiSsoConnectorsIdResponse200ProviderConfig,
    )


T = TypeVar("T", bound="PatchApiSsoConnectorsIdResponse200")


@_attrs_define
class PatchApiSsoConnectorsIdResponse200:
    """
    Attributes:
        id (str):
        provider_name (PatchApiSsoConnectorsIdResponse200ProviderName):
        connector_name (str):
        config (PatchApiSsoConnectorsIdResponse200Config): arbitrary
        domains (List[str]):
        branding (PatchApiSsoConnectorsIdResponse200Branding):
        sync_profile (bool):
        created_at (float):
        name (str):
        provider_type (PatchApiSsoConnectorsIdResponse200ProviderType):
        provider_logo (str):
        provider_logo_dark (str):
        provider_config (Union[Unset, PatchApiSsoConnectorsIdResponse200ProviderConfig]):
    """

    id: str
    provider_name: PatchApiSsoConnectorsIdResponse200ProviderName
    connector_name: str
    config: "PatchApiSsoConnectorsIdResponse200Config"
    domains: List[str]
    branding: "PatchApiSsoConnectorsIdResponse200Branding"
    sync_profile: bool
    created_at: float
    name: str
    provider_type: PatchApiSsoConnectorsIdResponse200ProviderType
    provider_logo: str
    provider_logo_dark: str
    provider_config: Union[Unset, "PatchApiSsoConnectorsIdResponse200ProviderConfig"] = UNSET
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
        from ..models.patch_api_sso_connectors_id_response_200_branding import (
            PatchApiSsoConnectorsIdResponse200Branding,
        )
        from ..models.patch_api_sso_connectors_id_response_200_config import PatchApiSsoConnectorsIdResponse200Config
        from ..models.patch_api_sso_connectors_id_response_200_provider_config import (
            PatchApiSsoConnectorsIdResponse200ProviderConfig,
        )

        d = src_dict.copy()
        id = d.pop("id")

        provider_name = PatchApiSsoConnectorsIdResponse200ProviderName(d.pop("providerName"))

        connector_name = d.pop("connectorName")

        config = PatchApiSsoConnectorsIdResponse200Config.from_dict(d.pop("config"))

        domains = cast(List[str], d.pop("domains"))

        branding = PatchApiSsoConnectorsIdResponse200Branding.from_dict(d.pop("branding"))

        sync_profile = d.pop("syncProfile")

        created_at = d.pop("createdAt")

        name = d.pop("name")

        provider_type = PatchApiSsoConnectorsIdResponse200ProviderType(d.pop("providerType"))

        provider_logo = d.pop("providerLogo")

        provider_logo_dark = d.pop("providerLogoDark")

        _provider_config = d.pop("providerConfig", UNSET)
        provider_config: Union[Unset, PatchApiSsoConnectorsIdResponse200ProviderConfig]
        if isinstance(_provider_config, Unset):
            provider_config = UNSET
        else:
            provider_config = PatchApiSsoConnectorsIdResponse200ProviderConfig.from_dict(_provider_config)

        patch_api_sso_connectors_id_response_200 = cls(
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

        patch_api_sso_connectors_id_response_200.additional_properties = d
        return patch_api_sso_connectors_id_response_200

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
