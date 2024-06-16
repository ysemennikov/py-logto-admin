from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_users_user_id_custom_data_body_custom_data import (
        PatchApiUsersUserIdCustomDataBodyCustomData,
    )


T = TypeVar("T", bound="PatchApiUsersUserIdCustomDataBody")


@_attrs_define
class PatchApiUsersUserIdCustomDataBody:
    """
    Attributes:
        custom_data (PatchApiUsersUserIdCustomDataBodyCustomData): Partial custom data object to update for the given
            user ID.
    """

    custom_data: "PatchApiUsersUserIdCustomDataBodyCustomData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_data = self.custom_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customData": custom_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_users_user_id_custom_data_body_custom_data import (
            PatchApiUsersUserIdCustomDataBodyCustomData,
        )

        d = src_dict.copy()
        custom_data = PatchApiUsersUserIdCustomDataBodyCustomData.from_dict(d.pop("customData"))

        patch_api_users_user_id_custom_data_body = cls(
            custom_data=custom_data,
        )

        patch_api_users_user_id_custom_data_body.additional_properties = d
        return patch_api_users_user_id_custom_data_body

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
