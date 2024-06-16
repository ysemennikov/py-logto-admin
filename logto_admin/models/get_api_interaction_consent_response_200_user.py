from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiInteractionConsentResponse200User")


@_attrs_define
class GetApiInteractionConsentResponse200User:
    """
    Attributes:
        id (str):
        name (Union[None, str]):
        avatar (Union[None, str]):
        username (Union[None, str]):
        primary_email (Union[None, str]):
        primary_phone (Union[None, str]):
    """

    id: str
    name: Union[None, str]
    avatar: Union[None, str]
    username: Union[None, str]
    primary_email: Union[None, str]
    primary_phone: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name: Union[None, str]
        name = self.name

        avatar: Union[None, str]
        avatar = self.avatar

        username: Union[None, str]
        username = self.username

        primary_email: Union[None, str]
        primary_email = self.primary_email

        primary_phone: Union[None, str]
        primary_phone = self.primary_phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "avatar": avatar,
                "username": username,
                "primaryEmail": primary_email,
                "primaryPhone": primary_phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        def _parse_avatar(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        avatar = _parse_avatar(d.pop("avatar"))

        def _parse_username(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        username = _parse_username(d.pop("username"))

        def _parse_primary_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        primary_email = _parse_primary_email(d.pop("primaryEmail"))

        def _parse_primary_phone(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        primary_phone = _parse_primary_phone(d.pop("primaryPhone"))

        get_api_interaction_consent_response_200_user = cls(
            id=id,
            name=name,
            avatar=avatar,
            username=username,
            primary_email=primary_email,
            primary_phone=primary_phone,
        )

        get_api_interaction_consent_response_200_user.additional_properties = d
        return get_api_interaction_consent_response_200_user

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
