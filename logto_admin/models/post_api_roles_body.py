from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_roles_body_type import PostApiRolesBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRolesBody")


@_attrs_define
class PostApiRolesBody:
    """
    Attributes:
        name (str): The name of the role. It should be unique within the tenant.
        description (str):
        type (Union[Unset, PostApiRolesBodyType]): The type of the role. It cannot be changed after creation.
        is_default (Union[Unset, bool]):
        scope_ids (Union[Unset, List[str]]): The initial API resource scopes assigned to the role.
    """

    name: str
    description: str
    type: Union[Unset, PostApiRolesBodyType] = UNSET
    is_default: Union[Unset, bool] = UNSET
    scope_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        is_default = self.is_default

        scope_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scope_ids, Unset):
            scope_ids = self.scope_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if scope_ids is not UNSET:
            field_dict["scopeIds"] = scope_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        _type = d.pop("type", UNSET)
        type: Union[Unset, PostApiRolesBodyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PostApiRolesBodyType(_type)

        is_default = d.pop("isDefault", UNSET)

        scope_ids = cast(List[str], d.pop("scopeIds", UNSET))

        post_api_roles_body = cls(
            name=name,
            description=description,
            type=type,
            is_default=is_default,
            scope_ids=scope_ids,
        )

        post_api_roles_body.additional_properties = d
        return post_api_roles_body

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
