from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_connector_factories_response_200_item_platform import (
    GetApiConnectorFactoriesResponse200ItemPlatform,
)
from ..models.get_api_connector_factories_response_200_item_type import GetApiConnectorFactoriesResponse200ItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_connector_factories_response_200_item_description import (
        GetApiConnectorFactoriesResponse200ItemDescription,
    )
    from ..models.get_api_connector_factories_response_200_item_form_items_item_type_0 import (
        GetApiConnectorFactoriesResponse200ItemFormItemsItemType0,
    )
    from ..models.get_api_connector_factories_response_200_item_form_items_item_type_1 import (
        GetApiConnectorFactoriesResponse200ItemFormItemsItemType1,
    )
    from ..models.get_api_connector_factories_response_200_item_name import GetApiConnectorFactoriesResponse200ItemName


T = TypeVar("T", bound="GetApiConnectorFactoriesResponse200Item")


@_attrs_define
class GetApiConnectorFactoriesResponse200Item:
    """
    Attributes:
        type (GetApiConnectorFactoriesResponse200ItemType):
        id (str):
        target (str):
        name (GetApiConnectorFactoriesResponse200ItemName): Validator function
        description (GetApiConnectorFactoriesResponse200ItemDescription): Validator function
        logo (str):
        logo_dark (Union[None, str]):
        readme (str):
        platform (GetApiConnectorFactoriesResponse200ItemPlatform):
        is_demo (Union[Unset, bool]):
        config_template (Union[Unset, str]):
        form_items (Union[Unset, List[Union['GetApiConnectorFactoriesResponse200ItemFormItemsItemType0',
            'GetApiConnectorFactoriesResponse200ItemFormItemsItemType1']]]):
        is_standard (Union[Unset, bool]):
    """

    type: GetApiConnectorFactoriesResponse200ItemType
    id: str
    target: str
    name: "GetApiConnectorFactoriesResponse200ItemName"
    description: "GetApiConnectorFactoriesResponse200ItemDescription"
    logo: str
    logo_dark: Union[None, str]
    readme: str
    platform: GetApiConnectorFactoriesResponse200ItemPlatform
    is_demo: Union[Unset, bool] = UNSET
    config_template: Union[Unset, str] = UNSET
    form_items: Union[
        Unset,
        List[
            Union[
                "GetApiConnectorFactoriesResponse200ItemFormItemsItemType0",
                "GetApiConnectorFactoriesResponse200ItemFormItemsItemType1",
            ]
        ],
    ] = UNSET
    is_standard: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_connector_factories_response_200_item_form_items_item_type_0 import (
            GetApiConnectorFactoriesResponse200ItemFormItemsItemType0,
        )

        type = self.type.value

        id = self.id

        target = self.target

        name = self.name.to_dict()

        description = self.description.to_dict()

        logo = self.logo

        logo_dark: Union[None, str]
        logo_dark = self.logo_dark

        readme = self.readme

        platform = self.platform.value

        is_demo = self.is_demo

        config_template = self.config_template

        form_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.form_items, Unset):
            form_items = []
            for form_items_item_data in self.form_items:
                form_items_item: Dict[str, Any]
                if isinstance(form_items_item_data, GetApiConnectorFactoriesResponse200ItemFormItemsItemType0):
                    form_items_item = form_items_item_data.to_dict()
                else:
                    form_items_item = form_items_item_data.to_dict()

                form_items.append(form_items_item)

        is_standard = self.is_standard

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "target": target,
                "name": name,
                "description": description,
                "logo": logo,
                "logoDark": logo_dark,
                "readme": readme,
                "platform": platform,
            }
        )
        if is_demo is not UNSET:
            field_dict["isDemo"] = is_demo
        if config_template is not UNSET:
            field_dict["configTemplate"] = config_template
        if form_items is not UNSET:
            field_dict["formItems"] = form_items
        if is_standard is not UNSET:
            field_dict["isStandard"] = is_standard

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_connector_factories_response_200_item_description import (
            GetApiConnectorFactoriesResponse200ItemDescription,
        )
        from ..models.get_api_connector_factories_response_200_item_form_items_item_type_0 import (
            GetApiConnectorFactoriesResponse200ItemFormItemsItemType0,
        )
        from ..models.get_api_connector_factories_response_200_item_form_items_item_type_1 import (
            GetApiConnectorFactoriesResponse200ItemFormItemsItemType1,
        )
        from ..models.get_api_connector_factories_response_200_item_name import (
            GetApiConnectorFactoriesResponse200ItemName,
        )

        d = src_dict.copy()
        type = GetApiConnectorFactoriesResponse200ItemType(d.pop("type"))

        id = d.pop("id")

        target = d.pop("target")

        name = GetApiConnectorFactoriesResponse200ItemName.from_dict(d.pop("name"))

        description = GetApiConnectorFactoriesResponse200ItemDescription.from_dict(d.pop("description"))

        logo = d.pop("logo")

        def _parse_logo_dark(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        logo_dark = _parse_logo_dark(d.pop("logoDark"))

        readme = d.pop("readme")

        platform = GetApiConnectorFactoriesResponse200ItemPlatform(d.pop("platform"))

        is_demo = d.pop("isDemo", UNSET)

        config_template = d.pop("configTemplate", UNSET)

        form_items = []
        _form_items = d.pop("formItems", UNSET)
        for form_items_item_data in _form_items or []:

            def _parse_form_items_item(
                data: object,
            ) -> Union[
                "GetApiConnectorFactoriesResponse200ItemFormItemsItemType0",
                "GetApiConnectorFactoriesResponse200ItemFormItemsItemType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    form_items_item_type_0 = GetApiConnectorFactoriesResponse200ItemFormItemsItemType0.from_dict(data)

                    return form_items_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                form_items_item_type_1 = GetApiConnectorFactoriesResponse200ItemFormItemsItemType1.from_dict(data)

                return form_items_item_type_1

            form_items_item = _parse_form_items_item(form_items_item_data)

            form_items.append(form_items_item)

        is_standard = d.pop("isStandard", UNSET)

        get_api_connector_factories_response_200_item = cls(
            type=type,
            id=id,
            target=target,
            name=name,
            description=description,
            logo=logo,
            logo_dark=logo_dark,
            readme=readme,
            platform=platform,
            is_demo=is_demo,
            config_template=config_template,
            form_items=form_items,
            is_standard=is_standard,
        )

        get_api_connector_factories_response_200_item.additional_properties = d
        return get_api_connector_factories_response_200_item

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
