from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_applications_application_id_user_consent_scopes_response_200_user_scopes_item import (
    GetApiApplicationsApplicationIdUserConsentScopesResponse200UserScopesItem,
)

if TYPE_CHECKING:
    from ..models.get_api_applications_application_id_user_consent_scopes_response_200_organization_resource_scopes_item import (
        GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationResourceScopesItem,
    )
    from ..models.get_api_applications_application_id_user_consent_scopes_response_200_organization_scopes_item import (
        GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationScopesItem,
    )
    from ..models.get_api_applications_application_id_user_consent_scopes_response_200_resource_scopes_item import (
        GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItem,
    )


T = TypeVar("T", bound="GetApiApplicationsApplicationIdUserConsentScopesResponse200")


@_attrs_define
class GetApiApplicationsApplicationIdUserConsentScopesResponse200:
    """
    Attributes:
        organization_scopes (List['GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationScopesItem']):
            A list of organization scope details assigned to the application.
        resource_scopes (List['GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItem']): A list
            of resource scope details grouped by resource id assigned to the application.
        organization_resource_scopes
            (List['GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationResourceScopesItem']): A list of
            organization resource scope details grouped by resource id assigned to the application.
        user_scopes (List[GetApiApplicationsApplicationIdUserConsentScopesResponse200UserScopesItem]): A list of user
            scope enum value assigned to the application.
    """

    organization_scopes: List["GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationScopesItem"]
    resource_scopes: List["GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItem"]
    organization_resource_scopes: List[
        "GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationResourceScopesItem"
    ]
    user_scopes: List[GetApiApplicationsApplicationIdUserConsentScopesResponse200UserScopesItem]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_scopes = []
        for organization_scopes_item_data in self.organization_scopes:
            organization_scopes_item = organization_scopes_item_data.to_dict()
            organization_scopes.append(organization_scopes_item)

        resource_scopes = []
        for resource_scopes_item_data in self.resource_scopes:
            resource_scopes_item = resource_scopes_item_data.to_dict()
            resource_scopes.append(resource_scopes_item)

        organization_resource_scopes = []
        for organization_resource_scopes_item_data in self.organization_resource_scopes:
            organization_resource_scopes_item = organization_resource_scopes_item_data.to_dict()
            organization_resource_scopes.append(organization_resource_scopes_item)

        user_scopes = []
        for user_scopes_item_data in self.user_scopes:
            user_scopes_item = user_scopes_item_data.value
            user_scopes.append(user_scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationScopes": organization_scopes,
                "resourceScopes": resource_scopes,
                "organizationResourceScopes": organization_resource_scopes,
                "userScopes": user_scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_applications_application_id_user_consent_scopes_response_200_organization_resource_scopes_item import (
            GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationResourceScopesItem,
        )
        from ..models.get_api_applications_application_id_user_consent_scopes_response_200_organization_scopes_item import (
            GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationScopesItem,
        )
        from ..models.get_api_applications_application_id_user_consent_scopes_response_200_resource_scopes_item import (
            GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItem,
        )

        d = src_dict.copy()
        organization_scopes = []
        _organization_scopes = d.pop("organizationScopes")
        for organization_scopes_item_data in _organization_scopes:
            organization_scopes_item = (
                GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationScopesItem.from_dict(
                    organization_scopes_item_data
                )
            )

            organization_scopes.append(organization_scopes_item)

        resource_scopes = []
        _resource_scopes = d.pop("resourceScopes")
        for resource_scopes_item_data in _resource_scopes:
            resource_scopes_item = (
                GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItem.from_dict(
                    resource_scopes_item_data
                )
            )

            resource_scopes.append(resource_scopes_item)

        organization_resource_scopes = []
        _organization_resource_scopes = d.pop("organizationResourceScopes")
        for organization_resource_scopes_item_data in _organization_resource_scopes:
            organization_resource_scopes_item = (
                GetApiApplicationsApplicationIdUserConsentScopesResponse200OrganizationResourceScopesItem.from_dict(
                    organization_resource_scopes_item_data
                )
            )

            organization_resource_scopes.append(organization_resource_scopes_item)

        user_scopes = []
        _user_scopes = d.pop("userScopes")
        for user_scopes_item_data in _user_scopes:
            user_scopes_item = GetApiApplicationsApplicationIdUserConsentScopesResponse200UserScopesItem(
                user_scopes_item_data
            )

            user_scopes.append(user_scopes_item)

        get_api_applications_application_id_user_consent_scopes_response_200 = cls(
            organization_scopes=organization_scopes,
            resource_scopes=resource_scopes,
            organization_resource_scopes=organization_resource_scopes,
            user_scopes=user_scopes,
        )

        get_api_applications_application_id_user_consent_scopes_response_200.additional_properties = d
        return get_api_applications_application_id_user_consent_scopes_response_200

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
