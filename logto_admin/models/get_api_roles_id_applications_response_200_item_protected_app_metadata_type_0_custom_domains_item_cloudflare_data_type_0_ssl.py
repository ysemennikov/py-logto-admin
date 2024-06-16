from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl_validation_errors_item import (
        GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0SslValidationErrorsItem,
    )


T = TypeVar(
    "T",
    bound="GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl",
)


@_attrs_define
class GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl:
    """
    Attributes:
        status (str):
        validation_errors (Union[Unset, List['GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDom
            ainsItemCloudflareDataType0SslValidationErrorsItem']]):
    """

    status: str
    validation_errors: Union[
        Unset,
        List[
            "GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0SslValidationErrorsItem"
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        validation_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = []
            for validation_errors_item_data in self.validation_errors:
                validation_errors_item = validation_errors_item_data.to_dict()
                validation_errors.append(validation_errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if validation_errors is not UNSET:
            field_dict["validation_errors"] = validation_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl_validation_errors_item import (
            GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0SslValidationErrorsItem,
        )

        d = src_dict.copy()
        status = d.pop("status")

        validation_errors = []
        _validation_errors = d.pop("validation_errors", UNSET)
        for validation_errors_item_data in _validation_errors or []:
            validation_errors_item = GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0SslValidationErrorsItem.from_dict(
                validation_errors_item_data
            )

            validation_errors.append(validation_errors_item)

        get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl = cls(
            status=status,
            validation_errors=validation_errors,
        )

        get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl.additional_properties = d
        return get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl

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
