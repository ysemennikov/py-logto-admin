from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item_scopes_item import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItemScopesItem,
    )


T = TypeVar("T", bound="PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem")


@_attrs_define
class PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        scopes (List['PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItemScopesItem']):
    """

    id: str
    name: str
    description: str
    scopes: List["PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItemScopesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

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
                "description": description,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item_scopes_item import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItemScopesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItemScopesItem.from_dict(
                scopes_item_data
            )

            scopes.append(scopes_item)

        post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item = cls(
            id=id,
            name=name,
            description=description,
            scopes=scopes,
        )

        post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item.additional_properties = d
        return post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item

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
