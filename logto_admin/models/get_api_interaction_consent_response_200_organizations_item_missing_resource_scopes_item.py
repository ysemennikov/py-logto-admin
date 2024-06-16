from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item_resource import (
        GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemResource,
    )
    from ..models.get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item_scopes_item import (
        GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemScopesItem,
    )


T = TypeVar("T", bound="GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem")


@_attrs_define
class GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem:
    """
    Attributes:
        resource (GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemResource):
        scopes (List['GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemScopesItem']):
    """

    resource: "GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemResource"
    scopes: List["GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemScopesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource = self.resource.to_dict()

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item_resource import (
            GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemResource,
        )
        from ..models.get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item_scopes_item import (
            GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemScopesItem,
        )

        d = src_dict.copy()
        resource = GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemResource.from_dict(
            d.pop("resource")
        )

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = (
                GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItemScopesItem.from_dict(
                    scopes_item_data
                )
            )

            scopes.append(scopes_item)

        get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item = cls(
            resource=resource,
            scopes=scopes,
        )

        get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item.additional_properties = d
        return get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item

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
