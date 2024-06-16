from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_connectors_id_response_200_platform import GetApiConnectorsIdResponse200Platform
from ..models.get_api_connectors_id_response_200_type import GetApiConnectorsIdResponse200Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_connectors_id_response_200_config import GetApiConnectorsIdResponse200Config
    from ..models.get_api_connectors_id_response_200_description import GetApiConnectorsIdResponse200Description
    from ..models.get_api_connectors_id_response_200_extra_info import GetApiConnectorsIdResponse200ExtraInfo
    from ..models.get_api_connectors_id_response_200_form_items_item_type_0 import (
        GetApiConnectorsIdResponse200FormItemsItemType0,
    )
    from ..models.get_api_connectors_id_response_200_form_items_item_type_1 import (
        GetApiConnectorsIdResponse200FormItemsItemType1,
    )
    from ..models.get_api_connectors_id_response_200_metadata import GetApiConnectorsIdResponse200Metadata
    from ..models.get_api_connectors_id_response_200_name import GetApiConnectorsIdResponse200Name


T = TypeVar("T", bound="GetApiConnectorsIdResponse200")


@_attrs_define
class GetApiConnectorsIdResponse200:
    """
    Attributes:
        id (str):
        sync_profile (bool):
        config (GetApiConnectorsIdResponse200Config): arbitrary
        metadata (GetApiConnectorsIdResponse200Metadata):
        connector_id (str):
        target (str):
        name (GetApiConnectorsIdResponse200Name): Validator function
        description (GetApiConnectorsIdResponse200Description): Validator function
        logo (str):
        logo_dark (Union[None, str]):
        readme (str):
        platform (GetApiConnectorsIdResponse200Platform):
        type (GetApiConnectorsIdResponse200Type):
        config_template (Union[Unset, str]):
        form_items (Union[Unset, List[Union['GetApiConnectorsIdResponse200FormItemsItemType0',
            'GetApiConnectorsIdResponse200FormItemsItemType1']]]):
        is_standard (Union[Unset, bool]):
        is_demo (Union[Unset, bool]):
        extra_info (Union[Unset, GetApiConnectorsIdResponse200ExtraInfo]):
        usage (Union[Unset, float]):
    """

    id: str
    sync_profile: bool
    config: "GetApiConnectorsIdResponse200Config"
    metadata: "GetApiConnectorsIdResponse200Metadata"
    connector_id: str
    target: str
    name: "GetApiConnectorsIdResponse200Name"
    description: "GetApiConnectorsIdResponse200Description"
    logo: str
    logo_dark: Union[None, str]
    readme: str
    platform: GetApiConnectorsIdResponse200Platform
    type: GetApiConnectorsIdResponse200Type
    config_template: Union[Unset, str] = UNSET
    form_items: Union[
        Unset,
        List[
            Union["GetApiConnectorsIdResponse200FormItemsItemType0", "GetApiConnectorsIdResponse200FormItemsItemType1"]
        ],
    ] = UNSET
    is_standard: Union[Unset, bool] = UNSET
    is_demo: Union[Unset, bool] = UNSET
    extra_info: Union[Unset, "GetApiConnectorsIdResponse200ExtraInfo"] = UNSET
    usage: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_connectors_id_response_200_form_items_item_type_0 import (
            GetApiConnectorsIdResponse200FormItemsItemType0,
        )

        id = self.id

        sync_profile = self.sync_profile

        config = self.config.to_dict()

        metadata = self.metadata.to_dict()

        connector_id = self.connector_id

        target = self.target

        name = self.name.to_dict()

        description = self.description.to_dict()

        logo = self.logo

        logo_dark: Union[None, str]
        logo_dark = self.logo_dark

        readme = self.readme

        platform = self.platform.value

        type = self.type.value

        config_template = self.config_template

        form_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.form_items, Unset):
            form_items = []
            for form_items_item_data in self.form_items:
                form_items_item: Dict[str, Any]
                if isinstance(form_items_item_data, GetApiConnectorsIdResponse200FormItemsItemType0):
                    form_items_item = form_items_item_data.to_dict()
                else:
                    form_items_item = form_items_item_data.to_dict()

                form_items.append(form_items_item)

        is_standard = self.is_standard

        is_demo = self.is_demo

        extra_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_info, Unset):
            extra_info = self.extra_info.to_dict()

        usage = self.usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "syncProfile": sync_profile,
                "config": config,
                "metadata": metadata,
                "connectorId": connector_id,
                "target": target,
                "name": name,
                "description": description,
                "logo": logo,
                "logoDark": logo_dark,
                "readme": readme,
                "platform": platform,
                "type": type,
            }
        )
        if config_template is not UNSET:
            field_dict["configTemplate"] = config_template
        if form_items is not UNSET:
            field_dict["formItems"] = form_items
        if is_standard is not UNSET:
            field_dict["isStandard"] = is_standard
        if is_demo is not UNSET:
            field_dict["isDemo"] = is_demo
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_connectors_id_response_200_config import GetApiConnectorsIdResponse200Config
        from ..models.get_api_connectors_id_response_200_description import GetApiConnectorsIdResponse200Description
        from ..models.get_api_connectors_id_response_200_extra_info import GetApiConnectorsIdResponse200ExtraInfo
        from ..models.get_api_connectors_id_response_200_form_items_item_type_0 import (
            GetApiConnectorsIdResponse200FormItemsItemType0,
        )
        from ..models.get_api_connectors_id_response_200_form_items_item_type_1 import (
            GetApiConnectorsIdResponse200FormItemsItemType1,
        )
        from ..models.get_api_connectors_id_response_200_metadata import GetApiConnectorsIdResponse200Metadata
        from ..models.get_api_connectors_id_response_200_name import GetApiConnectorsIdResponse200Name

        d = src_dict.copy()
        id = d.pop("id")

        sync_profile = d.pop("syncProfile")

        config = GetApiConnectorsIdResponse200Config.from_dict(d.pop("config"))

        metadata = GetApiConnectorsIdResponse200Metadata.from_dict(d.pop("metadata"))

        connector_id = d.pop("connectorId")

        target = d.pop("target")

        name = GetApiConnectorsIdResponse200Name.from_dict(d.pop("name"))

        description = GetApiConnectorsIdResponse200Description.from_dict(d.pop("description"))

        logo = d.pop("logo")

        def _parse_logo_dark(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        logo_dark = _parse_logo_dark(d.pop("logoDark"))

        readme = d.pop("readme")

        platform = GetApiConnectorsIdResponse200Platform(d.pop("platform"))

        type = GetApiConnectorsIdResponse200Type(d.pop("type"))

        config_template = d.pop("configTemplate", UNSET)

        form_items = []
        _form_items = d.pop("formItems", UNSET)
        for form_items_item_data in _form_items or []:

            def _parse_form_items_item(
                data: object,
            ) -> Union[
                "GetApiConnectorsIdResponse200FormItemsItemType0", "GetApiConnectorsIdResponse200FormItemsItemType1"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    form_items_item_type_0 = GetApiConnectorsIdResponse200FormItemsItemType0.from_dict(data)

                    return form_items_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                form_items_item_type_1 = GetApiConnectorsIdResponse200FormItemsItemType1.from_dict(data)

                return form_items_item_type_1

            form_items_item = _parse_form_items_item(form_items_item_data)

            form_items.append(form_items_item)

        is_standard = d.pop("isStandard", UNSET)

        is_demo = d.pop("isDemo", UNSET)

        _extra_info = d.pop("extraInfo", UNSET)
        extra_info: Union[Unset, GetApiConnectorsIdResponse200ExtraInfo]
        if isinstance(_extra_info, Unset):
            extra_info = UNSET
        else:
            extra_info = GetApiConnectorsIdResponse200ExtraInfo.from_dict(_extra_info)

        usage = d.pop("usage", UNSET)

        get_api_connectors_id_response_200 = cls(
            id=id,
            sync_profile=sync_profile,
            config=config,
            metadata=metadata,
            connector_id=connector_id,
            target=target,
            name=name,
            description=description,
            logo=logo,
            logo_dark=logo_dark,
            readme=readme,
            platform=platform,
            type=type,
            config_template=config_template,
            form_items=form_items,
            is_standard=is_standard,
            is_demo=is_demo,
            extra_info=extra_info,
            usage=usage,
        )

        get_api_connectors_id_response_200.additional_properties = d
        return get_api_connectors_id_response_200

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
