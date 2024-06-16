from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_organizations_response_200_item_custom_data import (
        GetApiOrganizationsResponse200ItemCustomData,
    )
    from ..models.get_api_organizations_response_200_item_featured_users_item import (
        GetApiOrganizationsResponse200ItemFeaturedUsersItem,
    )


T = TypeVar("T", bound="GetApiOrganizationsResponse200Item")


@_attrs_define
class GetApiOrganizationsResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        description (Union[None, str]):
        custom_data (GetApiOrganizationsResponse200ItemCustomData): arbitrary
        created_at (float):
        users_count (Union[Unset, float]):
        featured_users (Union[Unset, List['GetApiOrganizationsResponse200ItemFeaturedUsersItem']]):
    """

    id: str
    name: str
    description: Union[None, str]
    custom_data: "GetApiOrganizationsResponse200ItemCustomData"
    created_at: float
    users_count: Union[Unset, float] = UNSET
    featured_users: Union[Unset, List["GetApiOrganizationsResponse200ItemFeaturedUsersItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, str]
        description = self.description

        custom_data = self.custom_data.to_dict()

        created_at = self.created_at

        users_count = self.users_count

        featured_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.featured_users, Unset):
            featured_users = []
            for featured_users_item_data in self.featured_users:
                featured_users_item = featured_users_item_data.to_dict()
                featured_users.append(featured_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "customData": custom_data,
                "createdAt": created_at,
            }
        )
        if users_count is not UNSET:
            field_dict["usersCount"] = users_count
        if featured_users is not UNSET:
            field_dict["featuredUsers"] = featured_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_organizations_response_200_item_custom_data import (
            GetApiOrganizationsResponse200ItemCustomData,
        )
        from ..models.get_api_organizations_response_200_item_featured_users_item import (
            GetApiOrganizationsResponse200ItemFeaturedUsersItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        custom_data = GetApiOrganizationsResponse200ItemCustomData.from_dict(d.pop("customData"))

        created_at = d.pop("createdAt")

        users_count = d.pop("usersCount", UNSET)

        featured_users = []
        _featured_users = d.pop("featuredUsers", UNSET)
        for featured_users_item_data in _featured_users or []:
            featured_users_item = GetApiOrganizationsResponse200ItemFeaturedUsersItem.from_dict(
                featured_users_item_data
            )

            featured_users.append(featured_users_item)

        get_api_organizations_response_200_item = cls(
            id=id,
            name=name,
            description=description,
            custom_data=custom_data,
            created_at=created_at,
            users_count=users_count,
            featured_users=featured_users,
        )

        get_api_organizations_response_200_item.additional_properties = d
        return get_api_organizations_response_200_item

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
