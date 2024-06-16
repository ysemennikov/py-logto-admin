from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_sign_in_exp_response_200_language_info_fallback_language import (
    PatchApiSignInExpResponse200LanguageInfoFallbackLanguage,
)

T = TypeVar("T", bound="PatchApiSignInExpResponse200LanguageInfo")


@_attrs_define
class PatchApiSignInExpResponse200LanguageInfo:
    """
    Attributes:
        auto_detect (bool):
        fallback_language (PatchApiSignInExpResponse200LanguageInfoFallbackLanguage):
    """

    auto_detect: bool
    fallback_language: PatchApiSignInExpResponse200LanguageInfoFallbackLanguage
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_detect = self.auto_detect

        fallback_language = self.fallback_language.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoDetect": auto_detect,
                "fallbackLanguage": fallback_language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_detect = d.pop("autoDetect")

        fallback_language = PatchApiSignInExpResponse200LanguageInfoFallbackLanguage(d.pop("fallbackLanguage"))

        patch_api_sign_in_exp_response_200_language_info = cls(
            auto_detect=auto_detect,
            fallback_language=fallback_language,
        )

        patch_api_sign_in_exp_response_200_language_info.additional_properties = d
        return patch_api_sign_in_exp_response_200_language_info

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
