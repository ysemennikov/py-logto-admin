from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item import (
        GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem,
    )


T = TypeVar("T", bound="GetApiInteractionConsentResponse200OrganizationsItem")


@_attrs_define
class GetApiInteractionConsentResponse200OrganizationsItem:
    """
    Attributes:
        id (str):
        name (str):
        missing_resource_scopes (Union[Unset,
            List['GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem']]):
    """

    id: str
    name: str
    missing_resource_scopes: Union[
        Unset, List["GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

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
                "id": id,
                "name": name,
            }
        )
        if missing_resource_scopes is not UNSET:
            field_dict["missingResourceScopes"] = missing_resource_scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_interaction_consent_response_200_organizations_item_missing_resource_scopes_item import (
            GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        missing_resource_scopes = []
        _missing_resource_scopes = d.pop("missingResourceScopes", UNSET)
        for missing_resource_scopes_item_data in _missing_resource_scopes or []:
            missing_resource_scopes_item = (
                GetApiInteractionConsentResponse200OrganizationsItemMissingResourceScopesItem.from_dict(
                    missing_resource_scopes_item_data
                )
            )

            missing_resource_scopes.append(missing_resource_scopes_item)

        get_api_interaction_consent_response_200_organizations_item = cls(
            id=id,
            name=name,
            missing_resource_scopes=missing_resource_scopes,
        )

        get_api_interaction_consent_response_200_organizations_item.additional_properties = d
        return get_api_interaction_consent_response_200_organizations_item

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
