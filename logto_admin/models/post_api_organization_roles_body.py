from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiOrganizationRolesBody")


@_attrs_define
class PostApiOrganizationRolesBody:
    """
    Attributes:
        name (str): The name of the organization role. It must be unique within the organization template.
        organization_scope_ids (List[str]): An array of organization scope IDs to be assigned to the organization role.
        resource_scope_ids (List[str]): An array of resource scope IDs to be assigned to the organization role.
        description (Union[None, Unset, str]): The description of the organization role.
    """

    name: str
    organization_scope_ids: List[str]
    resource_scope_ids: List[str]
    description: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        organization_scope_ids = self.organization_scope_ids

        resource_scope_ids = self.resource_scope_ids

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organizationScopeIds": organization_scope_ids,
                "resourceScopeIds": resource_scope_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_scope_ids = cast(List[str], d.pop("organizationScopeIds"))

        resource_scope_ids = cast(List[str], d.pop("resourceScopeIds"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        post_api_organization_roles_body = cls(
            name=name,
            organization_scope_ids=organization_scope_ids,
            resource_scope_ids=resource_scope_ids,
            description=description,
        )

        post_api_organization_roles_body.additional_properties = d
        return post_api_organization_roles_body

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
