from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiResourcesBody")


@_attrs_define
class PostApiResourcesBody:
    """
    Attributes:
        name (str): The name of the resource.
        indicator (str): The unique resource indicator. Should be a valid URI.
        access_token_ttl (Union[Unset, float]): The access token TTL in seconds. It affects the `exp` claim of the
            access token granted for this resource. Default: 3600.0.
    """

    name: str
    indicator: str
    access_token_ttl: Union[Unset, float] = 3600.0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        indicator = self.indicator

        access_token_ttl = self.access_token_ttl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "indicator": indicator,
            }
        )
        if access_token_ttl is not UNSET:
            field_dict["accessTokenTtl"] = access_token_ttl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        indicator = d.pop("indicator")

        access_token_ttl = d.pop("accessTokenTtl", UNSET)

        post_api_resources_body = cls(
            name=name,
            indicator=indicator,
            access_token_ttl=access_token_ttl,
        )

        post_api_resources_body.additional_properties = d
        return post_api_resources_body

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
