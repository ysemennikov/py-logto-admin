from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item_status import (
    GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemStatus,
)

if TYPE_CHECKING:
    from ..models.get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0 import (
        GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0,
    )
    from ..models.get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item_dns_records_item import (
        GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemDnsRecordsItem,
    )


T = TypeVar("T", bound="GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItem")


@_attrs_define
class GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItem:
    """
    Attributes:
        domain (str):
        status (GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemStatus):
        error_message (Union[None, str]):
        dns_records (List['GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemDnsRecordsItem']):
        cloudflare_data
            (Union['GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0', None]):
    """

    domain: str
    status: GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemStatus
    error_message: Union[None, str]
    dns_records: List["GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemDnsRecordsItem"]
    cloudflare_data: Union[
        "GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0", None
    ]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0 import (
            GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0,
        )

        domain = self.domain

        status = self.status.value

        error_message: Union[None, str]
        error_message = self.error_message

        dns_records = []
        for dns_records_item_data in self.dns_records:
            dns_records_item = dns_records_item_data.to_dict()
            dns_records.append(dns_records_item)

        cloudflare_data: Union[Dict[str, Any], None]
        if isinstance(
            self.cloudflare_data,
            GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0,
        ):
            cloudflare_data = self.cloudflare_data.to_dict()
        else:
            cloudflare_data = self.cloudflare_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "status": status,
                "errorMessage": error_message,
                "dnsRecords": dns_records,
                "cloudflareData": cloudflare_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item_cloudflare_data_type_0 import (
            GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0,
        )
        from ..models.get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item_dns_records_item import (
            GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemDnsRecordsItem,
        )

        d = src_dict.copy()
        domain = d.pop("domain")

        status = GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemStatus(d.pop("status"))

        def _parse_error_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error_message = _parse_error_message(d.pop("errorMessage"))

        dns_records = []
        _dns_records = d.pop("dnsRecords")
        for dns_records_item_data in _dns_records:
            dns_records_item = (
                GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemDnsRecordsItem.from_dict(
                    dns_records_item_data
                )
            )

            dns_records.append(dns_records_item)

        def _parse_cloudflare_data(
            data: object,
        ) -> Union[
            "GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0", None
        ]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cloudflare_data_type_0 = GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0.from_dict(
                    data
                )

                return cloudflare_data_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "GetApiApplicationsIdResponse200ProtectedAppMetadataType0CustomDomainsItemCloudflareDataType0", None
                ],
                data,
            )

        cloudflare_data = _parse_cloudflare_data(d.pop("cloudflareData"))

        get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item = cls(
            domain=domain,
            status=status,
            error_message=error_message,
            dns_records=dns_records,
            cloudflare_data=cloudflare_data,
        )

        get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item.additional_properties = d
        return get_api_applications_id_response_200_protected_app_metadata_type_0_custom_domains_item

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
