from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_sign_in_exp_body_password_policy_character_types import (
        PatchApiSignInExpBodyPasswordPolicyCharacterTypes,
    )
    from ..models.patch_api_sign_in_exp_body_password_policy_length import PatchApiSignInExpBodyPasswordPolicyLength
    from ..models.patch_api_sign_in_exp_body_password_policy_rejects import PatchApiSignInExpBodyPasswordPolicyRejects


T = TypeVar("T", bound="PatchApiSignInExpBodyPasswordPolicy")


@_attrs_define
class PatchApiSignInExpBodyPasswordPolicy:
    """Password policies to adjust the password strength requirements.

    Attributes:
        length (Union[Unset, PatchApiSignInExpBodyPasswordPolicyLength]):
        character_types (Union[Unset, PatchApiSignInExpBodyPasswordPolicyCharacterTypes]):
        rejects (Union[Unset, PatchApiSignInExpBodyPasswordPolicyRejects]):
    """

    length: Union[Unset, "PatchApiSignInExpBodyPasswordPolicyLength"] = UNSET
    character_types: Union[Unset, "PatchApiSignInExpBodyPasswordPolicyCharacterTypes"] = UNSET
    rejects: Union[Unset, "PatchApiSignInExpBodyPasswordPolicyRejects"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        length: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.length, Unset):
            length = self.length.to_dict()

        character_types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.character_types, Unset):
            character_types = self.character_types.to_dict()

        rejects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejects, Unset):
            rejects = self.rejects.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if length is not UNSET:
            field_dict["length"] = length
        if character_types is not UNSET:
            field_dict["characterTypes"] = character_types
        if rejects is not UNSET:
            field_dict["rejects"] = rejects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_sign_in_exp_body_password_policy_character_types import (
            PatchApiSignInExpBodyPasswordPolicyCharacterTypes,
        )
        from ..models.patch_api_sign_in_exp_body_password_policy_length import PatchApiSignInExpBodyPasswordPolicyLength
        from ..models.patch_api_sign_in_exp_body_password_policy_rejects import (
            PatchApiSignInExpBodyPasswordPolicyRejects,
        )

        d = src_dict.copy()
        _length = d.pop("length", UNSET)
        length: Union[Unset, PatchApiSignInExpBodyPasswordPolicyLength]
        if isinstance(_length, Unset):
            length = UNSET
        else:
            length = PatchApiSignInExpBodyPasswordPolicyLength.from_dict(_length)

        _character_types = d.pop("characterTypes", UNSET)
        character_types: Union[Unset, PatchApiSignInExpBodyPasswordPolicyCharacterTypes]
        if isinstance(_character_types, Unset):
            character_types = UNSET
        else:
            character_types = PatchApiSignInExpBodyPasswordPolicyCharacterTypes.from_dict(_character_types)

        _rejects = d.pop("rejects", UNSET)
        rejects: Union[Unset, PatchApiSignInExpBodyPasswordPolicyRejects]
        if isinstance(_rejects, Unset):
            rejects = UNSET
        else:
            rejects = PatchApiSignInExpBodyPasswordPolicyRejects.from_dict(_rejects)

        patch_api_sign_in_exp_body_password_policy = cls(
            length=length,
            character_types=character_types,
            rejects=rejects,
        )

        patch_api_sign_in_exp_body_password_policy.additional_properties = d
        return patch_api_sign_in_exp_body_password_policy

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
