from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_interaction_verification_webauthn_registration_response_200_attestation import (
    PostApiInteractionVerificationWebauthnRegistrationResponse200Attestation,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection import (
        PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection,
    )
    from ..models.post_api_interaction_verification_webauthn_registration_response_200_exclude_credentials_item import (
        PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem,
    )
    from ..models.post_api_interaction_verification_webauthn_registration_response_200_extensions import (
        PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions,
    )
    from ..models.post_api_interaction_verification_webauthn_registration_response_200_pub_key_cred_params_item import (
        PostApiInteractionVerificationWebauthnRegistrationResponse200PubKeyCredParamsItem,
    )
    from ..models.post_api_interaction_verification_webauthn_registration_response_200_rp import (
        PostApiInteractionVerificationWebauthnRegistrationResponse200Rp,
    )
    from ..models.post_api_interaction_verification_webauthn_registration_response_200_user import (
        PostApiInteractionVerificationWebauthnRegistrationResponse200User,
    )


T = TypeVar("T", bound="PostApiInteractionVerificationWebauthnRegistrationResponse200")


@_attrs_define
class PostApiInteractionVerificationWebauthnRegistrationResponse200:
    """
    Attributes:
        rp (PostApiInteractionVerificationWebauthnRegistrationResponse200Rp):
        user (PostApiInteractionVerificationWebauthnRegistrationResponse200User):
        challenge (str):
        pub_key_cred_params (List['PostApiInteractionVerificationWebauthnRegistrationResponse200PubKeyCredParamsItem']):
        timeout (Union[Unset, float]):
        exclude_credentials (Union[Unset,
            List['PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem']]):
        authenticator_selection (Union[Unset,
            PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection]):
        attestation (Union[Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200Attestation]):
        extensions (Union[Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions]):
    """

    rp: "PostApiInteractionVerificationWebauthnRegistrationResponse200Rp"
    user: "PostApiInteractionVerificationWebauthnRegistrationResponse200User"
    challenge: str
    pub_key_cred_params: List["PostApiInteractionVerificationWebauthnRegistrationResponse200PubKeyCredParamsItem"]
    timeout: Union[Unset, float] = UNSET
    exclude_credentials: Union[
        Unset, List["PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem"]
    ] = UNSET
    authenticator_selection: Union[
        Unset, "PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection"
    ] = UNSET
    attestation: Union[Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200Attestation] = UNSET
    extensions: Union[Unset, "PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rp = self.rp.to_dict()

        user = self.user.to_dict()

        challenge = self.challenge

        pub_key_cred_params = []
        for pub_key_cred_params_item_data in self.pub_key_cred_params:
            pub_key_cred_params_item = pub_key_cred_params_item_data.to_dict()
            pub_key_cred_params.append(pub_key_cred_params_item)

        timeout = self.timeout

        exclude_credentials: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exclude_credentials, Unset):
            exclude_credentials = []
            for exclude_credentials_item_data in self.exclude_credentials:
                exclude_credentials_item = exclude_credentials_item_data.to_dict()
                exclude_credentials.append(exclude_credentials_item)

        authenticator_selection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authenticator_selection, Unset):
            authenticator_selection = self.authenticator_selection.to_dict()

        attestation: Union[Unset, str] = UNSET
        if not isinstance(self.attestation, Unset):
            attestation = self.attestation.value

        extensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rp": rp,
                "user": user,
                "challenge": challenge,
                "pubKeyCredParams": pub_key_cred_params,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if exclude_credentials is not UNSET:
            field_dict["excludeCredentials"] = exclude_credentials
        if authenticator_selection is not UNSET:
            field_dict["authenticatorSelection"] = authenticator_selection
        if attestation is not UNSET:
            field_dict["attestation"] = attestation
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_interaction_verification_webauthn_registration_response_200_authenticator_selection import (
            PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection,
        )
        from ..models.post_api_interaction_verification_webauthn_registration_response_200_exclude_credentials_item import (
            PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem,
        )
        from ..models.post_api_interaction_verification_webauthn_registration_response_200_extensions import (
            PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions,
        )
        from ..models.post_api_interaction_verification_webauthn_registration_response_200_pub_key_cred_params_item import (
            PostApiInteractionVerificationWebauthnRegistrationResponse200PubKeyCredParamsItem,
        )
        from ..models.post_api_interaction_verification_webauthn_registration_response_200_rp import (
            PostApiInteractionVerificationWebauthnRegistrationResponse200Rp,
        )
        from ..models.post_api_interaction_verification_webauthn_registration_response_200_user import (
            PostApiInteractionVerificationWebauthnRegistrationResponse200User,
        )

        d = src_dict.copy()
        rp = PostApiInteractionVerificationWebauthnRegistrationResponse200Rp.from_dict(d.pop("rp"))

        user = PostApiInteractionVerificationWebauthnRegistrationResponse200User.from_dict(d.pop("user"))

        challenge = d.pop("challenge")

        pub_key_cred_params = []
        _pub_key_cred_params = d.pop("pubKeyCredParams")
        for pub_key_cred_params_item_data in _pub_key_cred_params:
            pub_key_cred_params_item = (
                PostApiInteractionVerificationWebauthnRegistrationResponse200PubKeyCredParamsItem.from_dict(
                    pub_key_cred_params_item_data
                )
            )

            pub_key_cred_params.append(pub_key_cred_params_item)

        timeout = d.pop("timeout", UNSET)

        exclude_credentials = []
        _exclude_credentials = d.pop("excludeCredentials", UNSET)
        for exclude_credentials_item_data in _exclude_credentials or []:
            exclude_credentials_item = (
                PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem.from_dict(
                    exclude_credentials_item_data
                )
            )

            exclude_credentials.append(exclude_credentials_item)

        _authenticator_selection = d.pop("authenticatorSelection", UNSET)
        authenticator_selection: Union[
            Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection
        ]
        if isinstance(_authenticator_selection, Unset):
            authenticator_selection = UNSET
        else:
            authenticator_selection = (
                PostApiInteractionVerificationWebauthnRegistrationResponse200AuthenticatorSelection.from_dict(
                    _authenticator_selection
                )
            )

        _attestation = d.pop("attestation", UNSET)
        attestation: Union[Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200Attestation]
        if isinstance(_attestation, Unset):
            attestation = UNSET
        else:
            attestation = PostApiInteractionVerificationWebauthnRegistrationResponse200Attestation(_attestation)

        _extensions = d.pop("extensions", UNSET)
        extensions: Union[Unset, PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions]
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions.from_dict(_extensions)

        post_api_interaction_verification_webauthn_registration_response_200 = cls(
            rp=rp,
            user=user,
            challenge=challenge,
            pub_key_cred_params=pub_key_cred_params,
            timeout=timeout,
            exclude_credentials=exclude_credentials,
            authenticator_selection=authenticator_selection,
            attestation=attestation,
            extensions=extensions,
        )

        post_api_interaction_verification_webauthn_registration_response_200.additional_properties = d
        return post_api_interaction_verification_webauthn_registration_response_200

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
