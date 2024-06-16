from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_roles_response_200_item_featured_applications_item_type import (
    GetApiRolesResponse200ItemFeaturedApplicationsItemType,
)

T = TypeVar("T", bound="GetApiRolesResponse200ItemFeaturedApplicationsItem")


@_attrs_define
class GetApiRolesResponse200ItemFeaturedApplicationsItem:
    """
    Attributes:
        id (str):
        name (str):
        type (GetApiRolesResponse200ItemFeaturedApplicationsItemType):
    """

    id: str
    name: str
    type: GetApiRolesResponse200ItemFeaturedApplicationsItemType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = GetApiRolesResponse200ItemFeaturedApplicationsItemType(d.pop("type"))

        get_api_roles_response_200_item_featured_applications_item = cls(
            id=id,
            name=name,
            type=type,
        )

        get_api_roles_response_200_item_featured_applications_item.additional_properties = d
        return get_api_roles_response_200_item_featured_applications_item

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
