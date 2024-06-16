from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiUsersUserIdMfaVerificationsResponse200Type1")


@_attrs_define
class PostApiUsersUserIdMfaVerificationsResponse200Type1:
    """
    Attributes:
        type (str):
        codes (List[str]):
    """

    type: str
    codes: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        codes = self.codes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "codes": codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        codes = cast(List[str], d.pop("codes"))

        post_api_users_user_id_mfa_verifications_response_200_type_1 = cls(
            type=type,
            codes=codes,
        )

        post_api_users_user_id_mfa_verifications_response_200_type_1.additional_properties = d
        return post_api_users_user_id_mfa_verifications_response_200_type_1

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
