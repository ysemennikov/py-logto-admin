from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_interaction_consent_response_200_application import (
        GetApiInteractionConsentResponse200Application,
    )
    from ..models.get_api_interaction_consent_response_200_missing_resource_scopes_item import (
        GetApiInteractionConsentResponse200MissingResourceScopesItem,
    )
    from ..models.get_api_interaction_consent_response_200_organizations_item import (
        GetApiInteractionConsentResponse200OrganizationsItem,
    )
    from ..models.get_api_interaction_consent_response_200_user import GetApiInteractionConsentResponse200User


T = TypeVar("T", bound="GetApiInteractionConsentResponse200")


@_attrs_define
class GetApiInteractionConsentResponse200:
    """
    Attributes:
        application (GetApiInteractionConsentResponse200Application):
        user (GetApiInteractionConsentResponse200User):
        redirect_uri (str):
        organizations (Union[Unset, List['GetApiInteractionConsentResponse200OrganizationsItem']]):
        missing_oidc_scope (Union[Unset, List[str]]):
        missing_resource_scopes (Union[Unset, List['GetApiInteractionConsentResponse200MissingResourceScopesItem']]):
    """

    application: "GetApiInteractionConsentResponse200Application"
    user: "GetApiInteractionConsentResponse200User"
    redirect_uri: str
    organizations: Union[Unset, List["GetApiInteractionConsentResponse200OrganizationsItem"]] = UNSET
    missing_oidc_scope: Union[Unset, List[str]] = UNSET
    missing_resource_scopes: Union[Unset, List["GetApiInteractionConsentResponse200MissingResourceScopesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        application = self.application.to_dict()

        user = self.user.to_dict()

        redirect_uri = self.redirect_uri

        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        missing_oidc_scope: Union[Unset, List[str]] = UNSET
        if not isinstance(self.missing_oidc_scope, Unset):
            missing_oidc_scope = self.missing_oidc_scope

        missing_resource_scopes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.missing_resource_scopes, Unset):
            missing_resource_scopes = []
            for missing_resource_scopes_item_data in self.missing_resource_scopes:
                missing_resource_scopes_item = missing_resource_scopes_item_data.to_dict()
                missing_resource_scopes.append(missing_resource_scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application": application,
                "user": user,
                "redirectUri": redirect_uri,
            }
        )
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if missing_oidc_scope is not UNSET:
            field_dict["missingOIDCScope"] = missing_oidc_scope
        if missing_resource_scopes is not UNSET:
            field_dict["missingResourceScopes"] = missing_resource_scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_interaction_consent_response_200_application import (
            GetApiInteractionConsentResponse200Application,
        )
        from ..models.get_api_interaction_consent_response_200_missing_resource_scopes_item import (
            GetApiInteractionConsentResponse200MissingResourceScopesItem,
        )
        from ..models.get_api_interaction_consent_response_200_organizations_item import (
            GetApiInteractionConsentResponse200OrganizationsItem,
        )
        from ..models.get_api_interaction_consent_response_200_user import GetApiInteractionConsentResponse200User

        d = src_dict.copy()
        application = GetApiInteractionConsentResponse200Application.from_dict(d.pop("application"))

        user = GetApiInteractionConsentResponse200User.from_dict(d.pop("user"))

        redirect_uri = d.pop("redirectUri")

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = GetApiInteractionConsentResponse200OrganizationsItem.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        missing_oidc_scope = cast(List[str], d.pop("missingOIDCScope", UNSET))

        missing_resource_scopes = []
        _missing_resource_scopes = d.pop("missingResourceScopes", UNSET)
        for missing_resource_scopes_item_data in _missing_resource_scopes or []:
            missing_resource_scopes_item = GetApiInteractionConsentResponse200MissingResourceScopesItem.from_dict(
                missing_resource_scopes_item_data
            )

            missing_resource_scopes.append(missing_resource_scopes_item)

        get_api_interaction_consent_response_200 = cls(
            application=application,
            user=user,
            redirect_uri=redirect_uri,
            organizations=organizations,
            missing_oidc_scope=missing_oidc_scope,
            missing_resource_scopes=missing_resource_scopes,
        )

        get_api_interaction_consent_response_200.additional_properties = d
        return get_api_interaction_consent_response_200

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
