from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiApplicationsIdResponse200ProtectedAppMetadataType0PageRulesItem")


@_attrs_define
class GetApiApplicationsIdResponse200ProtectedAppMetadataType0PageRulesItem:
    """
    Attributes:
        path (str):
    """

    path: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        get_api_applications_id_response_200_protected_app_metadata_type_0_page_rules_item = cls(
            path=path,
        )

        get_api_applications_id_response_200_protected_app_metadata_type_0_page_rules_item.additional_properties = d
        return get_api_applications_id_response_200_protected_app_metadata_type_0_page_rules_item

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
