from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiHooksResponse200ItemExecutionStats")


@_attrs_define
class GetApiHooksResponse200ItemExecutionStats:
    """
    Attributes:
        success_count (float):
        request_count (float):
    """

    success_count: float
    request_count: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success_count = self.success_count

        request_count = self.request_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "successCount": success_count,
                "requestCount": request_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success_count = d.pop("successCount")

        request_count = d.pop("requestCount")

        get_api_hooks_response_200_item_execution_stats = cls(
            success_count=success_count,
            request_count=request_count,
        )

        get_api_hooks_response_200_item_execution_stats.additional_properties = d
        return get_api_hooks_response_200_item_execution_stats

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
