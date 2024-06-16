from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiOrganizationsResponse200ItemFeaturedUsersItem")


@_attrs_define
class GetApiOrganizationsResponse200ItemFeaturedUsersItem:
    """
    Attributes:
        id (str):
        avatar (Union[None, str]):
        name (Union[None, str]):
    """

    id: str
    avatar: Union[None, str]
    name: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        avatar: Union[None, str]
        avatar = self.avatar

        name: Union[None, str]
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "avatar": avatar,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_avatar(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        avatar = _parse_avatar(d.pop("avatar"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        get_api_organizations_response_200_item_featured_users_item = cls(
            id=id,
            avatar=avatar,
            name=name,
        )

        get_api_organizations_response_200_item_featured_users_item.additional_properties = d
        return get_api_organizations_response_200_item_featured_users_item

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
