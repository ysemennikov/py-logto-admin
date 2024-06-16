from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiResourcesResourceIdScopesScopeIdResponse200")


@_attrs_define
class PatchApiResourcesResourceIdScopesScopeIdResponse200:
    """
    Attributes:
        id (str):
        resource_id (str):
        name (str):
        description (Union[None, str]):
        created_at (float):
    """

    id: str
    resource_id: str
    name: str
    description: Union[None, str]
    created_at: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        resource_id = self.resource_id

        name = self.name

        description: Union[None, str]
        description = self.description

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resourceId": resource_id,
                "name": name,
                "description": description,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        resource_id = d.pop("resourceId")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        created_at = d.pop("createdAt")

        patch_api_resources_resource_id_scopes_scope_id_response_200 = cls(
            id=id,
            resource_id=resource_id,
            name=name,
            description=description,
            created_at=created_at,
        )

        patch_api_resources_resource_id_scopes_scope_id_response_200.additional_properties = d
        return patch_api_resources_resource_id_scopes_scope_id_response_200

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
