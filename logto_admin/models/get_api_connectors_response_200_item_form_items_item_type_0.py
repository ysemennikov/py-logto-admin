from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_connectors_response_200_item_form_items_item_type_0_select_items_item import (
        GetApiConnectorsResponse200ItemFormItemsItemType0SelectItemsItem,
    )
    from ..models.get_api_connectors_response_200_item_form_items_item_type_0_show_conditions_item import (
        GetApiConnectorsResponse200ItemFormItemsItemType0ShowConditionsItem,
    )


T = TypeVar("T", bound="GetApiConnectorsResponse200ItemFormItemsItemType0")


@_attrs_define
class GetApiConnectorsResponse200ItemFormItemsItemType0:
    """
    Attributes:
        type (str):
        select_items (List['GetApiConnectorsResponse200ItemFormItemsItemType0SelectItemsItem']):
        key (str):
        label (str):
        placeholder (Union[Unset, str]):
        required (Union[Unset, bool]):
        default_value (Union[Unset, Any]):
        show_conditions (Union[Unset, List['GetApiConnectorsResponse200ItemFormItemsItemType0ShowConditionsItem']]):
        description (Union[Unset, str]):
        tooltip (Union[Unset, str]):
        is_confidential (Union[Unset, bool]):
    """

    type: str
    select_items: List["GetApiConnectorsResponse200ItemFormItemsItemType0SelectItemsItem"]
    key: str
    label: str
    placeholder: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    default_value: Union[Unset, Any] = UNSET
    show_conditions: Union[Unset, List["GetApiConnectorsResponse200ItemFormItemsItemType0ShowConditionsItem"]] = UNSET
    description: Union[Unset, str] = UNSET
    tooltip: Union[Unset, str] = UNSET
    is_confidential: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        select_items = []
        for select_items_item_data in self.select_items:
            select_items_item = select_items_item_data.to_dict()
            select_items.append(select_items_item)

        key = self.key

        label = self.label

        placeholder = self.placeholder

        required = self.required

        default_value = self.default_value

        show_conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.show_conditions, Unset):
            show_conditions = []
            for show_conditions_item_data in self.show_conditions:
                show_conditions_item = show_conditions_item_data.to_dict()
                show_conditions.append(show_conditions_item)

        description = self.description

        tooltip = self.tooltip

        is_confidential = self.is_confidential

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "selectItems": select_items,
                "key": key,
                "label": label,
            }
        )
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if required is not UNSET:
            field_dict["required"] = required
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if show_conditions is not UNSET:
            field_dict["showConditions"] = show_conditions
        if description is not UNSET:
            field_dict["description"] = description
        if tooltip is not UNSET:
            field_dict["tooltip"] = tooltip
        if is_confidential is not UNSET:
            field_dict["isConfidential"] = is_confidential

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_connectors_response_200_item_form_items_item_type_0_select_items_item import (
            GetApiConnectorsResponse200ItemFormItemsItemType0SelectItemsItem,
        )
        from ..models.get_api_connectors_response_200_item_form_items_item_type_0_show_conditions_item import (
            GetApiConnectorsResponse200ItemFormItemsItemType0ShowConditionsItem,
        )

        d = src_dict.copy()
        type = d.pop("type")

        select_items = []
        _select_items = d.pop("selectItems")
        for select_items_item_data in _select_items:
            select_items_item = GetApiConnectorsResponse200ItemFormItemsItemType0SelectItemsItem.from_dict(
                select_items_item_data
            )

            select_items.append(select_items_item)

        key = d.pop("key")

        label = d.pop("label")

        placeholder = d.pop("placeholder", UNSET)

        required = d.pop("required", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        show_conditions = []
        _show_conditions = d.pop("showConditions", UNSET)
        for show_conditions_item_data in _show_conditions or []:
            show_conditions_item = GetApiConnectorsResponse200ItemFormItemsItemType0ShowConditionsItem.from_dict(
                show_conditions_item_data
            )

            show_conditions.append(show_conditions_item)

        description = d.pop("description", UNSET)

        tooltip = d.pop("tooltip", UNSET)

        is_confidential = d.pop("isConfidential", UNSET)

        get_api_connectors_response_200_item_form_items_item_type_0 = cls(
            type=type,
            select_items=select_items,
            key=key,
            label=label,
            placeholder=placeholder,
            required=required,
            default_value=default_value,
            show_conditions=show_conditions,
            description=description,
            tooltip=tooltip,
            is_confidential=is_confidential,
        )

        get_api_connectors_response_200_item_form_items_item_type_0.additional_properties = d
        return get_api_connectors_response_200_item_form_items_item_type_0

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
