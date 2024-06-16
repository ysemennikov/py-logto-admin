from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiDashboardUsersNewResponse200Last7Days")


@_attrs_define
class GetApiDashboardUsersNewResponse200Last7Days:
    """
    Attributes:
        count (float):
        delta (float):
    """

    count: float
    delta: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        delta = self.delta

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "delta": delta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        delta = d.pop("delta")

        get_api_dashboard_users_new_response_200_last_7_days = cls(
            count=count,
            delta=delta,
        )

        get_api_dashboard_users_new_response_200_last_7_days.additional_properties = d
        return get_api_dashboard_users_new_response_200_last_7_days

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
