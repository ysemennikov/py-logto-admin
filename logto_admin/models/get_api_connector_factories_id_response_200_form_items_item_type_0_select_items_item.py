from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiConnectorFactoriesIdResponse200FormItemsItemType0SelectItemsItem")


@_attrs_define
class GetApiConnectorFactoriesIdResponse200FormItemsItemType0SelectItemsItem:
    """
    Attributes:
        value (str):
        title (str):
    """

    value: str
    title: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        title = d.pop("title")

        get_api_connector_factories_id_response_200_form_items_item_type_0_select_items_item = cls(
            value=value,
            title=title,
        )

        get_api_connector_factories_id_response_200_form_items_item_type_0_select_items_item.additional_properties = d
        return get_api_connector_factories_id_response_200_form_items_item_type_0_select_items_item

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
