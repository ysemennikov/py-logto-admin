from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiResourcesIdBody")


@_attrs_define
class PatchApiResourcesIdBody:
    """
    Attributes:
        name (Union[Unset, str]): The updated name of the resource.
        access_token_ttl (Union[Unset, float]): The updated access token TTL in seconds.
    """

    name: Union[Unset, str] = UNSET
    access_token_ttl: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        access_token_ttl = self.access_token_ttl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if access_token_ttl is not UNSET:
            field_dict["accessTokenTtl"] = access_token_ttl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        access_token_ttl = d.pop("accessTokenTtl", UNSET)

        patch_api_resources_id_body = cls(
            name=name,
            access_token_ttl=access_token_ttl,
        )

        patch_api_resources_id_body.additional_properties = d
        return patch_api_resources_id_body

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
