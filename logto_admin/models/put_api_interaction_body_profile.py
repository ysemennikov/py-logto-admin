from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiInteractionBodyProfile")


@_attrs_define
class PutApiInteractionBodyProfile:
    """
    Attributes:
        username (Union[Unset, str]):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        connector_id (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    connector_id: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        email = self.email

        phone = self.phone

        connector_id = self.connector_id

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        password = d.pop("password", UNSET)

        put_api_interaction_body_profile = cls(
            username=username,
            email=email,
            phone=phone,
            connector_id=connector_id,
            password=password,
        )

        put_api_interaction_body_profile.additional_properties = d
        return put_api_interaction_body_profile

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
