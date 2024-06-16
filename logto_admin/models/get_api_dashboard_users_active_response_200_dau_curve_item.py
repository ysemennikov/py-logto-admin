from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiDashboardUsersActiveResponse200DauCurveItem")


@_attrs_define
class GetApiDashboardUsersActiveResponse200DauCurveItem:
    """
    Attributes:
        date (str):
        count (float):
    """

    date: str
    count: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        count = d.pop("count")

        get_api_dashboard_users_active_response_200_dau_curve_item = cls(
            date=date,
            count=count,
        )

        get_api_dashboard_users_active_response_200_dau_curve_item.additional_properties = d
        return get_api_dashboard_users_active_response_200_dau_curve_item

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
