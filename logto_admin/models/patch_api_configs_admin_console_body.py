from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_configs_admin_console_body_checked_charge_notification import (
        PatchApiConfigsAdminConsoleBodyCheckedChargeNotification,
    )
    from ..models.patch_api_configs_admin_console_body_development_tenant_migration_notification import (
        PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification,
    )


T = TypeVar("T", bound="PatchApiConfigsAdminConsoleBody")


@_attrs_define
class PatchApiConfigsAdminConsoleBody:
    """
    Attributes:
        sign_in_experience_customized (Union[Unset, bool]):
        organization_created (Union[Unset, bool]):
        development_tenant_migration_notification (Union[Unset,
            PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification]):
        checked_charge_notification (Union[Unset, PatchApiConfigsAdminConsoleBodyCheckedChargeNotification]):
    """

    sign_in_experience_customized: Union[Unset, bool] = UNSET
    organization_created: Union[Unset, bool] = UNSET
    development_tenant_migration_notification: Union[
        Unset, "PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification"
    ] = UNSET
    checked_charge_notification: Union[Unset, "PatchApiConfigsAdminConsoleBodyCheckedChargeNotification"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sign_in_experience_customized = self.sign_in_experience_customized

        organization_created = self.organization_created

        development_tenant_migration_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.development_tenant_migration_notification, Unset):
            development_tenant_migration_notification = self.development_tenant_migration_notification.to_dict()

        checked_charge_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checked_charge_notification, Unset):
            checked_charge_notification = self.checked_charge_notification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sign_in_experience_customized is not UNSET:
            field_dict["signInExperienceCustomized"] = sign_in_experience_customized
        if organization_created is not UNSET:
            field_dict["organizationCreated"] = organization_created
        if development_tenant_migration_notification is not UNSET:
            field_dict["developmentTenantMigrationNotification"] = development_tenant_migration_notification
        if checked_charge_notification is not UNSET:
            field_dict["checkedChargeNotification"] = checked_charge_notification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_configs_admin_console_body_checked_charge_notification import (
            PatchApiConfigsAdminConsoleBodyCheckedChargeNotification,
        )
        from ..models.patch_api_configs_admin_console_body_development_tenant_migration_notification import (
            PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification,
        )

        d = src_dict.copy()
        sign_in_experience_customized = d.pop("signInExperienceCustomized", UNSET)

        organization_created = d.pop("organizationCreated", UNSET)

        _development_tenant_migration_notification = d.pop("developmentTenantMigrationNotification", UNSET)
        development_tenant_migration_notification: Union[
            Unset, PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification
        ]
        if isinstance(_development_tenant_migration_notification, Unset):
            development_tenant_migration_notification = UNSET
        else:
            development_tenant_migration_notification = (
                PatchApiConfigsAdminConsoleBodyDevelopmentTenantMigrationNotification.from_dict(
                    _development_tenant_migration_notification
                )
            )

        _checked_charge_notification = d.pop("checkedChargeNotification", UNSET)
        checked_charge_notification: Union[Unset, PatchApiConfigsAdminConsoleBodyCheckedChargeNotification]
        if isinstance(_checked_charge_notification, Unset):
            checked_charge_notification = UNSET
        else:
            checked_charge_notification = PatchApiConfigsAdminConsoleBodyCheckedChargeNotification.from_dict(
                _checked_charge_notification
            )

        patch_api_configs_admin_console_body = cls(
            sign_in_experience_customized=sign_in_experience_customized,
            organization_created=organization_created,
            development_tenant_migration_notification=development_tenant_migration_notification,
            checked_charge_notification=checked_charge_notification,
        )

        patch_api_configs_admin_console_body.additional_properties = d
        return patch_api_configs_admin_console_body

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
