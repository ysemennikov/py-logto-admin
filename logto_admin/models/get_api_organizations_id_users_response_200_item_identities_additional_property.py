from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_organizations_id_users_response_200_item_identities_additional_property_details import (
        GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalPropertyDetails,
    )


T = TypeVar("T", bound="GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty")


@_attrs_define
class GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty:
    """
    Attributes:
        user_id (str):
        details (Union[Unset, GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalPropertyDetails]): arbitrary
    """

    user_id: str
    details: Union[Unset, "GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalPropertyDetails"] = UNSET
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
        from ..models.get_api_organizations_id_users_response_200_item_identities_additional_property_details import (
            GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalPropertyDetails,
        )

        d = src_dict.copy()
        user_id = d.pop("userId")

        _details = d.pop("details", UNSET)
        details: Union[Unset, GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalPropertyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalPropertyDetails.from_dict(_details)

        get_api_organizations_id_users_response_200_item_identities_additional_property = cls(
            user_id=user_id,
            details=details,
        )

        get_api_organizations_id_users_response_200_item_identities_additional_property.additional_properties = d
        return get_api_organizations_id_users_response_200_item_identities_additional_property

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
