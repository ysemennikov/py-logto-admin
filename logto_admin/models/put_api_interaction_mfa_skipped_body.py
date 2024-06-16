from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiInteractionMfaSkippedBody")


@_attrs_define
class PutApiInteractionMfaSkippedBody:
    """
    Attributes:
        mfa_skipped (bool):
    """

    mfa_skipped: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mfa_skipped = self.mfa_skipped

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mfaSkipped": mfa_skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mfa_skipped = d.pop("mfaSkipped")

        put_api_interaction_mfa_skipped_body = cls(
            mfa_skipped=mfa_skipped,
        )

        put_api_interaction_mfa_skipped_body.additional_properties = d
        return put_api_interaction_mfa_skipped_body

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
