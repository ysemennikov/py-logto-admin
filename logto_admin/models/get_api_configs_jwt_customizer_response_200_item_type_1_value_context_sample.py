from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample")


@_attrs_define
class GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample:
    """arbitrary"""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_api_configs_jwt_customizer_response_200_item_type_1_value_context_sample = cls()

        get_api_configs_jwt_customizer_response_200_item_type_1_value_context_sample.additional_properties = d
        return get_api_configs_jwt_customizer_response_200_item_type_1_value_context_sample

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
