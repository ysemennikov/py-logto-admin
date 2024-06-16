from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiApplicationsResponse200OidcClientMetadataRedirectUrisItemType1")


@_attrs_define
class PostApiApplicationsResponse200OidcClientMetadataRedirectUrisItemType1:
    """Validator function"""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        post_api_applications_response_200_oidc_client_metadata_redirect_uris_item_type_1 = cls()

        post_api_applications_response_200_oidc_client_metadata_redirect_uris_item_type_1.additional_properties = d
        return post_api_applications_response_200_oidc_client_metadata_redirect_uris_item_type_1

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
