from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_dashboard_users_new_response_200_last_7_days import (
        GetApiDashboardUsersNewResponse200Last7Days,
    )
    from ..models.get_api_dashboard_users_new_response_200_today import GetApiDashboardUsersNewResponse200Today


T = TypeVar("T", bound="GetApiDashboardUsersNewResponse200")


@_attrs_define
class GetApiDashboardUsersNewResponse200:
    """
    Attributes:
        today (GetApiDashboardUsersNewResponse200Today):
        last_7_days (GetApiDashboardUsersNewResponse200Last7Days):
    """

    today: "GetApiDashboardUsersNewResponse200Today"
    last_7_days: "GetApiDashboardUsersNewResponse200Last7Days"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        today = self.today.to_dict()

        last_7_days = self.last_7_days.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "today": today,
                "last7Days": last_7_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_dashboard_users_new_response_200_last_7_days import (
            GetApiDashboardUsersNewResponse200Last7Days,
        )
        from ..models.get_api_dashboard_users_new_response_200_today import GetApiDashboardUsersNewResponse200Today

        d = src_dict.copy()
        today = GetApiDashboardUsersNewResponse200Today.from_dict(d.pop("today"))

        last_7_days = GetApiDashboardUsersNewResponse200Last7Days.from_dict(d.pop("last7Days"))

        get_api_dashboard_users_new_response_200 = cls(
            today=today,
            last_7_days=last_7_days,
        )

        get_api_dashboard_users_new_response_200.additional_properties = d
        return get_api_dashboard_users_new_response_200

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
