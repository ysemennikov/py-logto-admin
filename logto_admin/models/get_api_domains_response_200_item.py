from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_domains_response_200_item_status import GetApiDomainsResponse200ItemStatus

if TYPE_CHECKING:
    from ..models.get_api_domains_response_200_item_dns_records_item import GetApiDomainsResponse200ItemDnsRecordsItem


T = TypeVar("T", bound="GetApiDomainsResponse200Item")


@_attrs_define
class GetApiDomainsResponse200Item:
    """
    Attributes:
        id (str):
        domain (str):
        status (GetApiDomainsResponse200ItemStatus):
        error_message (Union[None, str]):
        dns_records (List['GetApiDomainsResponse200ItemDnsRecordsItem']):
    """

    id: str
    domain: str
    status: GetApiDomainsResponse200ItemStatus
    error_message: Union[None, str]
    dns_records: List["GetApiDomainsResponse200ItemDnsRecordsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        domain = self.domain

        status = self.status.value

        error_message: Union[None, str]
        error_message = self.error_message

        dns_records = []
        for dns_records_item_data in self.dns_records:
            dns_records_item = dns_records_item_data.to_dict()
            dns_records.append(dns_records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "domain": domain,
                "status": status,
                "errorMessage": error_message,
                "dnsRecords": dns_records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_domains_response_200_item_dns_records_item import (
            GetApiDomainsResponse200ItemDnsRecordsItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        domain = d.pop("domain")

        status = GetApiDomainsResponse200ItemStatus(d.pop("status"))

        def _parse_error_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error_message = _parse_error_message(d.pop("errorMessage"))

        dns_records = []
        _dns_records = d.pop("dnsRecords")
        for dns_records_item_data in _dns_records:
            dns_records_item = GetApiDomainsResponse200ItemDnsRecordsItem.from_dict(dns_records_item_data)

            dns_records.append(dns_records_item)

        get_api_domains_response_200_item = cls(
            id=id,
            domain=domain,
            status=status,
            error_message=error_message,
            dns_records=dns_records,
        )

        get_api_domains_response_200_item.additional_properties = d
        return get_api_domains_response_200_item

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
