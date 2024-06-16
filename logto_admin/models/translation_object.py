from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslationObject")


@_attrs_define
class TranslationObject:
    """
    Example:
        {'input': {'username': 'Username', 'password': 'Password'}, 'action': {'sign_in': 'Sign In', 'continue':
            'Continue'}}

    Attributes:
        translation_key (Union[Unset, str]):
    """

    translation_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        translation_key: Union[Unset, str]
        if isinstance(self.translation_key, Unset):
            translation_key = UNSET
        else:
            translation_key = self.translation_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation_key is not UNSET:
            field_dict["[translationKey]"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_translation_key(data: object) -> Union[Unset, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, str], data)

        translation_key = _parse_translation_key(d.pop("[translationKey]", UNSET))

        translation_object = cls(
            translation_key=translation_key,
        )

        translation_object.additional_properties = d
        return translation_object

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
