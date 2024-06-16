from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiUsersUserIdMfaVerificationsBody")


@_attrs_define
class PostApiUsersUserIdMfaVerificationsBody:
    """
    Attributes:
        type (str): The type of MFA verification to create.
    """

    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_type(data: object) -> str:
            return cast(str, data)

        type = _parse_type(d.pop("type"))

        post_api_users_user_id_mfa_verifications_body = cls(
            type=type,
        )

        post_api_users_user_id_mfa_verifications_body.additional_properties = d
        return post_api_users_user_id_mfa_verifications_body

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
