from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_roles_id_response_200_type import PatchApiRolesIdResponse200Type

T = TypeVar("T", bound="PatchApiRolesIdResponse200")


@_attrs_define
class PatchApiRolesIdResponse200:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        type (PatchApiRolesIdResponse200Type):
        is_default (bool):
    """

    id: str
    name: str
    description: str
    type: PatchApiRolesIdResponse200Type
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

        type = PatchApiRolesIdResponse200Type(d.pop("type"))

        is_default = d.pop("isDefault")

        patch_api_roles_id_response_200 = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            is_default=is_default,
        )

        patch_api_roles_id_response_200.additional_properties = d
        return patch_api_roles_id_response_200

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
