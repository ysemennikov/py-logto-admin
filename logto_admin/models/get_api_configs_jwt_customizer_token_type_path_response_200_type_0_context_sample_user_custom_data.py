from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserCustomData")


@_attrs_define
class GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserCustomData:
    """arbitrary"""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_custom_data = cls()

        get_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_custom_data.additional_properties = d
        return get_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_custom_data

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
