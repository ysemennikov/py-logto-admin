from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item import (
        GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItem,
    )
    from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_page_rules_item import (
        GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0PageRulesItem,
    )


T = TypeVar("T", bound="GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0")


@_attrs_define
class GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0:
    """
    Attributes:
        host (str):
        origin (str):
        session_duration (float):
        page_rules (List['GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0PageRulesItem']):
        custom_domains (Union[Unset,
            List['GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItem']]):
    """

    host: str
    origin: str
    session_duration: float
    page_rules: List["GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0PageRulesItem"]
    custom_domains: Union[
        Unset, List["GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        origin = self.origin

        session_duration = self.session_duration

        page_rules = []
        for page_rules_item_data in self.page_rules:
            page_rules_item = page_rules_item_data.to_dict()
            page_rules.append(page_rules_item)

        custom_domains: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_domains, Unset):
            custom_domains = []
            for custom_domains_item_data in self.custom_domains:
                custom_domains_item = custom_domains_item_data.to_dict()
                custom_domains.append(custom_domains_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "origin": origin,
                "sessionDuration": session_duration,
                "pageRules": page_rules,
            }
        )
        if custom_domains is not UNSET:
            field_dict["customDomains"] = custom_domains

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_custom_domains_item import (
            GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItem,
        )
        from ..models.get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0_page_rules_item import (
            GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0PageRulesItem,
        )

        d = src_dict.copy()
        host = d.pop("host")

        origin = d.pop("origin")

        session_duration = d.pop("sessionDuration")

        page_rules = []
        _page_rules = d.pop("pageRules")
        for page_rules_item_data in _page_rules:
            page_rules_item = GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0PageRulesItem.from_dict(
                page_rules_item_data
            )

            page_rules.append(page_rules_item)

        custom_domains = []
        _custom_domains = d.pop("customDomains", UNSET)
        for custom_domains_item_data in _custom_domains or []:
            custom_domains_item = (
                GetApiRolesIdApplicationsResponse200ItemProtectedAppMetadataType0CustomDomainsItem.from_dict(
                    custom_domains_item_data
                )
            )

            custom_domains.append(custom_domains_item)

        get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0 = cls(
            host=host,
            origin=origin,
            session_duration=session_duration,
            page_rules=page_rules,
            custom_domains=custom_domains,
        )

        get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0.additional_properties = d
        return get_api_roles_id_applications_response_200_item_protected_app_metadata_type_0

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
