from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_sso_connectors_id_body_branding import PatchApiSsoConnectorsIdBodyBranding
    from ..models.patch_api_sso_connectors_id_body_config import PatchApiSsoConnectorsIdBodyConfig


T = TypeVar("T", bound="PatchApiSsoConnectorsIdBody")


@_attrs_define
class PatchApiSsoConnectorsIdBody:
    """
    Attributes:
        config (Union[Unset, PatchApiSsoConnectorsIdBodyConfig]): arbitrary
        domains (Union[Unset, List[str]]):
        branding (Union[Unset, PatchApiSsoConnectorsIdBodyBranding]):
        sync_profile (Union[Unset, bool]):
        connector_name (Union[Unset, str]):
    """

    config: Union[Unset, "PatchApiSsoConnectorsIdBodyConfig"] = UNSET
    domains: Union[Unset, List[str]] = UNSET
    branding: Union[Unset, "PatchApiSsoConnectorsIdBodyBranding"] = UNSET
    sync_profile: Union[Unset, bool] = UNSET
    connector_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        branding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branding, Unset):
            branding = self.branding.to_dict()

        sync_profile = self.sync_profile

        connector_name = self.connector_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if domains is not UNSET:
            field_dict["domains"] = domains
        if branding is not UNSET:
            field_dict["branding"] = branding
        if sync_profile is not UNSET:
            field_dict["syncProfile"] = sync_profile
        if connector_name is not UNSET:
            field_dict["connectorName"] = connector_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_sso_connectors_id_body_branding import PatchApiSsoConnectorsIdBodyBranding
        from ..models.patch_api_sso_connectors_id_body_config import PatchApiSsoConnectorsIdBodyConfig

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, PatchApiSsoConnectorsIdBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PatchApiSsoConnectorsIdBodyConfig.from_dict(_config)

        domains = cast(List[str], d.pop("domains", UNSET))

        _branding = d.pop("branding", UNSET)
        branding: Union[Unset, PatchApiSsoConnectorsIdBodyBranding]
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = PatchApiSsoConnectorsIdBodyBranding.from_dict(_branding)

        sync_profile = d.pop("syncProfile", UNSET)

        connector_name = d.pop("connectorName", UNSET)

        patch_api_sso_connectors_id_body = cls(
            config=config,
            domains=domains,
            branding=branding,
            sync_profile=sync_profile,
            connector_name=connector_name,
        )

        patch_api_sso_connectors_id_body.additional_properties = d
        return patch_api_sso_connectors_id_body

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
