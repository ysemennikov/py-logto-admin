from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_interaction_mfa_body_type_1_client_extension_results_crep_props import (
        PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps,
    )


T = TypeVar("T", bound="PutApiInteractionMfaBodyType1ClientExtensionResults")


@_attrs_define
class PutApiInteractionMfaBodyType1ClientExtensionResults:
    """
    Attributes:
        appid (Union[Unset, bool]):
        crep_props (Union[Unset, PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps]):
        hmac_create_secret (Union[Unset, bool]):
    """

    appid: Union[Unset, bool] = UNSET
    crep_props: Union[Unset, "PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps"] = UNSET
    hmac_create_secret: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appid = self.appid

        crep_props: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crep_props, Unset):
            crep_props = self.crep_props.to_dict()

        hmac_create_secret = self.hmac_create_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appid is not UNSET:
            field_dict["appid"] = appid
        if crep_props is not UNSET:
            field_dict["crepProps"] = crep_props
        if hmac_create_secret is not UNSET:
            field_dict["hmacCreateSecret"] = hmac_create_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_interaction_mfa_body_type_1_client_extension_results_crep_props import (
            PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps,
        )

        d = src_dict.copy()
        appid = d.pop("appid", UNSET)

        _crep_props = d.pop("crepProps", UNSET)
        crep_props: Union[Unset, PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps]
        if isinstance(_crep_props, Unset):
            crep_props = UNSET
        else:
            crep_props = PutApiInteractionMfaBodyType1ClientExtensionResultsCrepProps.from_dict(_crep_props)

        hmac_create_secret = d.pop("hmacCreateSecret", UNSET)

        put_api_interaction_mfa_body_type_1_client_extension_results = cls(
            appid=appid,
            crep_props=crep_props,
            hmac_create_secret=hmac_create_secret,
        )

        put_api_interaction_mfa_body_type_1_client_extension_results.additional_properties = d
        return put_api_interaction_mfa_body_type_1_client_extension_results

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
