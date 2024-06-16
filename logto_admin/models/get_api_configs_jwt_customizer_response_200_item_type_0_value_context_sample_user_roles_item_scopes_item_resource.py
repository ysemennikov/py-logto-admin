from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItemScopesItemResource"
)


@_attrs_define
class GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItemScopesItemResource:
    """
    Attributes:
        id (str):
        name (str):
        indicator (str):
        is_default (bool):
        access_token_ttl (float):
    """

    id: str
    name: str
    indicator: str
    is_default: bool
    access_token_ttl: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        indicator = self.indicator

        is_default = self.is_default

        access_token_ttl = self.access_token_ttl

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        indicator = d.pop("indicator")

        is_default = d.pop("isDefault")

        access_token_ttl = d.pop("accessTokenTtl")

        get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_roles_item_scopes_item_resource = cls(
            id=id,
            name=name,
            indicator=indicator,
            is_default=is_default,
            access_token_ttl=access_token_ttl,
        )

        get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_roles_item_scopes_item_resource.additional_properties = d
        return get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_roles_item_scopes_item_resource

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
