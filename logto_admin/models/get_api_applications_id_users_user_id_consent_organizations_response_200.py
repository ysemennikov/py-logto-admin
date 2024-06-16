from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item import (
        GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem,
    )


T = TypeVar("T", bound="GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200")


@_attrs_define
class GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200:
    """
    Attributes:
        organizations (List['GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem']): A list
            of organization entities granted by the user for the application.
    """

    organizations: List["GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()
            organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizations": organizations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item import (
            GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem,
        )

        d = src_dict.copy()
        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = (
                GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem.from_dict(
                    organizations_item_data
                )
            )

            organizations.append(organizations_item)

        get_api_applications_id_users_user_id_consent_organizations_response_200 = cls(
            organizations=organizations,
        )

        get_api_applications_id_users_user_id_consent_organizations_response_200.additional_properties = d
        return get_api_applications_id_users_user_id_consent_organizations_response_200

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
