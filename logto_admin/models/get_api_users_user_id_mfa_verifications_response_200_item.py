from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_users_user_id_mfa_verifications_response_200_item_type import (
    GetApiUsersUserIdMfaVerificationsResponse200ItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiUsersUserIdMfaVerificationsResponse200Item")


@_attrs_define
class GetApiUsersUserIdMfaVerificationsResponse200Item:
    """
    Attributes:
        id (str):
        created_at (str):
        type (GetApiUsersUserIdMfaVerificationsResponse200ItemType):
        agent (Union[Unset, str]):
        remain_codes (Union[Unset, float]):
    """

    id: str
    created_at: str
    type: GetApiUsersUserIdMfaVerificationsResponse200ItemType
    agent: Union[Unset, str] = UNSET
    remain_codes: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        created_at = self.created_at

        type = self.type.value

        agent = self.agent

        remain_codes = self.remain_codes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "type": type,
            }
        )
        if agent is not UNSET:
            field_dict["agent"] = agent
        if remain_codes is not UNSET:
            field_dict["remainCodes"] = remain_codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_at = d.pop("createdAt")

        type = GetApiUsersUserIdMfaVerificationsResponse200ItemType(d.pop("type"))

        agent = d.pop("agent", UNSET)

        remain_codes = d.pop("remainCodes", UNSET)

        get_api_users_user_id_mfa_verifications_response_200_item = cls(
            id=id,
            created_at=created_at,
            type=type,
            agent=agent,
            remain_codes=remain_codes,
        )

        get_api_users_user_id_mfa_verifications_response_200_item.additional_properties = d
        return get_api_users_user_id_mfa_verifications_response_200_item

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
