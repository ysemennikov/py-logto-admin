from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_users_user_id_response_200_identities_additional_property import (
        PatchApiUsersUserIdResponse200IdentitiesAdditionalProperty,
    )


T = TypeVar("T", bound="PatchApiUsersUserIdResponse200Identities")


@_attrs_define
class PatchApiUsersUserIdResponse200Identities:
    """ """

    additional_properties: Dict[str, "PatchApiUsersUserIdResponse200IdentitiesAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_users_user_id_response_200_identities_additional_property import (
            PatchApiUsersUserIdResponse200IdentitiesAdditionalProperty,
        )

        d = src_dict.copy()
        patch_api_users_user_id_response_200_identities = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PatchApiUsersUserIdResponse200IdentitiesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        patch_api_users_user_id_response_200_identities.additional_properties = additional_properties
        return patch_api_users_user_id_response_200_identities

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "PatchApiUsersUserIdResponse200IdentitiesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "PatchApiUsersUserIdResponse200IdentitiesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
