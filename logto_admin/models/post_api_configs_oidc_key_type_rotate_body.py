from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_configs_oidc_key_type_rotate_body_signing_key_algorithm import (
    PostApiConfigsOidcKeyTypeRotateBodySigningKeyAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiConfigsOidcKeyTypeRotateBody")


@_attrs_define
class PostApiConfigsOidcKeyTypeRotateBody:
    """
    Attributes:
        signing_key_algorithm (Union[Unset, PostApiConfigsOidcKeyTypeRotateBodySigningKeyAlgorithm]): The signing key
            algorithm the new generated private key is using.

            Only applicable when `keyType` is `private-keys`.
    """

    signing_key_algorithm: Union[Unset, PostApiConfigsOidcKeyTypeRotateBodySigningKeyAlgorithm] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signing_key_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.signing_key_algorithm, Unset):
            signing_key_algorithm = self.signing_key_algorithm.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signing_key_algorithm is not UNSET:
            field_dict["signingKeyAlgorithm"] = signing_key_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _signing_key_algorithm = d.pop("signingKeyAlgorithm", UNSET)
        signing_key_algorithm: Union[Unset, PostApiConfigsOidcKeyTypeRotateBodySigningKeyAlgorithm]
        if isinstance(_signing_key_algorithm, Unset):
            signing_key_algorithm = UNSET
        else:
            signing_key_algorithm = PostApiConfigsOidcKeyTypeRotateBodySigningKeyAlgorithm(_signing_key_algorithm)

        post_api_configs_oidc_key_type_rotate_body = cls(
            signing_key_algorithm=signing_key_algorithm,
        )

        post_api_configs_oidc_key_type_rotate_body.additional_properties = d
        return post_api_configs_oidc_key_type_rotate_body

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
