from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_organizations_id_users_response_200_item_custom_data import (
        GetApiOrganizationsIdUsersResponse200ItemCustomData,
    )
    from ..models.get_api_organizations_id_users_response_200_item_identities import (
        GetApiOrganizationsIdUsersResponse200ItemIdentities,
    )
    from ..models.get_api_organizations_id_users_response_200_item_organization_roles_item import (
        GetApiOrganizationsIdUsersResponse200ItemOrganizationRolesItem,
    )
    from ..models.get_api_organizations_id_users_response_200_item_profile import (
        GetApiOrganizationsIdUsersResponse200ItemProfile,
    )


T = TypeVar("T", bound="GetApiOrganizationsIdUsersResponse200Item")


@_attrs_define
class GetApiOrganizationsIdUsersResponse200Item:
    """
    Attributes:
        id (str):
        username (Union[None, str]):
        primary_email (Union[None, str]):
        primary_phone (Union[None, str]):
        name (Union[None, str]):
        avatar (Union[None, str]):
        custom_data (GetApiOrganizationsIdUsersResponse200ItemCustomData): arbitrary
        identities (GetApiOrganizationsIdUsersResponse200ItemIdentities):
        last_sign_in_at (Union[None, float]):
        created_at (float):
        updated_at (float):
        profile (GetApiOrganizationsIdUsersResponse200ItemProfile):
        application_id (Union[None, str]):
        is_suspended (bool):
        organization_roles (List['GetApiOrganizationsIdUsersResponse200ItemOrganizationRolesItem']):
    """

    id: str
    username: Union[None, str]
    primary_email: Union[None, str]
    primary_phone: Union[None, str]
    name: Union[None, str]
    avatar: Union[None, str]
    custom_data: "GetApiOrganizationsIdUsersResponse200ItemCustomData"
    identities: "GetApiOrganizationsIdUsersResponse200ItemIdentities"
    last_sign_in_at: Union[None, float]
    created_at: float
    updated_at: float
    profile: "GetApiOrganizationsIdUsersResponse200ItemProfile"
    application_id: Union[None, str]
    is_suspended: bool
    organization_roles: List["GetApiOrganizationsIdUsersResponse200ItemOrganizationRolesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        username: Union[None, str]
        username = self.username

        primary_email: Union[None, str]
        primary_email = self.primary_email

        primary_phone: Union[None, str]
        primary_phone = self.primary_phone

        name: Union[None, str]
        name = self.name

        avatar: Union[None, str]
        avatar = self.avatar

        custom_data = self.custom_data.to_dict()

        identities = self.identities.to_dict()

        last_sign_in_at: Union[None, float]
        last_sign_in_at = self.last_sign_in_at

        created_at = self.created_at

        updated_at = self.updated_at

        profile = self.profile.to_dict()

        application_id: Union[None, str]
        application_id = self.application_id

        is_suspended = self.is_suspended

        organization_roles = []
        for organization_roles_item_data in self.organization_roles:
            organization_roles_item = organization_roles_item_data.to_dict()
            organization_roles.append(organization_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "primaryEmail": primary_email,
                "primaryPhone": primary_phone,
                "name": name,
                "avatar": avatar,
                "customData": custom_data,
                "identities": identities,
                "lastSignInAt": last_sign_in_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "profile": profile,
                "applicationId": application_id,
                "isSuspended": is_suspended,
                "organizationRoles": organization_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_organizations_id_users_response_200_item_custom_data import (
            GetApiOrganizationsIdUsersResponse200ItemCustomData,
        )
        from ..models.get_api_organizations_id_users_response_200_item_identities import (
            GetApiOrganizationsIdUsersResponse200ItemIdentities,
        )
        from ..models.get_api_organizations_id_users_response_200_item_organization_roles_item import (
            GetApiOrganizationsIdUsersResponse200ItemOrganizationRolesItem,
        )
        from ..models.get_api_organizations_id_users_response_200_item_profile import (
            GetApiOrganizationsIdUsersResponse200ItemProfile,
        )

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_username(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        username = _parse_username(d.pop("username"))

        def _parse_primary_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        primary_email = _parse_primary_email(d.pop("primaryEmail"))

        def _parse_primary_phone(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        primary_phone = _parse_primary_phone(d.pop("primaryPhone"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        def _parse_avatar(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        avatar = _parse_avatar(d.pop("avatar"))

        custom_data = GetApiOrganizationsIdUsersResponse200ItemCustomData.from_dict(d.pop("customData"))

        identities = GetApiOrganizationsIdUsersResponse200ItemIdentities.from_dict(d.pop("identities"))

        def _parse_last_sign_in_at(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        last_sign_in_at = _parse_last_sign_in_at(d.pop("lastSignInAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        profile = GetApiOrganizationsIdUsersResponse200ItemProfile.from_dict(d.pop("profile"))

        def _parse_application_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        application_id = _parse_application_id(d.pop("applicationId"))

        is_suspended = d.pop("isSuspended")

        organization_roles = []
        _organization_roles = d.pop("organizationRoles")
        for organization_roles_item_data in _organization_roles:
            organization_roles_item = GetApiOrganizationsIdUsersResponse200ItemOrganizationRolesItem.from_dict(
                organization_roles_item_data
            )

            organization_roles.append(organization_roles_item)

        get_api_organizations_id_users_response_200_item = cls(
            id=id,
            username=username,
            primary_email=primary_email,
            primary_phone=primary_phone,
            name=name,
            avatar=avatar,
            custom_data=custom_data,
            identities=identities,
            last_sign_in_at=last_sign_in_at,
            created_at=created_at,
            updated_at=updated_at,
            profile=profile,
            application_id=application_id,
            is_suspended=is_suspended,
            organization_roles=organization_roles,
        )

        get_api_organizations_id_users_response_200_item.additional_properties = d
        return get_api_organizations_id_users_response_200_item

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
