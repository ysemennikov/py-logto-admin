from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_sso_connectors_body_branding import PostApiSsoConnectorsBodyBranding
    from ..models.post_api_sso_connectors_body_config import PostApiSsoConnectorsBodyConfig


T = TypeVar("T", bound="PostApiSsoConnectorsBody")


@_attrs_define
class PostApiSsoConnectorsBody:
    """
    Attributes:
        provider_name (str):
        connector_name (str):
        config (Union[Unset, PostApiSsoConnectorsBodyConfig]): arbitrary
        domains (Union[Unset, List[str]]):
        branding (Union[Unset, PostApiSsoConnectorsBodyBranding]):
        sync_profile (Union[Unset, bool]):
    """

    provider_name: str
    connector_name: str
    config: Union[Unset, "PostApiSsoConnectorsBodyConfig"] = UNSET
    domains: Union[Unset, List[str]] = UNSET
    branding: Union[Unset, "PostApiSsoConnectorsBodyBranding"] = UNSET
    sync_profile: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_name = self.provider_name

        connector_name = self.connector_name

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerName": provider_name,
                "connectorName": connector_name,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if domains is not UNSET:
            field_dict["domains"] = domains
        if branding is not UNSET:
            field_dict["branding"] = branding
        if sync_profile is not UNSET:
            field_dict["syncProfile"] = sync_profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_sso_connectors_body_branding import PostApiSsoConnectorsBodyBranding
        from ..models.post_api_sso_connectors_body_config import PostApiSsoConnectorsBodyConfig

        d = src_dict.copy()
        provider_name = d.pop("providerName")

        connector_name = d.pop("connectorName")

        _config = d.pop("config", UNSET)
        config: Union[Unset, PostApiSsoConnectorsBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PostApiSsoConnectorsBodyConfig.from_dict(_config)

        domains = cast(List[str], d.pop("domains", UNSET))

        _branding = d.pop("branding", UNSET)
        branding: Union[Unset, PostApiSsoConnectorsBodyBranding]
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = PostApiSsoConnectorsBodyBranding.from_dict(_branding)

        sync_profile = d.pop("syncProfile", UNSET)

        post_api_sso_connectors_body = cls(
            provider_name=provider_name,
            connector_name=connector_name,
            config=config,
            domains=domains,
            branding=branding,
            sync_profile=sync_profile,
        )

        post_api_sso_connectors_body.additional_properties = d
        return post_api_sso_connectors_body

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
