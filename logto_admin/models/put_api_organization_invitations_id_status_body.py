from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_organization_invitations_id_status_body_status import (
    PutApiOrganizationInvitationsIdStatusBodyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiOrganizationInvitationsIdStatusBody")


@_attrs_define
class PutApiOrganizationInvitationsIdStatusBody:
    """
    Attributes:
        status (PutApiOrganizationInvitationsIdStatusBodyStatus): The status of the organization invitation.
        accepted_user_id (Union[None, Unset, str]): The ID of the user who accepted the organization invitation.
            Required if the status is "Accepted".
    """

    status: PutApiOrganizationInvitationsIdStatusBodyStatus
    accepted_user_id: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        accepted_user_id: Union[None, Unset, str]
        if isinstance(self.accepted_user_id, Unset):
            accepted_user_id = UNSET
        else:
            accepted_user_id = self.accepted_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if accepted_user_id is not UNSET:
            field_dict["acceptedUserId"] = accepted_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = PutApiOrganizationInvitationsIdStatusBodyStatus(d.pop("status"))

        def _parse_accepted_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        accepted_user_id = _parse_accepted_user_id(d.pop("acceptedUserId", UNSET))

        put_api_organization_invitations_id_status_body = cls(
            status=status,
            accepted_user_id=accepted_user_id,
        )

        put_api_organization_invitations_id_status_body.additional_properties = d
        return put_api_organization_invitations_id_status_body

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
