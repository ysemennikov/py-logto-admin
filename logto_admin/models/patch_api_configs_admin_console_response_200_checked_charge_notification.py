from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiConfigsAdminConsoleResponse200CheckedChargeNotification")


@_attrs_define
class PatchApiConfigsAdminConsoleResponse200CheckedChargeNotification:
    """
    Attributes:
        token (Union[Unset, bool]):
        api_resource (Union[Unset, bool]):
        machine_to_machine_app (Union[Unset, bool]):
        tenant_member (Union[Unset, bool]):
    """

    token: Union[Unset, bool] = UNSET
    api_resource: Union[Unset, bool] = UNSET
    machine_to_machine_app: Union[Unset, bool] = UNSET
    tenant_member: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        api_resource = self.api_resource

        machine_to_machine_app = self.machine_to_machine_app

        tenant_member = self.tenant_member

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if api_resource is not UNSET:
            field_dict["apiResource"] = api_resource
        if machine_to_machine_app is not UNSET:
            field_dict["machineToMachineApp"] = machine_to_machine_app
        if tenant_member is not UNSET:
            field_dict["tenantMember"] = tenant_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        api_resource = d.pop("apiResource", UNSET)

        machine_to_machine_app = d.pop("machineToMachineApp", UNSET)

        tenant_member = d.pop("tenantMember", UNSET)

        patch_api_configs_admin_console_response_200_checked_charge_notification = cls(
            token=token,
            api_resource=api_resource,
            machine_to_machine_app=machine_to_machine_app,
            tenant_member=tenant_member,
        )

        patch_api_configs_admin_console_response_200_checked_charge_notification.additional_properties = d
        return patch_api_configs_admin_console_response_200_checked_charge_notification

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
