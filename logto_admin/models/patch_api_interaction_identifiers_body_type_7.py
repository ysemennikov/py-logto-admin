from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiInteractionIdentifiersBodyType7")


@_attrs_define
class PatchApiInteractionIdentifiersBodyType7:
    """
    Attributes:
        connector_id (str):
        phone (str):
    """

    connector_id: str
    phone: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
                "phone": phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connector_id = d.pop("connectorId")

        phone = d.pop("phone")

        patch_api_interaction_identifiers_body_type_7 = cls(
            connector_id=connector_id,
            phone=phone,
        )

        patch_api_interaction_identifiers_body_type_7.additional_properties = d
        return patch_api_interaction_identifiers_body_type_7

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
