from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_organization_roles_response_200_item_resource_scopes_item import (
        GetApiOrganizationRolesResponse200ItemResourceScopesItem,
    )
    from ..models.get_api_organization_roles_response_200_item_scopes_item import (
        GetApiOrganizationRolesResponse200ItemScopesItem,
    )


T = TypeVar("T", bound="GetApiOrganizationRolesResponse200Item")


@_attrs_define
class GetApiOrganizationRolesResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        description (Union[None, str]):
        scopes (List['GetApiOrganizationRolesResponse200ItemScopesItem']):
        resource_scopes (List['GetApiOrganizationRolesResponse200ItemResourceScopesItem']):
    """

    id: str
    name: str
    description: Union[None, str]
    scopes: List["GetApiOrganizationRolesResponse200ItemScopesItem"]
    resource_scopes: List["GetApiOrganizationRolesResponse200ItemResourceScopesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, str]
        description = self.description

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        resource_scopes = []
        for resource_scopes_item_data in self.resource_scopes:
            resource_scopes_item = resource_scopes_item_data.to_dict()
            resource_scopes.append(resource_scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "scopes": scopes,
                "resourceScopes": resource_scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_organization_roles_response_200_item_resource_scopes_item import (
            GetApiOrganizationRolesResponse200ItemResourceScopesItem,
        )
        from ..models.get_api_organization_roles_response_200_item_scopes_item import (
            GetApiOrganizationRolesResponse200ItemScopesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = GetApiOrganizationRolesResponse200ItemScopesItem.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        resource_scopes = []
        _resource_scopes = d.pop("resourceScopes")
        for resource_scopes_item_data in _resource_scopes:
            resource_scopes_item = GetApiOrganizationRolesResponse200ItemResourceScopesItem.from_dict(
                resource_scopes_item_data
            )

            resource_scopes.append(resource_scopes_item)

        get_api_organization_roles_response_200_item = cls(
            id=id,
            name=name,
            description=description,
            scopes=scopes,
            resource_scopes=resource_scopes,
        )

        get_api_organization_roles_response_200_item.additional_properties = d
        return get_api_organization_roles_response_200_item

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
