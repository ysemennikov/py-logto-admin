from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAuthnSingleSignOnSamlConnectorIdBody")


@_attrs_define
class PostApiAuthnSingleSignOnSamlConnectorIdBody:
    """
    Attributes:
        relay_state (str): SAML standard parameter that will be transmitted between the identity provider and the
            service provider. It will be used as the session ID (jti) of the user's Logto authentication session. This API
            will use this session ID to retrieve the SSO connector authentication session from the database.
        saml_response (str): The SAML assertion response from the identity provider (IdP).
    """

    relay_state: str
    saml_response: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relay_state = self.relay_state

        saml_response = self.saml_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "RelayState": relay_state,
                "SAMLResponse": saml_response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        relay_state = d.pop("RelayState")

        saml_response = d.pop("SAMLResponse")

        post_api_authn_single_sign_on_saml_connector_id_body = cls(
            relay_state=relay_state,
            saml_response=saml_response,
        )

        post_api_authn_single_sign_on_saml_connector_id_body.additional_properties = d
        return post_api_authn_single_sign_on_saml_connector_id_body

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
