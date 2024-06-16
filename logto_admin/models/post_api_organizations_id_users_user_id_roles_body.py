from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiOrganizationsIdUsersUserIdRolesBody")


@_attrs_define
class PostApiOrganizationsIdUsersUserIdRolesBody:
    """
    Attributes:
        organization_role_ids (List[str]): An array of organization role IDs to assign to the user. User existed roles
            assignment will be ignored.
    """

    organization_role_ids: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_role_ids = self.organization_role_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationRoleIds": organization_role_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_role_ids = cast(List[str], d.pop("organizationRoleIds"))

        post_api_organizations_id_users_user_id_roles_body = cls(
            organization_role_ids=organization_role_ids,
        )

        post_api_organizations_id_users_user_id_roles_body.additional_properties = d
        return post_api_organizations_id_users_user_id_roles_body

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
