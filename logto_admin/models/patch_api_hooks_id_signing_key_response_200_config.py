from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_hooks_id_signing_key_response_200_config_headers import (
        PatchApiHooksIdSigningKeyResponse200ConfigHeaders,
    )


T = TypeVar("T", bound="PatchApiHooksIdSigningKeyResponse200Config")


@_attrs_define
class PatchApiHooksIdSigningKeyResponse200Config:
    """
    Attributes:
        url (str):
        headers (Union[Unset, PatchApiHooksIdSigningKeyResponse200ConfigHeaders]):
        retries (Union[Unset, float]):
    """

    url: str
    headers: Union[Unset, "PatchApiHooksIdSigningKeyResponse200ConfigHeaders"] = UNSET
    retries: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        retries = self.retries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if retries is not UNSET:
            field_dict["retries"] = retries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_hooks_id_signing_key_response_200_config_headers import (
            PatchApiHooksIdSigningKeyResponse200ConfigHeaders,
        )

        d = src_dict.copy()
        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, PatchApiHooksIdSigningKeyResponse200ConfigHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = PatchApiHooksIdSigningKeyResponse200ConfigHeaders.from_dict(_headers)

        retries = d.pop("retries", UNSET)

        patch_api_hooks_id_signing_key_response_200_config = cls(
            url=url,
            headers=headers,
            retries=retries,
        )

        patch_api_hooks_id_signing_key_response_200_config.additional_properties = d
        return patch_api_hooks_id_signing_key_response_200_config

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
