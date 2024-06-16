from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiSignInExpBodyPasswordPolicyRejects")


@_attrs_define
class PatchApiSignInExpBodyPasswordPolicyRejects:
    """
    Attributes:
        pwned (bool):  Default: True.
        repetition_and_sequence (bool):  Default: True.
        user_info (bool):  Default: True.
        words (List[str]):
    """

    words: List[str]
    pwned: bool = True
    repetition_and_sequence: bool = True
    user_info: bool = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pwned = self.pwned

        repetition_and_sequence = self.repetition_and_sequence

        user_info = self.user_info

        words = self.words

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pwned": pwned,
                "repetitionAndSequence": repetition_and_sequence,
                "userInfo": user_info,
                "words": words,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pwned = d.pop("pwned")

        repetition_and_sequence = d.pop("repetitionAndSequence")

        user_info = d.pop("userInfo")

        words = cast(List[str], d.pop("words"))

        patch_api_sign_in_exp_body_password_policy_rejects = cls(
            pwned=pwned,
            repetition_and_sequence=repetition_and_sequence,
            user_info=user_info,
            words=words,
        )

        patch_api_sign_in_exp_body_password_policy_rejects.additional_properties = d
        return patch_api_sign_in_exp_body_password_policy_rejects

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
