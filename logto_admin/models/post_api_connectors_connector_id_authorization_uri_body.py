from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiConnectorsConnectorIdAuthorizationUriBody")


@_attrs_define
class PostApiConnectorsConnectorIdAuthorizationUriBody:
    """
    Attributes:
        state (str): A random string generated on the client side to prevent CSRF (Cross-Site Request Forgery) attacks.
        redirect_uri (str): The URI to navigate back to after the user is authenticated by the connected social identity
            provider and has granted access to the connector.
    """

    state: str
    redirect_uri: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state

        redirect_uri = self.redirect_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "redirectUri": redirect_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state")

        redirect_uri = d.pop("redirectUri")

        post_api_connectors_connector_id_authorization_uri_body = cls(
            state=state,
            redirect_uri=redirect_uri,
        )

        post_api_connectors_connector_id_authorization_uri_body.additional_properties = d
        return post_api_connectors_connector_id_authorization_uri_body

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
