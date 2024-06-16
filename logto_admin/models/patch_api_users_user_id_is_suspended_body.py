from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiUsersUserIdIsSuspendedBody")


@_attrs_define
class PatchApiUsersUserIdIsSuspendedBody:
    """
    Attributes:
        is_suspended (bool): New suspension status for the user.
    """

    is_suspended: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_suspended = self.is_suspended

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isSuspended": is_suspended,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_suspended = d.pop("isSuspended")

        patch_api_users_user_id_is_suspended_body = cls(
            is_suspended=is_suspended,
        )

        patch_api_users_user_id_is_suspended_body.additional_properties = d
        return patch_api_users_user_id_is_suspended_body

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
