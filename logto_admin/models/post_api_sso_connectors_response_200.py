from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_sso_connectors_response_200_branding import PostApiSsoConnectorsResponse200Branding
    from ..models.post_api_sso_connectors_response_200_config import PostApiSsoConnectorsResponse200Config


T = TypeVar("T", bound="PostApiSsoConnectorsResponse200")


@_attrs_define
class PostApiSsoConnectorsResponse200:
    """
    Attributes:
        id (str):
        provider_name (str):
        connector_name (str):
        config (PostApiSsoConnectorsResponse200Config): arbitrary
        domains (List[str]):
        branding (PostApiSsoConnectorsResponse200Branding):
        sync_profile (bool):
        created_at (float):
    """

    id: str
    provider_name: str
    connector_name: str
    config: "PostApiSsoConnectorsResponse200Config"
    domains: List[str]
    branding: "PostApiSsoConnectorsResponse200Branding"
    sync_profile: bool
    created_at: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        provider_name = self.provider_name

        connector_name = self.connector_name

        config = self.config.to_dict()

        domains = self.domains

        branding = self.branding.to_dict()

        sync_profile = self.sync_profile

        created_at = self.created_at

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
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_sso_connectors_response_200_branding import PostApiSsoConnectorsResponse200Branding
        from ..models.post_api_sso_connectors_response_200_config import PostApiSsoConnectorsResponse200Config

        d = src_dict.copy()
        id = d.pop("id")

        provider_name = d.pop("providerName")

        connector_name = d.pop("connectorName")

        config = PostApiSsoConnectorsResponse200Config.from_dict(d.pop("config"))

        domains = cast(List[str], d.pop("domains"))

        branding = PostApiSsoConnectorsResponse200Branding.from_dict(d.pop("branding"))

        sync_profile = d.pop("syncProfile")

        created_at = d.pop("createdAt")

        post_api_sso_connectors_response_200 = cls(
            id=id,
            provider_name=provider_name,
            connector_name=connector_name,
            config=config,
            domains=domains,
            branding=branding,
            sync_profile=sync_profile,
            created_at=created_at,
        )

        post_api_sso_connectors_response_200.additional_properties = d
        return post_api_sso_connectors_response_200

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
