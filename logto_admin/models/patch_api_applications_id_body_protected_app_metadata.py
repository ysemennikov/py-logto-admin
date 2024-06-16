from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_applications_id_body_protected_app_metadata_page_rules_item import (
        PatchApiApplicationsIdBodyProtectedAppMetadataPageRulesItem,
    )


T = TypeVar("T", bound="PatchApiApplicationsIdBodyProtectedAppMetadata")


@_attrs_define
class PatchApiApplicationsIdBodyProtectedAppMetadata:
    """
    Attributes:
        origin (Union[Unset, str]):
        session_duration (Union[Unset, float]):
        page_rules (Union[Unset, List['PatchApiApplicationsIdBodyProtectedAppMetadataPageRulesItem']]):
    """

    origin: Union[Unset, str] = UNSET
    session_duration: Union[Unset, float] = UNSET
    page_rules: Union[Unset, List["PatchApiApplicationsIdBodyProtectedAppMetadataPageRulesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin

        session_duration = self.session_duration

        page_rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.page_rules, Unset):
            page_rules = []
            for page_rules_item_data in self.page_rules:
                page_rules_item = page_rules_item_data.to_dict()
                page_rules.append(page_rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origin is not UNSET:
            field_dict["origin"] = origin
        if session_duration is not UNSET:
            field_dict["sessionDuration"] = session_duration
        if page_rules is not UNSET:
            field_dict["pageRules"] = page_rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_applications_id_body_protected_app_metadata_page_rules_item import (
            PatchApiApplicationsIdBodyProtectedAppMetadataPageRulesItem,
        )

        d = src_dict.copy()
        origin = d.pop("origin", UNSET)

        session_duration = d.pop("sessionDuration", UNSET)

        page_rules = []
        _page_rules = d.pop("pageRules", UNSET)
        for page_rules_item_data in _page_rules or []:
            page_rules_item = PatchApiApplicationsIdBodyProtectedAppMetadataPageRulesItem.from_dict(
                page_rules_item_data
            )

            page_rules.append(page_rules_item)

        patch_api_applications_id_body_protected_app_metadata = cls(
            origin=origin,
            session_duration=session_duration,
            page_rules=page_rules,
        )

        patch_api_applications_id_body_protected_app_metadata.additional_properties = d
        return patch_api_applications_id_body_protected_app_metadata

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
