from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_interaction_single_sign_on_connector_id_authorization_url_body_redirect_uri import (
        PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBodyRedirectUri,
    )


T = TypeVar("T", bound="PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBody")


@_attrs_define
class PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBody:
    """
    Attributes:
        state (str):
        redirect_uri (PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBodyRedirectUri): Validator function
    """

    state: str
    redirect_uri: "PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBodyRedirectUri"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state

        redirect_uri = self.redirect_uri.to_dict()

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
        from ..models.post_api_interaction_single_sign_on_connector_id_authorization_url_body_redirect_uri import (
            PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBodyRedirectUri,
        )

        d = src_dict.copy()
        state = d.pop("state")

        redirect_uri = PostApiInteractionSingleSignOnConnectorIdAuthorizationUrlBodyRedirectUri.from_dict(
            d.pop("redirectUri")
        )

        post_api_interaction_single_sign_on_connector_id_authorization_url_body = cls(
            state=state,
            redirect_uri=redirect_uri,
        )

        post_api_interaction_single_sign_on_connector_id_authorization_url_body.additional_properties = d
        return post_api_interaction_single_sign_on_connector_id_authorization_url_body

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
