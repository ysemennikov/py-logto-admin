from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_organization_invitations_body_message_payload_type_0 import (
        PostApiOrganizationInvitationsBodyMessagePayloadType0,
    )


T = TypeVar("T", bound="PostApiOrganizationInvitationsBody")


@_attrs_define
class PostApiOrganizationInvitationsBody:
    """
    Attributes:
        invitee (str): The email address of the user to invite to join the organization.
        organization_id (str): The ID of the organization to invite the user to join.
        expires_at (float): The epoch time in milliseconds when the invitation expires.
        message_payload (Union['PostApiOrganizationInvitationsBodyMessagePayloadType0', bool]): The message payload for
            the "OrganizationInvitation" template to use when sending the invitation via email. If it is `false`, the
            invitation will not be sent via email. Default: False.
        inviter_id (Union[None, Unset, str]): The ID of the user who is inviting the user to join the organization.
        organization_role_ids (Union[Unset, List[str]]): The IDs of the organization roles to assign to the user when
            they accept the invitation.
    """

    invitee: str
    organization_id: str
    expires_at: float
    message_payload: Union["PostApiOrganizationInvitationsBodyMessagePayloadType0", bool] = False
    inviter_id: Union[None, Unset, str] = UNSET
    organization_role_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.post_api_organization_invitations_body_message_payload_type_0 import (
            PostApiOrganizationInvitationsBodyMessagePayloadType0,
        )

        invitee = self.invitee

        organization_id = self.organization_id

        expires_at = self.expires_at

        message_payload: Union[Dict[str, Any], bool]
        if isinstance(self.message_payload, PostApiOrganizationInvitationsBodyMessagePayloadType0):
            message_payload = self.message_payload.to_dict()
        else:
            message_payload = self.message_payload

        inviter_id: Union[None, Unset, str]
        if isinstance(self.inviter_id, Unset):
            inviter_id = UNSET
        else:
            inviter_id = self.inviter_id

        organization_role_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organization_role_ids, Unset):
            organization_role_ids = self.organization_role_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invitee": invitee,
                "organizationId": organization_id,
                "expiresAt": expires_at,
                "messagePayload": message_payload,
            }
        )
        if inviter_id is not UNSET:
            field_dict["inviterId"] = inviter_id
        if organization_role_ids is not UNSET:
            field_dict["organizationRoleIds"] = organization_role_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_organization_invitations_body_message_payload_type_0 import (
            PostApiOrganizationInvitationsBodyMessagePayloadType0,
        )

        d = src_dict.copy()
        invitee = d.pop("invitee")

        organization_id = d.pop("organizationId")

        expires_at = d.pop("expiresAt")

        def _parse_message_payload(
            data: object,
        ) -> Union["PostApiOrganizationInvitationsBodyMessagePayloadType0", bool]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_payload_type_0 = PostApiOrganizationInvitationsBodyMessagePayloadType0.from_dict(data)

                return message_payload_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PostApiOrganizationInvitationsBodyMessagePayloadType0", bool], data)

        message_payload = _parse_message_payload(d.pop("messagePayload"))

        def _parse_inviter_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inviter_id = _parse_inviter_id(d.pop("inviterId", UNSET))

        organization_role_ids = cast(List[str], d.pop("organizationRoleIds", UNSET))

        post_api_organization_invitations_body = cls(
            invitee=invitee,
            organization_id=organization_id,
            expires_at=expires_at,
            message_payload=message_payload,
            inviter_id=inviter_id,
            organization_role_ids=organization_role_ids,
        )

        post_api_organization_invitations_body.additional_properties = d
        return post_api_organization_invitations_body

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
