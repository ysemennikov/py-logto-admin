from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_resources_response_200_item_scopes_item import GetApiResourcesResponse200ItemScopesItem


T = TypeVar("T", bound="GetApiResourcesResponse200Item")


@_attrs_define
class GetApiResourcesResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        indicator (str):
        is_default (bool):
        access_token_ttl (float):
        scopes (Union[Unset, List['GetApiResourcesResponse200ItemScopesItem']]):
    """

    id: str
    name: str
    indicator: str
    is_default: bool
    access_token_ttl: float
    scopes: Union[Unset, List["GetApiResourcesResponse200ItemScopesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        indicator = self.indicator

        is_default = self.is_default

        access_token_ttl = self.access_token_ttl

        scopes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "indicator": indicator,
                "isDefault": is_default,
                "accessTokenTtl": access_token_ttl,
            }
        )
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_resources_response_200_item_scopes_item import GetApiResourcesResponse200ItemScopesItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        indicator = d.pop("indicator")

        is_default = d.pop("isDefault")

        access_token_ttl = d.pop("accessTokenTtl")

        scopes = []
        _scopes = d.pop("scopes", UNSET)
        for scopes_item_data in _scopes or []:
            scopes_item = GetApiResourcesResponse200ItemScopesItem.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        get_api_resources_response_200_item = cls(
            id=id,
            name=name,
            indicator=indicator,
            is_default=is_default,
            access_token_ttl=access_token_ttl,
            scopes=scopes,
        )

        get_api_resources_response_200_item.additional_properties = d
        return get_api_resources_response_200_item

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
