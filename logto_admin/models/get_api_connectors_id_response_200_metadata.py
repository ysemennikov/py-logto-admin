from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_connectors_id_response_200_metadata_name import GetApiConnectorsIdResponse200MetadataName


T = TypeVar("T", bound="GetApiConnectorsIdResponse200Metadata")


@_attrs_define
class GetApiConnectorsIdResponse200Metadata:
    """
    Attributes:
        target (Union[Unset, str]):
        name (Union[Unset, GetApiConnectorsIdResponse200MetadataName]): Validator function
        logo (Union[Unset, str]):
        logo_dark (Union[None, Unset, str]):
    """

    target: Union[Unset, str] = UNSET
    name: Union[Unset, "GetApiConnectorsIdResponse200MetadataName"] = UNSET
    logo: Union[Unset, str] = UNSET
    logo_dark: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target = self.target

        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        logo = self.logo

        logo_dark: Union[None, Unset, str]
        if isinstance(self.logo_dark, Unset):
            logo_dark = UNSET
        else:
            logo_dark = self.logo_dark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logo_dark is not UNSET:
            field_dict["logoDark"] = logo_dark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_connectors_id_response_200_metadata_name import GetApiConnectorsIdResponse200MetadataName

        d = src_dict.copy()
        target = d.pop("target", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, GetApiConnectorsIdResponse200MetadataName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = GetApiConnectorsIdResponse200MetadataName.from_dict(_name)

        logo = d.pop("logo", UNSET)

        def _parse_logo_dark(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_dark = _parse_logo_dark(d.pop("logoDark", UNSET))

        get_api_connectors_id_response_200_metadata = cls(
            target=target,
            name=name,
            logo=logo,
            logo_dark=logo_dark,
        )

        get_api_connectors_id_response_200_metadata.additional_properties = d
        return get_api_connectors_id_response_200_metadata

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
