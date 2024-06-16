from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_organizations_id_users_response_200_item_identities_additional_property import (
        GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty,
    )


T = TypeVar("T", bound="GetApiOrganizationsIdUsersResponse200ItemIdentities")


@_attrs_define
class GetApiOrganizationsIdUsersResponse200ItemIdentities:
    """ """

    additional_properties: Dict[str, "GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty"] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_organizations_id_users_response_200_item_identities_additional_property import (
            GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty,
        )

        d = src_dict.copy()
        get_api_organizations_id_users_response_200_item_identities = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        get_api_organizations_id_users_response_200_item_identities.additional_properties = additional_properties
        return get_api_organizations_id_users_response_200_item_identities

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: "GetApiOrganizationsIdUsersResponse200ItemIdentitiesAdditionalProperty"
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
