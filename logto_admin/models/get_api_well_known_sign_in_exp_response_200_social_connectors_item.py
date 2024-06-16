from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_platform import (
    GetApiWellKnownSignInExpResponse200SocialConnectorsItemPlatform,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_description import (
        GetApiWellKnownSignInExpResponse200SocialConnectorsItemDescription,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_form_items_item_type_0 import (
        GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_form_items_item_type_1 import (
        GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType1,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_name import (
        GetApiWellKnownSignInExpResponse200SocialConnectorsItemName,
    )


T = TypeVar("T", bound="GetApiWellKnownSignInExpResponse200SocialConnectorsItem")


@_attrs_define
class GetApiWellKnownSignInExpResponse200SocialConnectorsItem:
    """
    Attributes:
        id (str):
        target (str):
        name (GetApiWellKnownSignInExpResponse200SocialConnectorsItemName): Validator function
        description (GetApiWellKnownSignInExpResponse200SocialConnectorsItemDescription): Validator function
        logo (str):
        logo_dark (Union[None, str]):
        readme (str):
        platform (GetApiWellKnownSignInExpResponse200SocialConnectorsItemPlatform):
        config_template (Union[Unset, str]):
        form_items (Union[Unset, List[Union['GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0',
            'GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType1']]]):
        is_standard (Union[Unset, bool]):
    """

    id: str
    target: str
    name: "GetApiWellKnownSignInExpResponse200SocialConnectorsItemName"
    description: "GetApiWellKnownSignInExpResponse200SocialConnectorsItemDescription"
    logo: str
    logo_dark: Union[None, str]
    readme: str
    platform: GetApiWellKnownSignInExpResponse200SocialConnectorsItemPlatform
    config_template: Union[Unset, str] = UNSET
    form_items: Union[
        Unset,
        List[
            Union[
                "GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0",
                "GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType1",
            ]
        ],
    ] = UNSET
    is_standard: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_form_items_item_type_0 import (
            GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0,
        )

        id = self.id

        target = self.target

        name = self.name.to_dict()

        description = self.description.to_dict()

        logo = self.logo

        logo_dark: Union[None, str]
        logo_dark = self.logo_dark

        readme = self.readme

        platform = self.platform.value

        config_template = self.config_template

        form_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.form_items, Unset):
            form_items = []
            for form_items_item_data in self.form_items:
                form_items_item: Dict[str, Any]
                if isinstance(
                    form_items_item_data, GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0
                ):
                    form_items_item = form_items_item_data.to_dict()
                else:
                    form_items_item = form_items_item_data.to_dict()

                form_items.append(form_items_item)

        is_standard = self.is_standard

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if config_template is not UNSET:
            field_dict["configTemplate"] = config_template
        if form_items is not UNSET:
            field_dict["formItems"] = form_items
        if is_standard is not UNSET:
            field_dict["isStandard"] = is_standard

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_description import (
            GetApiWellKnownSignInExpResponse200SocialConnectorsItemDescription,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_form_items_item_type_0 import (
            GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_form_items_item_type_1 import (
            GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType1,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item_name import (
            GetApiWellKnownSignInExpResponse200SocialConnectorsItemName,
        )

        d = src_dict.copy()
        id = d.pop("id")

        target = d.pop("target")

        name = GetApiWellKnownSignInExpResponse200SocialConnectorsItemName.from_dict(d.pop("name"))

        description = GetApiWellKnownSignInExpResponse200SocialConnectorsItemDescription.from_dict(d.pop("description"))

        logo = d.pop("logo")

        def _parse_logo_dark(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        logo_dark = _parse_logo_dark(d.pop("logoDark"))

        readme = d.pop("readme")

        platform = GetApiWellKnownSignInExpResponse200SocialConnectorsItemPlatform(d.pop("platform"))

        config_template = d.pop("configTemplate", UNSET)

        form_items = []
        _form_items = d.pop("formItems", UNSET)
        for form_items_item_data in _form_items or []:

            def _parse_form_items_item(
                data: object,
            ) -> Union[
                "GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0",
                "GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    form_items_item_type_0 = (
                        GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType0.from_dict(data)
                    )

                    return form_items_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                form_items_item_type_1 = (
                    GetApiWellKnownSignInExpResponse200SocialConnectorsItemFormItemsItemType1.from_dict(data)
                )

                return form_items_item_type_1

            form_items_item = _parse_form_items_item(form_items_item_data)

            form_items.append(form_items_item)

        is_standard = d.pop("isStandard", UNSET)

        get_api_well_known_sign_in_exp_response_200_social_connectors_item = cls(
            id=id,
            target=target,
            name=name,
            description=description,
            logo=logo,
            logo_dark=logo_dark,
            readme=readme,
            platform=platform,
            config_template=config_template,
            form_items=form_items,
            is_standard=is_standard,
        )

        get_api_well_known_sign_in_exp_response_200_social_connectors_item.additional_properties = d
        return get_api_well_known_sign_in_exp_response_200_social_connectors_item

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
