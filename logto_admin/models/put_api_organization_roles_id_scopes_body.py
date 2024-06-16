from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiOrganizationRolesIdScopesBody")


@_attrs_define
class PutApiOrganizationRolesIdScopesBody:
    """
    Attributes:
        organization_scope_ids (List[str]): An array of organization scope IDs to replace existing scopes.
    """

    organization_scope_ids: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_scope_ids = self.organization_scope_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationScopeIds": organization_scope_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_scope_ids = cast(List[str], d.pop("organizationScopeIds"))

        put_api_organization_roles_id_scopes_body = cls(
            organization_scope_ids=organization_scope_ids,
        )

        put_api_organization_roles_id_scopes_body.additional_properties = d
        return put_api_organization_roles_id_scopes_body

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
