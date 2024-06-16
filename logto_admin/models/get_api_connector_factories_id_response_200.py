from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_connector_factories_id_response_200_platform import GetApiConnectorFactoriesIdResponse200Platform
from ..models.get_api_connector_factories_id_response_200_type import GetApiConnectorFactoriesIdResponse200Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_connector_factories_id_response_200_description import (
        GetApiConnectorFactoriesIdResponse200Description,
    )
    from ..models.get_api_connector_factories_id_response_200_form_items_item_type_0 import (
        GetApiConnectorFactoriesIdResponse200FormItemsItemType0,
    )
    from ..models.get_api_connector_factories_id_response_200_form_items_item_type_1 import (
        GetApiConnectorFactoriesIdResponse200FormItemsItemType1,
    )
    from ..models.get_api_connector_factories_id_response_200_name import GetApiConnectorFactoriesIdResponse200Name


T = TypeVar("T", bound="GetApiConnectorFactoriesIdResponse200")


@_attrs_define
class GetApiConnectorFactoriesIdResponse200:
    """
    Attributes:
        type (GetApiConnectorFactoriesIdResponse200Type):
        id (str):
        target (str):
        name (GetApiConnectorFactoriesIdResponse200Name): Validator function
        description (GetApiConnectorFactoriesIdResponse200Description): Validator function
        logo (str):
        logo_dark (Union[None, str]):
        readme (str):
        platform (GetApiConnectorFactoriesIdResponse200Platform):
        is_demo (Union[Unset, bool]):
        config_template (Union[Unset, str]):
        form_items (Union[Unset, List[Union['GetApiConnectorFactoriesIdResponse200FormItemsItemType0',
            'GetApiConnectorFactoriesIdResponse200FormItemsItemType1']]]):
        is_standard (Union[Unset, bool]):
    """

    type: GetApiConnectorFactoriesIdResponse200Type
    id: str
    target: str
    name: "GetApiConnectorFactoriesIdResponse200Name"
    description: "GetApiConnectorFactoriesIdResponse200Description"
    logo: str
    logo_dark: Union[None, str]
    readme: str
    platform: GetApiConnectorFactoriesIdResponse200Platform
    is_demo: Union[Unset, bool] = UNSET
    config_template: Union[Unset, str] = UNSET
    form_items: Union[
        Unset,
        List[
            Union[
                "GetApiConnectorFactoriesIdResponse200FormItemsItemType0",
                "GetApiConnectorFactoriesIdResponse200FormItemsItemType1",
            ]
        ],
    ] = UNSET
    is_standard: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_connector_factories_id_response_200_form_items_item_type_0 import (
            GetApiConnectorFactoriesIdResponse200FormItemsItemType0,
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
                if isinstance(form_items_item_data, GetApiConnectorFactoriesIdResponse200FormItemsItemType0):
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
        from ..models.get_api_connector_factories_id_response_200_description import (
            GetApiConnectorFactoriesIdResponse200Description,
        )
        from ..models.get_api_connector_factories_id_response_200_form_items_item_type_0 import (
            GetApiConnectorFactoriesIdResponse200FormItemsItemType0,
        )
        from ..models.get_api_connector_factories_id_response_200_form_items_item_type_1 import (
            GetApiConnectorFactoriesIdResponse200FormItemsItemType1,
        )
        from ..models.get_api_connector_factories_id_response_200_name import GetApiConnectorFactoriesIdResponse200Name

        d = src_dict.copy()
        type = GetApiConnectorFactoriesIdResponse200Type(d.pop("type"))

        id = d.pop("id")

        target = d.pop("target")

        name = GetApiConnectorFactoriesIdResponse200Name.from_dict(d.pop("name"))

        description = GetApiConnectorFactoriesIdResponse200Description.from_dict(d.pop("description"))

        logo = d.pop("logo")

        def _parse_logo_dark(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        logo_dark = _parse_logo_dark(d.pop("logoDark"))

        readme = d.pop("readme")

        platform = GetApiConnectorFactoriesIdResponse200Platform(d.pop("platform"))

        is_demo = d.pop("isDemo", UNSET)

        config_template = d.pop("configTemplate", UNSET)

        form_items = []
        _form_items = d.pop("formItems", UNSET)
        for form_items_item_data in _form_items or []:

            def _parse_form_items_item(
                data: object,
            ) -> Union[
                "GetApiConnectorFactoriesIdResponse200FormItemsItemType0",
                "GetApiConnectorFactoriesIdResponse200FormItemsItemType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    form_items_item_type_0 = GetApiConnectorFactoriesIdResponse200FormItemsItemType0.from_dict(data)

                    return form_items_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                form_items_item_type_1 = GetApiConnectorFactoriesIdResponse200FormItemsItemType1.from_dict(data)

                return form_items_item_type_1

            form_items_item = _parse_form_items_item(form_items_item_data)

            form_items.append(form_items_item)

        is_standard = d.pop("isStandard", UNSET)

        get_api_connector_factories_id_response_200 = cls(
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

        get_api_connector_factories_id_response_200.additional_properties = d
        return get_api_connector_factories_id_response_200

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
