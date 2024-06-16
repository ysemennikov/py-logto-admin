from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiApplicationsIdProtectedAppMetadataCustomDomainsBody")


@_attrs_define
class PostApiApplicationsIdProtectedAppMetadataCustomDomainsBody:
    """
    Attributes:
        domain (str): The domain to be added to the application.
    """

    domain: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain")

        post_api_applications_id_protected_app_metadata_custom_domains_body = cls(
            domain=domain,
        )

        post_api_applications_id_protected_app_metadata_custom_domains_body.additional_properties = d
        return post_api_applications_id_protected_app_metadata_custom_domains_body

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
