from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_users_user_id_identities_body_connector_data import (
        PostApiUsersUserIdIdentitiesBodyConnectorData,
    )


T = TypeVar("T", bound="PostApiUsersUserIdIdentitiesBody")


@_attrs_define
class PostApiUsersUserIdIdentitiesBody:
    """
    Attributes:
        connector_id (str): The Logto connector ID.
        connector_data (PostApiUsersUserIdIdentitiesBodyConnectorData): A json object constructed from the url query
            params returned by the social platform. Typically it contains `code`, `state` and `redirectUri` fields.
    """

    connector_id: str
    connector_data: "PostApiUsersUserIdIdentitiesBodyConnectorData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        connector_data = self.connector_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
                "connectorData": connector_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_users_user_id_identities_body_connector_data import (
            PostApiUsersUserIdIdentitiesBodyConnectorData,
        )

        d = src_dict.copy()
        connector_id = d.pop("connectorId")

        connector_data = PostApiUsersUserIdIdentitiesBodyConnectorData.from_dict(d.pop("connectorData"))

        post_api_users_user_id_identities_body = cls(
            connector_id=connector_id,
            connector_data=connector_data,
        )

        post_api_users_user_id_identities_body.additional_properties = d
        return post_api_users_user_id_identities_body

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
