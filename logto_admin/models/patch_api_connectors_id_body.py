from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_connectors_id_body_config import PatchApiConnectorsIdBodyConfig
    from ..models.patch_api_connectors_id_body_metadata import PatchApiConnectorsIdBodyMetadata


T = TypeVar("T", bound="PatchApiConnectorsIdBody")


@_attrs_define
class PatchApiConnectorsIdBody:
    """
    Attributes:
        config (Union[Unset, PatchApiConnectorsIdBodyConfig]): The connector config object that will be passed to the
            connector. The config object should be compatible with the connector factory.
        metadata (Union[Unset, PatchApiConnectorsIdBodyMetadata]): Custom connector metadata, will be used to overwrite
            the default connector metadata.
        sync_profile (Union[Unset, bool]): Whether to sync user profile from the identity provider to Logto at each
            sign-in. If `false`, the user profile will only be synced when the user is created.
    """

    config: Union[Unset, "PatchApiConnectorsIdBodyConfig"] = UNSET
    metadata: Union[Unset, "PatchApiConnectorsIdBodyMetadata"] = UNSET
    sync_profile: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        sync_profile = self.sync_profile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if sync_profile is not UNSET:
            field_dict["syncProfile"] = sync_profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_connectors_id_body_config import PatchApiConnectorsIdBodyConfig
        from ..models.patch_api_connectors_id_body_metadata import PatchApiConnectorsIdBodyMetadata

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, PatchApiConnectorsIdBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PatchApiConnectorsIdBodyConfig.from_dict(_config)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PatchApiConnectorsIdBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PatchApiConnectorsIdBodyMetadata.from_dict(_metadata)

        sync_profile = d.pop("syncProfile", UNSET)

        patch_api_connectors_id_body = cls(
            config=config,
            metadata=metadata,
            sync_profile=sync_profile,
        )

        patch_api_connectors_id_body.additional_properties = d
        return patch_api_connectors_id_body

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
