from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_organization_invitations_id_status_response_200_status import (
    PutApiOrganizationInvitationsIdStatusResponse200Status,
)

if TYPE_CHECKING:
    from ..models.put_api_organization_invitations_id_status_response_200_organization_roles_item import (
        PutApiOrganizationInvitationsIdStatusResponse200OrganizationRolesItem,
    )


T = TypeVar("T", bound="PutApiOrganizationInvitationsIdStatusResponse200")


@_attrs_define
class PutApiOrganizationInvitationsIdStatusResponse200:
    """
    Attributes:
        id (str):
        inviter_id (Union[None, str]):
        invitee (str):
        accepted_user_id (Union[None, str]):
        organization_id (str):
        status (PutApiOrganizationInvitationsIdStatusResponse200Status):
        created_at (float):
        updated_at (float):
        expires_at (float):
        organization_roles (List['PutApiOrganizationInvitationsIdStatusResponse200OrganizationRolesItem']):
    """

    id: str
    inviter_id: Union[None, str]
    invitee: str
    accepted_user_id: Union[None, str]
    organization_id: str
    status: PutApiOrganizationInvitationsIdStatusResponse200Status
    created_at: float
    updated_at: float
    expires_at: float
    organization_roles: List["PutApiOrganizationInvitationsIdStatusResponse200OrganizationRolesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        inviter_id: Union[None, str]
        inviter_id = self.inviter_id

        invitee = self.invitee

        accepted_user_id: Union[None, str]
        accepted_user_id = self.accepted_user_id

        organization_id = self.organization_id

        status = self.status.value

        created_at = self.created_at

        updated_at = self.updated_at

        expires_at = self.expires_at

        organization_roles = []
        for organization_roles_item_data in self.organization_roles:
            organization_roles_item = organization_roles_item_data.to_dict()
            organization_roles.append(organization_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "inviterId": inviter_id,
                "invitee": invitee,
                "acceptedUserId": accepted_user_id,
                "organizationId": organization_id,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "expiresAt": expires_at,
                "organizationRoles": organization_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_organization_invitations_id_status_response_200_organization_roles_item import (
            PutApiOrganizationInvitationsIdStatusResponse200OrganizationRolesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_inviter_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        inviter_id = _parse_inviter_id(d.pop("inviterId"))

        invitee = d.pop("invitee")

        def _parse_accepted_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        accepted_user_id = _parse_accepted_user_id(d.pop("acceptedUserId"))

        organization_id = d.pop("organizationId")

        status = PutApiOrganizationInvitationsIdStatusResponse200Status(d.pop("status"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        expires_at = d.pop("expiresAt")

        organization_roles = []
        _organization_roles = d.pop("organizationRoles")
        for organization_roles_item_data in _organization_roles:
            organization_roles_item = PutApiOrganizationInvitationsIdStatusResponse200OrganizationRolesItem.from_dict(
                organization_roles_item_data
            )

            organization_roles.append(organization_roles_item)

        put_api_organization_invitations_id_status_response_200 = cls(
            id=id,
            inviter_id=inviter_id,
            invitee=invitee,
            accepted_user_id=accepted_user_id,
            organization_id=organization_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            expires_at=expires_at,
            organization_roles=organization_roles,
        )

        put_api_organization_invitations_id_status_response_200.additional_properties = d
        return put_api_organization_invitations_id_status_response_200

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
