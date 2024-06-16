from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_interaction_verification_webauthn_authentication_response_200_user_verification import (
    PostApiInteractionVerificationWebauthnAuthenticationResponse200UserVerification,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_interaction_verification_webauthn_authentication_response_200_allow_credentials_item import (
        PostApiInteractionVerificationWebauthnAuthenticationResponse200AllowCredentialsItem,
    )
    from ..models.post_api_interaction_verification_webauthn_authentication_response_200_extensions import (
        PostApiInteractionVerificationWebauthnAuthenticationResponse200Extensions,
    )


T = TypeVar("T", bound="PostApiInteractionVerificationWebauthnAuthenticationResponse200")


@_attrs_define
class PostApiInteractionVerificationWebauthnAuthenticationResponse200:
    """
    Attributes:
        challenge (str):
        timeout (Union[Unset, float]):
        rp_id (Union[Unset, str]):
        allow_credentials (Union[Unset,
            List['PostApiInteractionVerificationWebauthnAuthenticationResponse200AllowCredentialsItem']]):
        user_verification (Union[Unset,
            PostApiInteractionVerificationWebauthnAuthenticationResponse200UserVerification]):
        extensions (Union[Unset, PostApiInteractionVerificationWebauthnAuthenticationResponse200Extensions]):
    """

    challenge: str
    timeout: Union[Unset, float] = UNSET
    rp_id: Union[Unset, str] = UNSET
    allow_credentials: Union[
        Unset, List["PostApiInteractionVerificationWebauthnAuthenticationResponse200AllowCredentialsItem"]
    ] = UNSET
    user_verification: Union[Unset, PostApiInteractionVerificationWebauthnAuthenticationResponse200UserVerification] = (
        UNSET
    )
    extensions: Union[Unset, "PostApiInteractionVerificationWebauthnAuthenticationResponse200Extensions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge = self.challenge

        timeout = self.timeout

        rp_id = self.rp_id

        allow_credentials: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allow_credentials, Unset):
            allow_credentials = []
            for allow_credentials_item_data in self.allow_credentials:
                allow_credentials_item = allow_credentials_item_data.to_dict()
                allow_credentials.append(allow_credentials_item)

        user_verification: Union[Unset, str] = UNSET
        if not isinstance(self.user_verification, Unset):
            user_verification = self.user_verification.value

        extensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge": challenge,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if rp_id is not UNSET:
            field_dict["rpId"] = rp_id
        if allow_credentials is not UNSET:
            field_dict["allowCredentials"] = allow_credentials
        if user_verification is not UNSET:
            field_dict["userVerification"] = user_verification
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_interaction_verification_webauthn_authentication_response_200_allow_credentials_item import (
            PostApiInteractionVerificationWebauthnAuthenticationResponse200AllowCredentialsItem,
        )
        from ..models.post_api_interaction_verification_webauthn_authentication_response_200_extensions import (
            PostApiInteractionVerificationWebauthnAuthenticationResponse200Extensions,
        )

        d = src_dict.copy()
        challenge = d.pop("challenge")

        timeout = d.pop("timeout", UNSET)

        rp_id = d.pop("rpId", UNSET)

        allow_credentials = []
        _allow_credentials = d.pop("allowCredentials", UNSET)
        for allow_credentials_item_data in _allow_credentials or []:
            allow_credentials_item = (
                PostApiInteractionVerificationWebauthnAuthenticationResponse200AllowCredentialsItem.from_dict(
                    allow_credentials_item_data
                )
            )

            allow_credentials.append(allow_credentials_item)

        _user_verification = d.pop("userVerification", UNSET)
        user_verification: Union[Unset, PostApiInteractionVerificationWebauthnAuthenticationResponse200UserVerification]
        if isinstance(_user_verification, Unset):
            user_verification = UNSET
        else:
            user_verification = PostApiInteractionVerificationWebauthnAuthenticationResponse200UserVerification(
                _user_verification
            )

        _extensions = d.pop("extensions", UNSET)
        extensions: Union[Unset, PostApiInteractionVerificationWebauthnAuthenticationResponse200Extensions]
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = PostApiInteractionVerificationWebauthnAuthenticationResponse200Extensions.from_dict(
                _extensions
            )

        post_api_interaction_verification_webauthn_authentication_response_200 = cls(
            challenge=challenge,
            timeout=timeout,
            rp_id=rp_id,
            allow_credentials=allow_credentials,
            user_verification=user_verification,
            extensions=extensions,
        )

        post_api_interaction_verification_webauthn_authentication_response_200.additional_properties = d
        return post_api_interaction_verification_webauthn_authentication_response_200

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
