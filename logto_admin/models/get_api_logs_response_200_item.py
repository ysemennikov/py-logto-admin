from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_logs_response_200_item_payload import GetApiLogsResponse200ItemPayload


T = TypeVar("T", bound="GetApiLogsResponse200Item")


@_attrs_define
class GetApiLogsResponse200Item:
    """
    Attributes:
        id (str):
        key (str):
        payload (GetApiLogsResponse200ItemPayload):
        created_at (float):
    """

    id: str
    key: str
    payload: "GetApiLogsResponse200ItemPayload"
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
        from ..models.get_api_logs_response_200_item_payload import GetApiLogsResponse200ItemPayload

        d = src_dict.copy()
        id = d.pop("id")

        key = d.pop("key")

        payload = GetApiLogsResponse200ItemPayload.from_dict(d.pop("payload"))

        created_at = d.pop("createdAt")

        get_api_logs_response_200_item = cls(
            id=id,
            key=key,
            payload=payload,
            created_at=created_at,
        )

        get_api_logs_response_200_item.additional_properties = d
        return get_api_logs_response_200_item

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
