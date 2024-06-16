from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_sign_in_exp_response_200_password_policy_character_types import (
        PatchApiSignInExpResponse200PasswordPolicyCharacterTypes,
    )
    from ..models.patch_api_sign_in_exp_response_200_password_policy_length import (
        PatchApiSignInExpResponse200PasswordPolicyLength,
    )
    from ..models.patch_api_sign_in_exp_response_200_password_policy_rejects import (
        PatchApiSignInExpResponse200PasswordPolicyRejects,
    )


T = TypeVar("T", bound="PatchApiSignInExpResponse200PasswordPolicy")


@_attrs_define
class PatchApiSignInExpResponse200PasswordPolicy:
    """
    Attributes:
        length (Union[Unset, PatchApiSignInExpResponse200PasswordPolicyLength]):
        character_types (Union[Unset, PatchApiSignInExpResponse200PasswordPolicyCharacterTypes]):
        rejects (Union[Unset, PatchApiSignInExpResponse200PasswordPolicyRejects]):
    """

    length: Union[Unset, "PatchApiSignInExpResponse200PasswordPolicyLength"] = UNSET
    character_types: Union[Unset, "PatchApiSignInExpResponse200PasswordPolicyCharacterTypes"] = UNSET
    rejects: Union[Unset, "PatchApiSignInExpResponse200PasswordPolicyRejects"] = UNSET
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
        from ..models.patch_api_sign_in_exp_response_200_password_policy_character_types import (
            PatchApiSignInExpResponse200PasswordPolicyCharacterTypes,
        )
        from ..models.patch_api_sign_in_exp_response_200_password_policy_length import (
            PatchApiSignInExpResponse200PasswordPolicyLength,
        )
        from ..models.patch_api_sign_in_exp_response_200_password_policy_rejects import (
            PatchApiSignInExpResponse200PasswordPolicyRejects,
        )

        d = src_dict.copy()
        _length = d.pop("length", UNSET)
        length: Union[Unset, PatchApiSignInExpResponse200PasswordPolicyLength]
        if isinstance(_length, Unset):
            length = UNSET
        else:
            length = PatchApiSignInExpResponse200PasswordPolicyLength.from_dict(_length)

        _character_types = d.pop("characterTypes", UNSET)
        character_types: Union[Unset, PatchApiSignInExpResponse200PasswordPolicyCharacterTypes]
        if isinstance(_character_types, Unset):
            character_types = UNSET
        else:
            character_types = PatchApiSignInExpResponse200PasswordPolicyCharacterTypes.from_dict(_character_types)

        _rejects = d.pop("rejects", UNSET)
        rejects: Union[Unset, PatchApiSignInExpResponse200PasswordPolicyRejects]
        if isinstance(_rejects, Unset):
            rejects = UNSET
        else:
            rejects = PatchApiSignInExpResponse200PasswordPolicyRejects.from_dict(_rejects)

        patch_api_sign_in_exp_response_200_password_policy = cls(
            length=length,
            character_types=character_types,
            rejects=rejects,
        )

        patch_api_sign_in_exp_response_200_password_policy.additional_properties = d
        return patch_api_sign_in_exp_response_200_password_policy

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
