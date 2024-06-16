from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_logs_id_response_200_payload import GetApiLogsIdResponse200Payload


T = TypeVar("T", bound="GetApiLogsIdResponse200")


@_attrs_define
class GetApiLogsIdResponse200:
    """
    Attributes:
        id (str):
        key (str):
        payload (GetApiLogsIdResponse200Payload):
        created_at (float):
    """

    id: str
    key: str
    payload: "GetApiLogsIdResponse200Payload"
    created_at: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        key = self.key

        payload = self.payload.to_dict()

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "payload": payload,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_logs_id_response_200_payload import GetApiLogsIdResponse200Payload

        d = src_dict.copy()
        id = d.pop("id")

        key = d.pop("key")

        payload = GetApiLogsIdResponse200Payload.from_dict(d.pop("payload"))

        created_at = d.pop("createdAt")

        get_api_logs_id_response_200 = cls(
            id=id,
            key=key,
            payload=payload,
            created_at=created_at,
        )

        get_api_logs_id_response_200.additional_properties = d
        return get_api_logs_id_response_200

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
