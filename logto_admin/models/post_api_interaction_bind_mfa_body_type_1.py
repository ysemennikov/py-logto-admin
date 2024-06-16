from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_interaction_bind_mfa_body_type_1_authenticator_attachment import (
    PostApiInteractionBindMfaBodyType1AuthenticatorAttachment,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_interaction_bind_mfa_body_type_1_client_extension_results import (
        PostApiInteractionBindMfaBodyType1ClientExtensionResults,
    )
    from ..models.post_api_interaction_bind_mfa_body_type_1_response import PostApiInteractionBindMfaBodyType1Response


T = TypeVar("T", bound="PostApiInteractionBindMfaBodyType1")


@_attrs_define
class PostApiInteractionBindMfaBodyType1:
    """
    Attributes:
        type (str):
        id (str):
        raw_id (str):
        response (PostApiInteractionBindMfaBodyType1Response):
        client_extension_results (PostApiInteractionBindMfaBodyType1ClientExtensionResults):
        authenticator_attachment (Union[Unset, PostApiInteractionBindMfaBodyType1AuthenticatorAttachment]):
    """

    type: str
    id: str
    raw_id: str
    response: "PostApiInteractionBindMfaBodyType1Response"
    client_extension_results: "PostApiInteractionBindMfaBodyType1ClientExtensionResults"
    authenticator_attachment: Union[Unset, PostApiInteractionBindMfaBodyType1AuthenticatorAttachment] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id = self.id

        raw_id = self.raw_id

        response = self.response.to_dict()

        client_extension_results = self.client_extension_results.to_dict()

        authenticator_attachment: Union[Unset, str] = UNSET
        if not isinstance(self.authenticator_attachment, Unset):
            authenticator_attachment = self.authenticator_attachment.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "rawId": raw_id,
                "response": response,
                "clientExtensionResults": client_extension_results,
            }
        )
        if authenticator_attachment is not UNSET:
            field_dict["authenticatorAttachment"] = authenticator_attachment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_interaction_bind_mfa_body_type_1_client_extension_results import (
            PostApiInteractionBindMfaBodyType1ClientExtensionResults,
        )
        from ..models.post_api_interaction_bind_mfa_body_type_1_response import (
            PostApiInteractionBindMfaBodyType1Response,
        )

        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id")

        raw_id = d.pop("rawId")

        response = PostApiInteractionBindMfaBodyType1Response.from_dict(d.pop("response"))

        client_extension_results = PostApiInteractionBindMfaBodyType1ClientExtensionResults.from_dict(
            d.pop("clientExtensionResults")
        )

        _authenticator_attachment = d.pop("authenticatorAttachment", UNSET)
        authenticator_attachment: Union[Unset, PostApiInteractionBindMfaBodyType1AuthenticatorAttachment]
        if isinstance(_authenticator_attachment, Unset):
            authenticator_attachment = UNSET
        else:
            authenticator_attachment = PostApiInteractionBindMfaBodyType1AuthenticatorAttachment(
                _authenticator_attachment
            )

        post_api_interaction_bind_mfa_body_type_1 = cls(
            type=type,
            id=id,
            raw_id=raw_id,
            response=response,
            client_extension_results=client_extension_results,
            authenticator_attachment=authenticator_attachment,
        )

        post_api_interaction_bind_mfa_body_type_1.additional_properties = d
        return post_api_interaction_bind_mfa_body_type_1

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
