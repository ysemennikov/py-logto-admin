from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps")


@_attrs_define
class PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps:
    """
    Attributes:
        rk (Union[Unset, bool]):
    """

    rk: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rk = self.rk

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rk is not UNSET:
            field_dict["rk"] = rk

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rk = d.pop("rk", UNSET)

        put_api_interaction_mfa_body_type_1_client_extension_results_crep_props = cls(
            rk=rk,
        )

        put_api_interaction_mfa_body_type_1_client_extension_results_crep_props.additional_properties = d
        return put_api_interaction_mfa_body_type_1_client_extension_results_crep_props

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
