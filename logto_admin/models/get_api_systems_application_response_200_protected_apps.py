from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiSystemsApplicationResponse200ProtectedApps")


@_attrs_define
class GetApiSystemsApplicationResponse200ProtectedApps:
    """
    Attributes:
        default_domain (str):
    """

    default_domain: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_domain = self.default_domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultDomain": default_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_domain = d.pop("defaultDomain")

        get_api_systems_application_response_200_protected_apps = cls(
            default_domain=default_domain,
        )

        get_api_systems_application_response_200_protected_apps.additional_properties = d
        return get_api_systems_application_response_200_protected_apps

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
