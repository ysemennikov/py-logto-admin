from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value import (
        GetApiConfigsJwtCustomizerResponse200ItemType1Value,
    )


T = TypeVar("T", bound="GetApiConfigsJwtCustomizerResponse200ItemType1")


@_attrs_define
class GetApiConfigsJwtCustomizerResponse200ItemType1:
    """
    Attributes:
        key (str):
        value (GetApiConfigsJwtCustomizerResponse200ItemType1Value):
    """

    key: str
    value: "GetApiConfigsJwtCustomizerResponse200ItemType1Value"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value import (
            GetApiConfigsJwtCustomizerResponse200ItemType1Value,
        )

        d = src_dict.copy()
        key = d.pop("key")

        value = GetApiConfigsJwtCustomizerResponse200ItemType1Value.from_dict(d.pop("value"))

        get_api_configs_jwt_customizer_response_200_item_type_1 = cls(
            key=key,
            value=value,
        )

        get_api_configs_jwt_customizer_response_200_item_type_1.additional_properties = d
        return get_api_configs_jwt_customizer_response_200_item_type_1

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
