from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_sign_in_exp_response_200_sign_in_methods_item import (
        PatchApiSignInExpResponse200SignInMethodsItem,
    )


T = TypeVar("T", bound="PatchApiSignInExpResponse200SignIn")


@_attrs_define
class PatchApiSignInExpResponse200SignIn:
    """
    Attributes:
        methods (List['PatchApiSignInExpResponse200SignInMethodsItem']):
    """

    methods: List["PatchApiSignInExpResponse200SignInMethodsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        methods = []
        for methods_item_data in self.methods:
            methods_item = methods_item_data.to_dict()
            methods.append(methods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "methods": methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_sign_in_exp_response_200_sign_in_methods_item import (
            PatchApiSignInExpResponse200SignInMethodsItem,
        )

        d = src_dict.copy()
        methods = []
        _methods = d.pop("methods")
        for methods_item_data in _methods:
            methods_item = PatchApiSignInExpResponse200SignInMethodsItem.from_dict(methods_item_data)

            methods.append(methods_item)

        patch_api_sign_in_exp_response_200_sign_in = cls(
            methods=methods,
        )

        patch_api_sign_in_exp_response_200_sign_in.additional_properties = d
        return patch_api_sign_in_exp_response_200_sign_in

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
