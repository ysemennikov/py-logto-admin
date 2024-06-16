from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item import (
        PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem,
    )


T = TypeVar("T", bound="PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItem")


@_attrs_define
class PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItem:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        scopes (List['PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem']):
    """

    id: str
    name: str
    description: str
    scopes: List["PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem"]
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
        from ..models.put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item import (
            PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = (
                PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem.from_dict(
                    scopes_item_data
                )
            )

            scopes.append(scopes_item)

        put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item = cls(
            id=id,
            name=name,
            description=description,
            scopes=scopes,
        )

        put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item.additional_properties = d
        return put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item

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
