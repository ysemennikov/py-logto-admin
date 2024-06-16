from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAuthnHasuraResponse200")


@_attrs_define
class GetApiAuthnHasuraResponse200:
    """
    Attributes:
        x_hasura_user_id (Union[Unset, str]):
        x_hasura_role (Union[Unset, str]):
    """

    x_hasura_user_id: Union[Unset, str] = UNSET
    x_hasura_role: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x_hasura_user_id = self.x_hasura_user_id

        x_hasura_role = self.x_hasura_role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x_hasura_user_id is not UNSET:
            field_dict["X-Hasura-User-Id"] = x_hasura_user_id
        if x_hasura_role is not UNSET:
            field_dict["X-Hasura-Role"] = x_hasura_role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x_hasura_user_id = d.pop("X-Hasura-User-Id", UNSET)

        x_hasura_role = d.pop("X-Hasura-Role", UNSET)

        get_api_authn_hasura_response_200 = cls(
            x_hasura_user_id=x_hasura_user_id,
            x_hasura_role=x_hasura_role,
        )

        get_api_authn_hasura_response_200.additional_properties = d
        return get_api_authn_hasura_response_200

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
