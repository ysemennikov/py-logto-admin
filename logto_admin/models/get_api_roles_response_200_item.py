from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_roles_response_200_item_type import GetApiRolesResponse200ItemType

if TYPE_CHECKING:
    from ..models.get_api_roles_response_200_item_featured_applications_item import (
        GetApiRolesResponse200ItemFeaturedApplicationsItem,
    )
    from ..models.get_api_roles_response_200_item_featured_users_item import GetApiRolesResponse200ItemFeaturedUsersItem


T = TypeVar("T", bound="GetApiRolesResponse200Item")


@_attrs_define
class GetApiRolesResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        type (GetApiRolesResponse200ItemType):
        is_default (bool):
        users_count (float):
        featured_users (List['GetApiRolesResponse200ItemFeaturedUsersItem']):
        applications_count (float):
        featured_applications (List['GetApiRolesResponse200ItemFeaturedApplicationsItem']):
    """

    id: str
    name: str
    description: str
    type: GetApiRolesResponse200ItemType
    is_default: bool
    users_count: float
    featured_users: List["GetApiRolesResponse200ItemFeaturedUsersItem"]
    applications_count: float
    featured_applications: List["GetApiRolesResponse200ItemFeaturedApplicationsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        type = self.type.value

        is_default = self.is_default

        users_count = self.users_count

        featured_users = []
        for featured_users_item_data in self.featured_users:
            featured_users_item = featured_users_item_data.to_dict()
            featured_users.append(featured_users_item)

        applications_count = self.applications_count

        featured_applications = []
        for featured_applications_item_data in self.featured_applications:
            featured_applications_item = featured_applications_item_data.to_dict()
            featured_applications.append(featured_applications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "type": type,
                "isDefault": is_default,
                "usersCount": users_count,
                "featuredUsers": featured_users,
                "applicationsCount": applications_count,
                "featuredApplications": featured_applications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_roles_response_200_item_featured_applications_item import (
            GetApiRolesResponse200ItemFeaturedApplicationsItem,
        )
        from ..models.get_api_roles_response_200_item_featured_users_item import (
            GetApiRolesResponse200ItemFeaturedUsersItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        type = GetApiRolesResponse200ItemType(d.pop("type"))

        is_default = d.pop("isDefault")

        users_count = d.pop("usersCount")

        featured_users = []
        _featured_users = d.pop("featuredUsers")
        for featured_users_item_data in _featured_users:
            featured_users_item = GetApiRolesResponse200ItemFeaturedUsersItem.from_dict(featured_users_item_data)

            featured_users.append(featured_users_item)

        applications_count = d.pop("applicationsCount")

        featured_applications = []
        _featured_applications = d.pop("featuredApplications")
        for featured_applications_item_data in _featured_applications:
            featured_applications_item = GetApiRolesResponse200ItemFeaturedApplicationsItem.from_dict(
                featured_applications_item_data
            )

            featured_applications.append(featured_applications_item)

        get_api_roles_response_200_item = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            is_default=is_default,
            users_count=users_count,
            featured_users=featured_users,
            applications_count=applications_count,
            featured_applications=featured_applications,
        )

        get_api_roles_response_200_item.additional_properties = d
        return get_api_roles_response_200_item

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
