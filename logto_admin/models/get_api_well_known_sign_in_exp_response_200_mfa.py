from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_well_known_sign_in_exp_response_200_mfa_factors_item import (
    GetApiWellKnownSignInExpResponse200MfaFactorsItem,
)
from ..models.get_api_well_known_sign_in_exp_response_200_mfa_policy import GetApiWellKnownSignInExpResponse200MfaPolicy

T = TypeVar("T", bound="GetApiWellKnownSignInExpResponse200Mfa")


@_attrs_define
class GetApiWellKnownSignInExpResponse200Mfa:
    """
    Attributes:
        factors (List[GetApiWellKnownSignInExpResponse200MfaFactorsItem]):
        policy (GetApiWellKnownSignInExpResponse200MfaPolicy):
    """

    factors: List[GetApiWellKnownSignInExpResponse200MfaFactorsItem]
    policy: GetApiWellKnownSignInExpResponse200MfaPolicy
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        factors = []
        for factors_item_data in self.factors:
            factors_item = factors_item_data.value
            factors.append(factors_item)

        policy = self.policy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "factors": factors,
                "policy": policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        factors = []
        _factors = d.pop("factors")
        for factors_item_data in _factors:
            factors_item = GetApiWellKnownSignInExpResponse200MfaFactorsItem(factors_item_data)

            factors.append(factors_item)

        policy = GetApiWellKnownSignInExpResponse200MfaPolicy(d.pop("policy"))

        get_api_well_known_sign_in_exp_response_200_mfa = cls(
            factors=factors,
            policy=policy,
        )

        get_api_well_known_sign_in_exp_response_200_mfa.additional_properties = d
        return get_api_well_known_sign_in_exp_response_200_mfa

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
