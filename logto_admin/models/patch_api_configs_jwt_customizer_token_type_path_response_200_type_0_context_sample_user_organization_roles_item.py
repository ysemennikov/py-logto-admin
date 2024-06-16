from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserOrganizationRolesItem"
)


@_attrs_define
class PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserOrganizationRolesItem:
    """
    Attributes:
        organization_id (str):
        role_id (str):
        role_name (str):
    """

    organization_id: str
    role_id: str
    role_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_id = self.organization_id

        role_id = self.role_id

        role_name = self.role_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationId": organization_id,
                "roleId": role_id,
                "roleName": role_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_id = d.pop("organizationId")

        role_id = d.pop("roleId")

        role_name = d.pop("roleName")

        patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_organization_roles_item = cls(
            organization_id=organization_id,
            role_id=role_id,
            role_name=role_name,
        )

        patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_organization_roles_item.additional_properties = d
        return patch_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_organization_roles_item

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
