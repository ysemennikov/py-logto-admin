from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_domains_id_response_200_status import GetApiDomainsIdResponse200Status

if TYPE_CHECKING:
    from ..models.get_api_domains_id_response_200_dns_records_item import GetApiDomainsIdResponse200DnsRecordsItem


T = TypeVar("T", bound="GetApiDomainsIdResponse200")


@_attrs_define
class GetApiDomainsIdResponse200:
    """
    Attributes:
        id (str):
        domain (str):
        status (GetApiDomainsIdResponse200Status):
        error_message (Union[None, str]):
        dns_records (List['GetApiDomainsIdResponse200DnsRecordsItem']):
    """

    id: str
    domain: str
    status: GetApiDomainsIdResponse200Status
    error_message: Union[None, str]
    dns_records: List["GetApiDomainsIdResponse200DnsRecordsItem"]
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
        from ..models.get_api_domains_id_response_200_dns_records_item import GetApiDomainsIdResponse200DnsRecordsItem

        d = src_dict.copy()
        id = d.pop("id")

        domain = d.pop("domain")

        status = GetApiDomainsIdResponse200Status(d.pop("status"))

        def _parse_error_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error_message = _parse_error_message(d.pop("errorMessage"))

        dns_records = []
        _dns_records = d.pop("dnsRecords")
        for dns_records_item_data in _dns_records:
            dns_records_item = GetApiDomainsIdResponse200DnsRecordsItem.from_dict(dns_records_item_data)

            dns_records.append(dns_records_item)

        get_api_domains_id_response_200 = cls(
            id=id,
            domain=domain,
            status=status,
            error_message=error_message,
            dns_records=dns_records,
        )

        get_api_domains_id_response_200.additional_properties = d
        return get_api_domains_id_response_200

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
