from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_connectors_body_config import PostApiConnectorsBodyConfig
    from ..models.post_api_connectors_body_metadata import PostApiConnectorsBodyMetadata


T = TypeVar("T", bound="PostApiConnectorsBody")


@_attrs_define
class PostApiConnectorsBody:
    """
    Attributes:
        connector_id (str): The connector factory ID for creating the connector.
        config (Union[Unset, PostApiConnectorsBodyConfig]): The connector config object that will be passed to the
            connector. The config object should be compatible with the connector factory.
        metadata (Union[Unset, PostApiConnectorsBodyMetadata]): Custom connector metadata, will be used to overwrite the
            default connector factory metadata.
        sync_profile (Union[Unset, bool]): Whether to sync user profile from the identity provider to Logto at each
            sign-in. If `false`, the user profile will only be synced when the user is created.
        id (Union[Unset, str]): The unique ID for the connector. If not provided, a random ID will be generated.
    """

    connector_id: str
    config: Union[Unset, "PostApiConnectorsBodyConfig"] = UNSET
    metadata: Union[Unset, "PostApiConnectorsBodyMetadata"] = UNSET
    sync_profile: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        sync_profile = self.sync_profile

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if sync_profile is not UNSET:
            field_dict["syncProfile"] = sync_profile
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_connectors_body_config import PostApiConnectorsBodyConfig
        from ..models.post_api_connectors_body_metadata import PostApiConnectorsBodyMetadata

        d = src_dict.copy()
        connector_id = d.pop("connectorId")

        _config = d.pop("config", UNSET)
        config: Union[Unset, PostApiConnectorsBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PostApiConnectorsBodyConfig.from_dict(_config)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PostApiConnectorsBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostApiConnectorsBodyMetadata.from_dict(_metadata)

        sync_profile = d.pop("syncProfile", UNSET)

        id = d.pop("id", UNSET)

        post_api_connectors_body = cls(
            connector_id=connector_id,
            config=config,
            metadata=metadata,
            sync_profile=sync_profile,
            id=id,
        )

        post_api_connectors_body.additional_properties = d
        return post_api_connectors_body

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
