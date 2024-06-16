from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiApplicationsBodyProtectedAppMetadata")


@_attrs_define
class PostApiApplicationsBodyProtectedAppMetadata:
    """The data for protected app, this feature is not available for open source version.

    Attributes:
        sub_domain (str): The subdomain prefix, e.g., my-site.
        origin (str): The origin of target website, e.g., https://example.com.
    """

    sub_domain: str
    origin: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_domain = self.sub_domain

        origin = self.origin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subDomain": sub_domain,
                "origin": origin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_domain = d.pop("subDomain")

        origin = d.pop("origin")

        post_api_applications_body_protected_app_metadata = cls(
            sub_domain=sub_domain,
            origin=origin,
        )

        post_api_applications_body_protected_app_metadata.additional_properties = d
        return post_api_applications_body_protected_app_metadata

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
