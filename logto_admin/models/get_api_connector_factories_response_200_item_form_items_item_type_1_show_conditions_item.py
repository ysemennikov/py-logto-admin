from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiConnectorFactoriesResponse200ItemFormItemsItemType1ShowConditionsItem")


@_attrs_define
class GetApiConnectorFactoriesResponse200ItemFormItemsItemType1ShowConditionsItem:
    """
    Attributes:
        target_key (str):
        expect_value (Union[Unset, Any]):
    """

    target_key: str
    expect_value: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_key = self.target_key

        expect_value = self.expect_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetKey": target_key,
            }
        )
        if expect_value is not UNSET:
            field_dict["expectValue"] = expect_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_key = d.pop("targetKey")

        expect_value = d.pop("expectValue", UNSET)

        get_api_connector_factories_response_200_item_form_items_item_type_1_show_conditions_item = cls(
            target_key=target_key,
            expect_value=expect_value,
        )

        get_api_connector_factories_response_200_item_form_items_item_type_1_show_conditions_item.additional_properties = d
        return get_api_connector_factories_response_200_item_form_items_item_type_1_show_conditions_item

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
