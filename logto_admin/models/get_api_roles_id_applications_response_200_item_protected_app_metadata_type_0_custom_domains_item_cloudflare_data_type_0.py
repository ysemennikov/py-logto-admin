from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl import (
        GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl,
    )


T = TypeVar(
    "T", bound="GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0"
)


@_attrs_define
class GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0:
    """
    Attributes:
        id (str):
        status (str):
        ssl (GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl):
        verification_errors (Union[Unset, List[str]]):
    """

    id: str
    status: str
    ssl: "GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl"
    verification_errors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status = self.status

        ssl = self.ssl.to_dict()

        verification_errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.verification_errors, Unset):
            verification_errors = self.verification_errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "ssl": ssl,
            }
        )
        if verification_errors is not UNSET:
            field_dict["verification_errors"] = verification_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0_ssl import (
            GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl,
        )

        d = src_dict.copy()
        id = d.pop("id")

        status = d.pop("status")

        ssl = GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0Ssl.from_dict(
            d.pop("ssl")
        )

        verification_errors = cast(List[str], d.pop("verification_errors", UNSET))

        get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0 = cls(
            id=id,
            status=status,
            ssl=ssl,
            verification_errors=verification_errors,
        )

        get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0.additional_properties = d
        return get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0

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
