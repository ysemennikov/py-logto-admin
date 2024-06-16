from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_configs_admin_console_response_200_checked_charge_notification import (
        GetApiConfigsAdminConsoleResponse200CheckedChargeNotification,
    )
    from ..models.get_api_configs_admin_console_response_200_development_tenant_migration_notification import (
        GetApiConfigsAdminConsoleResponse200DevelopmentTenantMigrationNotification,
    )


T = TypeVar("T", bound="GetApiConfigsAdminConsoleResponse200")


@_attrs_define
class GetApiConfigsAdminConsoleResponse200:
    """
    Attributes:
        sign_in_experience_customized (bool):
        organization_created (bool):
        development_tenant_migration_notification (Union[Unset,
            GetApiConfigsAdminConsoleResponse200DevelopmentTenantMigrationNotification]):
        checked_charge_notification (Union[Unset, GetApiConfigsAdminConsoleResponse200CheckedChargeNotification]):
    """

    sign_in_experience_customized: bool
    organization_created: bool
    development_tenant_migration_notification: Union[
        Unset, "GetApiConfigsAdminConsoleResponse200DevelopmentTenantMigrationNotification"
    ] = UNSET
    checked_charge_notification: Union[Unset, "GetApiConfigsAdminConsoleResponse200CheckedChargeNotification"] = UNSET
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
        field_dict.update(
            {
                "signInExperienceCustomized": sign_in_experience_customized,
                "organizationCreated": organization_created,
            }
        )
        if development_tenant_migration_notification is not UNSET:
            field_dict["developmentTenantMigrationNotification"] = development_tenant_migration_notification
        if checked_charge_notification is not UNSET:
            field_dict["checkedChargeNotification"] = checked_charge_notification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_configs_admin_console_response_200_checked_charge_notification import (
            GetApiConfigsAdminConsoleResponse200CheckedChargeNotification,
        )
        from ..models.get_api_configs_admin_console_response_200_development_tenant_migration_notification import (
            GetApiConfigsAdminConsoleResponse200DevelopmentTenantMigrationNotification,
        )

        d = src_dict.copy()
        sign_in_experience_customized = d.pop("signInExperienceCustomized")

        organization_created = d.pop("organizationCreated")

        _development_tenant_migration_notification = d.pop("developmentTenantMigrationNotification", UNSET)
        development_tenant_migration_notification: Union[
            Unset, GetApiConfigsAdminConsoleResponse200DevelopmentTenantMigrationNotification
        ]
        if isinstance(_development_tenant_migration_notification, Unset):
            development_tenant_migration_notification = UNSET
        else:
            development_tenant_migration_notification = (
                GetApiConfigsAdminConsoleResponse200DevelopmentTenantMigrationNotification.from_dict(
                    _development_tenant_migration_notification
                )
            )

        _checked_charge_notification = d.pop("checkedChargeNotification", UNSET)
        checked_charge_notification: Union[Unset, GetApiConfigsAdminConsoleResponse200CheckedChargeNotification]
        if isinstance(_checked_charge_notification, Unset):
            checked_charge_notification = UNSET
        else:
            checked_charge_notification = GetApiConfigsAdminConsoleResponse200CheckedChargeNotification.from_dict(
                _checked_charge_notification
            )

        get_api_configs_admin_console_response_200 = cls(
            sign_in_experience_customized=sign_in_experience_customized,
            organization_created=organization_created,
            development_tenant_migration_notification=development_tenant_migration_notification,
            checked_charge_notification=checked_charge_notification,
        )

        get_api_configs_admin_console_response_200.additional_properties = d
        return get_api_configs_admin_console_response_200

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
