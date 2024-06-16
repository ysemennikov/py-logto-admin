from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiWellKnownSignInExpResponse200SsoConnectorsItem")


@_attrs_define
class GetApiWellKnownSignInExpResponse200SsoConnectorsItem:
    """
    Attributes:
        id (str):
        connector_name (str):
        logo (str):
        dark_logo (Union[Unset, str]):
    """

    id: str
    connector_name: str
    logo: str
    dark_logo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        connector_name = self.connector_name

        logo = self.logo

        dark_logo = self.dark_logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "connectorName": connector_name,
                "logo": logo,
            }
        )
        if dark_logo is not UNSET:
            field_dict["darkLogo"] = dark_logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        connector_name = d.pop("connectorName")

        logo = d.pop("logo")

        dark_logo = d.pop("darkLogo", UNSET)

        get_api_well_known_sign_in_exp_response_200_sso_connectors_item = cls(
            id=id,
            connector_name=connector_name,
            logo=logo,
            dark_logo=dark_logo,
        )

        get_api_well_known_sign_in_exp_response_200_sso_connectors_item.additional_properties = d
        return get_api_well_known_sign_in_exp_response_200_sso_connectors_item

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
