from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item_resource import (
        PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItemResource,
    )


T = TypeVar("T", bound="PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem")


@_attrs_define
class PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItem:
    """
    Attributes:
        id (str):
        name (str):
        description (Union[None, str]):
        resource_id (str):
        resource
            (PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItemResource):
    """

    id: str
    name: str
    description: Union[None, str]
    resource_id: str
    resource: "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItemResource"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, str]
        description = self.description

        resource_id = self.resource_id

        resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "resourceId": resource_id,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item_resource import (
            PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItemResource,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        resource_id = d.pop("resourceId")

        resource = PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserRolesItemScopesItemResource.from_dict(
            d.pop("resource")
        )

        patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item = cls(
            id=id,
            name=name,
            description=description,
            resource_id=resource_id,
            resource=resource,
        )

        patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item.additional_properties = d
        return patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_roles_item_scopes_item

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
