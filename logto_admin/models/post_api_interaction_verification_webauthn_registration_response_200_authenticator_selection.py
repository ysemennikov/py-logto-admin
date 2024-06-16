from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection_authenticator_attachment import (
    PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionAuthenticatorAttachment,
)
from ..models.post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection_resident_key import (
    PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionResidentKey,
)
from ..models.post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection_user_verification import (
    PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionUserVerification,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection")


@_attrs_define
class PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection:
    """
    Attributes:
        authenticator_attachment (Union[Unset,
            PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionAuthenticatorAttachment]):
        require_resident_key (Union[Unset, bool]):
        resident_key (Union[Unset,
            PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionResidentKey]):
        user_verification (Union[Unset,
            PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionUserVerification]):
    """

    authenticator_attachment: Union[
        Unset,
        PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionAuthenticatorAttachment,
    ] = UNSET
    require_resident_key: Union[Unset, bool] = UNSET
    resident_key: Union[
        Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionResidentKey
    ] = UNSET
    user_verification: Union[
        Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionUserVerification
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authenticator_attachment: Union[Unset, str] = UNSET
        if not isinstance(self.authenticator_attachment, Unset):
            authenticator_attachment = self.authenticator_attachment.value

        require_resident_key = self.require_resident_key

        resident_key: Union[Unset, str] = UNSET
        if not isinstance(self.resident_key, Unset):
            resident_key = self.resident_key.value

        user_verification: Union[Unset, str] = UNSET
        if not isinstance(self.user_verification, Unset):
            user_verification = self.user_verification.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticator_attachment is not UNSET:
            field_dict["authenticatorAttachment"] = authenticator_attachment
        if require_resident_key is not UNSET:
            field_dict["requireResidentKey"] = require_resident_key
        if resident_key is not UNSET:
            field_dict["residentKey"] = resident_key
        if user_verification is not UNSET:
            field_dict["userVerification"] = user_verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _authenticator_attachment = d.pop("authenticatorAttachment", UNSET)
        authenticator_attachment: Union[
            Unset,
            PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionAuthenticatorAttachment,
        ]
        if isinstance(_authenticator_attachment, Unset):
            authenticator_attachment = UNSET
        else:
            authenticator_attachment = PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionAuthenticatorAttachment(
                _authenticator_attachment
            )

        require_resident_key = d.pop("requireResidentKey", UNSET)

        _resident_key = d.pop("residentKey", UNSET)
        resident_key: Union[
            Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionResidentKey
        ]
        if isinstance(_resident_key, Unset):
            resident_key = UNSET
        else:
            resident_key = (
                PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionResidentKey(
                    _resident_key
                )
            )

        _user_verification = d.pop("userVerification", UNSET)
        user_verification: Union[
            Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionUserVerification
        ]
        if isinstance(_user_verification, Unset):
            user_verification = UNSET
        else:
            user_verification = (
                PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelectionUserVerification(
                    _user_verification
                )
            )

        post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection = cls(
            authenticator_attachment=authenticator_attachment,
            require_resident_key=require_resident_key,
            resident_key=resident_key,
            user_verification=user_verification,
        )

        post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection.additional_properties = d
        return post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection

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
