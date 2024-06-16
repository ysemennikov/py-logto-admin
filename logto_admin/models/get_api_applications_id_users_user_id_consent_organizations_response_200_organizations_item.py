from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item_custom_data import (
        GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItemCustomData,
    )


T = TypeVar("T", bound="GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem")


@_attrs_define
class GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItem:
    """
    Attributes:
        id (str):
        name (str):
        description (Union[None, str]):
        custom_data (GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItemCustomData):
            arbitrary
        created_at (float):
    """

    id: str
    name: str
    description: Union[None, str]
    custom_data: "GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItemCustomData"
    created_at: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, str]
        description = self.description

        custom_data = self.custom_data.to_dict()

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "customData": custom_data,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item_custom_data import (
            GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItemCustomData,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        custom_data = (
            GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200OrganizationsItemCustomData.from_dict(
                d.pop("customData")
            )
        )

        created_at = d.pop("createdAt")

        get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item = cls(
            id=id,
            name=name,
            description=description,
            custom_data=custom_data,
            created_at=created_at,
        )

        get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item.additional_properties = d
        return get_api_applications_id_users_user_id_consent_organizations_response_200_organizations_item

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
