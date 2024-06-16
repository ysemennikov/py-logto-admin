from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_dashboard_users_active_response_200_dau import GetApiDashboardUsersActiveResponse200Dau
    from ..models.get_api_dashboard_users_active_response_200_dau_curve_item import (
        GetApiDashboardUsersActiveResponse200DauCurveItem,
    )
    from ..models.get_api_dashboard_users_active_response_200_mau import GetApiDashboardUsersActiveResponse200Mau
    from ..models.get_api_dashboard_users_active_response_200_wau import GetApiDashboardUsersActiveResponse200Wau


T = TypeVar("T", bound="GetApiDashboardUsersActiveResponse200")


@_attrs_define
class GetApiDashboardUsersActiveResponse200:
    """
    Attributes:
        dau_curve (List['GetApiDashboardUsersActiveResponse200DauCurveItem']):
        dau (GetApiDashboardUsersActiveResponse200Dau):
        wau (GetApiDashboardUsersActiveResponse200Wau):
        mau (GetApiDashboardUsersActiveResponse200Mau):
    """

    dau_curve: List["GetApiDashboardUsersActiveResponse200DauCurveItem"]
    dau: "GetApiDashboardUsersActiveResponse200Dau"
    wau: "GetApiDashboardUsersActiveResponse200Wau"
    mau: "GetApiDashboardUsersActiveResponse200Mau"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dau_curve = []
        for dau_curve_item_data in self.dau_curve:
            dau_curve_item = dau_curve_item_data.to_dict()
            dau_curve.append(dau_curve_item)

        dau = self.dau.to_dict()

        wau = self.wau.to_dict()

        mau = self.mau.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dauCurve": dau_curve,
                "dau": dau,
                "wau": wau,
                "mau": mau,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_dashboard_users_active_response_200_dau import GetApiDashboardUsersActiveResponse200Dau
        from ..models.get_api_dashboard_users_active_response_200_dau_curve_item import (
            GetApiDashboardUsersActiveResponse200DauCurveItem,
        )
        from ..models.get_api_dashboard_users_active_response_200_mau import GetApiDashboardUsersActiveResponse200Mau
        from ..models.get_api_dashboard_users_active_response_200_wau import GetApiDashboardUsersActiveResponse200Wau

        d = src_dict.copy()
        dau_curve = []
        _dau_curve = d.pop("dauCurve")
        for dau_curve_item_data in _dau_curve:
            dau_curve_item = GetApiDashboardUsersActiveResponse200DauCurveItem.from_dict(dau_curve_item_data)

            dau_curve.append(dau_curve_item)

        dau = GetApiDashboardUsersActiveResponse200Dau.from_dict(d.pop("dau"))

        wau = GetApiDashboardUsersActiveResponse200Wau.from_dict(d.pop("wau"))

        mau = GetApiDashboardUsersActiveResponse200Mau.from_dict(d.pop("mau"))

        get_api_dashboard_users_active_response_200 = cls(
            dau_curve=dau_curve,
            dau=dau,
            wau=wau,
            mau=mau,
        )

        get_api_dashboard_users_active_response_200.additional_properties = d
        return get_api_dashboard_users_active_response_200

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
