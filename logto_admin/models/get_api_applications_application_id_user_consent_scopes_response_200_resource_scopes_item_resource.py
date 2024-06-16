from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItemResource")


@_attrs_define
class GetApiApplicationsApplicationIdUserConsentScopesResponse200ResourceScopesItemResource:
    """
    Attributes:
        id (str):
        name (str):
        indicator (str):
    """

    id: str
    name: str
    indicator: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        indicator = self.indicator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "indicator": indicator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        indicator = d.pop("indicator")

        get_api_applications_application_id_user_consent_scopes_response_200_resource_scopes_item_resource = cls(
            id=id,
            name=name,
            indicator=indicator,
        )

        get_api_applications_application_id_user_consent_scopes_response_200_resource_scopes_item_resource.additional_properties = d
        return get_api_applications_application_id_user_consent_scopes_response_200_resource_scopes_item_resource

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
