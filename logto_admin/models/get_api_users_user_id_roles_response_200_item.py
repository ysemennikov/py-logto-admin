from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_users_user_id_roles_response_200_item_type import GetApiUsersUserIdRolesResponse200ItemType

T = TypeVar("T", bound="GetApiUsersUserIdRolesResponse200Item")


@_attrs_define
class GetApiUsersUserIdRolesResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        type (GetApiUsersUserIdRolesResponse200ItemType):
        is_default (bool):
    """

    id: str
    name: str
    description: str
    type: GetApiUsersUserIdRolesResponse200ItemType
    is_default: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        type = self.type.value

        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "type": type,
                "isDefault": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        type = GetApiUsersUserIdRolesResponse200ItemType(d.pop("type"))

        is_default = d.pop("isDefault")

        get_api_users_user_id_roles_response_200_item = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            is_default=is_default,
        )

        get_api_users_user_id_roles_response_200_item.additional_properties = d
        return get_api_users_user_id_roles_response_200_item

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
