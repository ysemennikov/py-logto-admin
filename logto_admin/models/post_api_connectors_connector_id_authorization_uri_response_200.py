from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiConnectorsConnectorIdAuthorizationUriResponse200")


@_attrs_define
class PostApiConnectorsConnectorIdAuthorizationUriResponse200:
    """
    Attributes:
        redirect_to (str):
        redirect_uri (Union[Unset, Any]): The URI to navigate for authentication and authorization in the connected
            social identity provider.
    """

    redirect_to: str
    redirect_uri: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        redirect_to = self.redirect_to

        redirect_uri = self.redirect_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redirectTo": redirect_to,
            }
        )
        if redirect_uri is not UNSET:
            field_dict["redirectUri"] = redirect_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        redirect_to = d.pop("redirectTo")

        redirect_uri = d.pop("redirectUri", UNSET)

        post_api_connectors_connector_id_authorization_uri_response_200 = cls(
            redirect_to=redirect_to,
            redirect_uri=redirect_uri,
        )

        post_api_connectors_connector_id_authorization_uri_response_200.additional_properties = d
        return post_api_connectors_connector_id_authorization_uri_response_200

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
