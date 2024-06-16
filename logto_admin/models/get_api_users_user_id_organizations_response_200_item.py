from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_users_user_id_organizations_response_200_item_custom_data import (
        GetApiUsersUserIdOrganizationsResponse200ItemCustomData,
    )
    from ..models.get_api_users_user_id_organizations_response_200_item_organization_roles_item import (
        GetApiUsersUserIdOrganizationsResponse200ItemOrganizationRolesItem,
    )


T = TypeVar("T", bound="GetApiUsersUserIdOrganizationsResponse200Item")


@_attrs_define
class GetApiUsersUserIdOrganizationsResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        description (Union[None, str]):
        custom_data (GetApiUsersUserIdOrganizationsResponse200ItemCustomData): arbitrary
        created_at (float):
        organization_roles (List['GetApiUsersUserIdOrganizationsResponse200ItemOrganizationRolesItem']):
    """

    id: str
    name: str
    description: Union[None, str]
    custom_data: "GetApiUsersUserIdOrganizationsResponse200ItemCustomData"
    created_at: float
    organization_roles: List["GetApiUsersUserIdOrganizationsResponse200ItemOrganizationRolesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, str]
        description = self.description

        custom_data = self.custom_data.to_dict()

        created_at = self.created_at

        organization_roles = []
        for organization_roles_item_data in self.organization_roles:
            organization_roles_item = organization_roles_item_data.to_dict()
            organization_roles.append(organization_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "customData": custom_data,
                "createdAt": created_at,
                "organizationRoles": organization_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_users_user_id_organizations_response_200_item_custom_data import (
            GetApiUsersUserIdOrganizationsResponse200ItemCustomData,
        )
        from ..models.get_api_users_user_id_organizations_response_200_item_organization_roles_item import (
            GetApiUsersUserIdOrganizationsResponse200ItemOrganizationRolesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        custom_data = GetApiUsersUserIdOrganizationsResponse200ItemCustomData.from_dict(d.pop("customData"))

        created_at = d.pop("createdAt")

        organization_roles = []
        _organization_roles = d.pop("organizationRoles")
        for organization_roles_item_data in _organization_roles:
            organization_roles_item = GetApiUsersUserIdOrganizationsResponse200ItemOrganizationRolesItem.from_dict(
                organization_roles_item_data
            )

            organization_roles.append(organization_roles_item)

        get_api_users_user_id_organizations_response_200_item = cls(
            id=id,
            name=name,
            description=description,
            custom_data=custom_data,
            created_at=created_at,
            organization_roles=organization_roles,
        )

        get_api_users_user_id_organizations_response_200_item.additional_properties = d
        return get_api_users_user_id_organizations_response_200_item

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
