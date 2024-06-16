from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_users_user_id_identities_target_body_details import (
        PutApiUsersUserIdIdentitiesTargetBodyDetails,
    )


T = TypeVar("T", bound="PutApiUsersUserIdIdentitiesTargetBody")


@_attrs_define
class PutApiUsersUserIdIdentitiesTargetBody:
    """
    Attributes:
        user_id (str): The user's social identity ID.
        details (Union[Unset, PutApiUsersUserIdIdentitiesTargetBodyDetails]): The user's social identity details.
    """

    user_id: str
    details: Union[Unset, "PutApiUsersUserIdIdentitiesTargetBodyDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_users_user_id_identities_target_body_details import (
            PutApiUsersUserIdIdentitiesTargetBodyDetails,
        )

        d = src_dict.copy()
        user_id = d.pop("userId")

        _details = d.pop("details", UNSET)
        details: Union[Unset, PutApiUsersUserIdIdentitiesTargetBodyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PutApiUsersUserIdIdentitiesTargetBodyDetails.from_dict(_details)

        put_api_users_user_id_identities_target_body = cls(
            user_id=user_id,
            details=details,
        )

        put_api_users_user_id_identities_target_body.additional_properties = d
        return put_api_users_user_id_identities_target_body

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
