from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification")


@_attrs_define
class PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification:
    """
    Attributes:
        is_paid_tenant (bool):
        tag (str):
        read_at (Union[Unset, float]):
    """

    is_paid_tenant: bool
    tag: str
    read_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_paid_tenant = self.is_paid_tenant

        tag = self.tag

        read_at = self.read_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isPaidTenant": is_paid_tenant,
                "tag": tag,
            }
        )
        if read_at is not UNSET:
            field_dict["readAt"] = read_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_paid_tenant = d.pop("isPaidTenant")

        tag = d.pop("tag")

        read_at = d.pop("readAt", UNSET)

        patch_api_configs_admin_console_body_development_tenant_migration_notification = cls(
            is_paid_tenant=is_paid_tenant,
            tag=tag,
            read_at=read_at,
        )

        patch_api_configs_admin_console_body_development_tenant_migration_notification.additional_properties = d
        return patch_api_configs_admin_console_body_development_tenant_migration_notification

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
