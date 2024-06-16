from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_api_interaction_body_identifier_type_5_connector_data import (
        PutApiInteractionBodyIdentifierType5ConnectorData,
    )


T = TypeVar("T", bound="PutApiInteractionBodyIdentifierType5")


@_attrs_define
class PutApiInteractionBodyIdentifierType5:
    """
    Attributes:
        connector_id (str):
        connector_data (PutApiInteractionBodyIdentifierType5ConnectorData): arbitrary
    """

    connector_id: str
    connector_data: "PutApiInteractionBodyIdentifierType5ConnectorData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        connector_data = self.connector_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
                "connectorData": connector_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_interaction_body_identifier_type_5_connector_data import (
            PutApiInteractionBodyIdentifierType5ConnectorData,
        )

        d = src_dict.copy()
        connector_id = d.pop("connectorId")

        connector_data = PutApiInteractionBodyIdentifierType5ConnectorData.from_dict(d.pop("connectorData"))

        put_api_interaction_body_identifier_type_5 = cls(
            connector_id=connector_id,
            connector_data=connector_data,
        )

        put_api_interaction_body_identifier_type_5.additional_properties = d
        return put_api_interaction_body_identifier_type_5

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
