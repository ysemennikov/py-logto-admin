from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiUsersUserIdIdentitiesBodyConnectorData")


@_attrs_define
class PostApiUsersUserIdIdentitiesBodyConnectorData:
    """A json object constructed from the url query params returned by the social platform. Typically it contains `code`,
    `state` and `redirectUri` fields.

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        post_api_users_user_id_identities_body_connector_data = cls()

        post_api_users_user_id_identities_body_connector_data.additional_properties = d
        return post_api_users_user_id_identities_body_connector_data

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
