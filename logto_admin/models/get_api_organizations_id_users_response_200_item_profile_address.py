from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiOrganizationsIdUsersResponse200ItemProfileAddress")


@_attrs_define
class GetApiOrganizationsIdUsersResponse200ItemProfileAddress:
    """
    Attributes:
        formatted (Union[Unset, str]):
        street_address (Union[Unset, str]):
        locality (Union[Unset, str]):
        region (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    formatted: Union[Unset, str] = UNSET
    street_address: Union[Unset, str] = UNSET
    locality: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formatted = self.formatted

        street_address = self.street_address

        locality = self.locality

        region = self.region

        postal_code = self.postal_code

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if formatted is not UNSET:
            field_dict["formatted"] = formatted
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address
        if locality is not UNSET:
            field_dict["locality"] = locality
        if region is not UNSET:
            field_dict["region"] = region
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formatted = d.pop("formatted", UNSET)

        street_address = d.pop("streetAddress", UNSET)

        locality = d.pop("locality", UNSET)

        region = d.pop("region", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        get_api_organizations_id_users_response_200_item_profile_address = cls(
            formatted=formatted,
            street_address=street_address,
            locality=locality,
            region=region,
            postal_code=postal_code,
            country=country,
        )

        get_api_organizations_id_users_response_200_item_profile_address.additional_properties = d
        return get_api_organizations_id_users_response_200_item_profile_address

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
