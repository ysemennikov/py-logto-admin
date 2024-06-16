from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions")


@_attrs_define
class PostApiInteractionVerificationWebauthnRegistrationResponse200Extensions:
    """
    Attributes:
        appid (Union[Unset, str]):
        cred_props (Union[Unset, bool]):
        hmac_create_secret (Union[Unset, bool]):
    """

    appid: Union[Unset, str] = UNSET
    cred_props: Union[Unset, bool] = UNSET
    hmac_create_secret: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appid = self.appid

        cred_props = self.cred_props

        hmac_create_secret = self.hmac_create_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appid is not UNSET:
            field_dict["appid"] = appid
        if cred_props is not UNSET:
            field_dict["credProps"] = cred_props
        if hmac_create_secret is not UNSET:
            field_dict["hmacCreateSecret"] = hmac_create_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        appid = d.pop("appid", UNSET)

        cred_props = d.pop("credProps", UNSET)

        hmac_create_secret = d.pop("hmacCreateSecret", UNSET)

        post_api_interaction_verification_webauthn_registration_response_200_extensions = cls(
            appid=appid,
            cred_props=cred_props,
            hmac_create_secret=hmac_create_secret,
        )

        post_api_interaction_verification_webauthn_registration_response_200_extensions.additional_properties = d
        return post_api_interaction_verification_webauthn_registration_response_200_extensions

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
