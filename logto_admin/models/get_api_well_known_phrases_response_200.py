from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_well_known_phrases_response_200_additional_property_type_1 import (
        GetApiWellKnownPhrasesResponse200AdditionalPropertyType1,
    )


T = TypeVar("T", bound="GetApiWellKnownPhrasesResponse200")


@_attrs_define
class GetApiWellKnownPhrasesResponse200:
    """ """

    additional_properties: Dict[str, Union["GetApiWellKnownPhrasesResponse200AdditionalPropertyType1", str]] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_well_known_phrases_response_200_additional_property_type_1 import (
            GetApiWellKnownPhrasesResponse200AdditionalPropertyType1,
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, GetApiWellKnownPhrasesResponse200AdditionalPropertyType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_well_known_phrases_response_200_additional_property_type_1 import (
            GetApiWellKnownPhrasesResponse200AdditionalPropertyType1,
        )

        d = src_dict.copy()
        get_api_well_known_phrases_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union["GetApiWellKnownPhrasesResponse200AdditionalPropertyType1", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = GetApiWellKnownPhrasesResponse200AdditionalPropertyType1.from_dict(
                        data
                    )

                    return additional_property_type_1
                except:  # noqa: E722
                    pass
                return cast(Union["GetApiWellKnownPhrasesResponse200AdditionalPropertyType1", str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        get_api_well_known_phrases_response_200.additional_properties = additional_properties
        return get_api_well_known_phrases_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["GetApiWellKnownPhrasesResponse200AdditionalPropertyType1", str]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union["GetApiWellKnownPhrasesResponse200AdditionalPropertyType1", str]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
