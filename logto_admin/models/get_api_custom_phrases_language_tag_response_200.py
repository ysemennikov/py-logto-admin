from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.translation_object import TranslationObject


T = TypeVar("T", bound="GetApiCustomPhrasesLanguageTagResponse200")


@_attrs_define
class GetApiCustomPhrasesLanguageTagResponse200:
    """
    Attributes:
        id (str):
        language_tag (str):
        translation (TranslationObject):  Example: {'input': {'username': 'Username', 'password': 'Password'}, 'action':
            {'sign_in': 'Sign In', 'continue': 'Continue'}}.
    """

    id: str
    language_tag: str
    translation: "TranslationObject"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        language_tag = self.language_tag

        translation = self.translation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "languageTag": language_tag,
                "translation": translation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.translation_object import TranslationObject

        d = src_dict.copy()
        id = d.pop("id")

        language_tag = d.pop("languageTag")

        translation = TranslationObject.from_dict(d.pop("translation"))

        get_api_custom_phrases_language_tag_response_200 = cls(
            id=id,
            language_tag=language_tag,
            translation=translation,
        )

        get_api_custom_phrases_language_tag_response_200.additional_properties = d
        return get_api_custom_phrases_language_tag_response_200

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
