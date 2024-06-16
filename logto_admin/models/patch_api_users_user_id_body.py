from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_users_user_id_body_custom_data import PatchApiUsersUserIdBodyCustomData
    from ..models.patch_api_users_user_id_body_profile import PatchApiUsersUserIdBodyProfile


T = TypeVar("T", bound="PatchApiUsersUserIdBody")


@_attrs_define
class PatchApiUsersUserIdBody:
    """
    Attributes:
        username (Union[None, Unset, str]): Updated username for the user. It should be unique across all users.
        primary_email (Union[None, Unset, str]): Updated primary email address for the user. It should be unique across
            all users.
        primary_phone (Union[None, Unset, str]): Updated primary phone number for the user. It should be unique across
            all users.
        name (Union[None, Unset, str]):
        avatar (Union[None, Unset, str]):
        custom_data (Union[Unset, PatchApiUsersUserIdBodyCustomData]): Custom data object to update for the given user
            ID. Note this will replace the entire custom data object.

            If you want to perform a partial update, use the `PATCH /api/users/{userId}/custom-data` endpoint instead.
        profile (Union[Unset, PatchApiUsersUserIdBodyProfile]):
    """

    username: Union[None, Unset, str] = UNSET
    primary_email: Union[None, Unset, str] = UNSET
    primary_phone: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    avatar: Union[None, Unset, str] = UNSET
    custom_data: Union[Unset, "PatchApiUsersUserIdBodyCustomData"] = UNSET
    profile: Union[Unset, "PatchApiUsersUserIdBodyProfile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        primary_email: Union[None, Unset, str]
        if isinstance(self.primary_email, Unset):
            primary_email = UNSET
        else:
            primary_email = self.primary_email

        primary_phone: Union[None, Unset, str]
        if isinstance(self.primary_phone, Unset):
            primary_phone = UNSET
        else:
            primary_phone = self.primary_phone

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        avatar: Union[None, Unset, str]
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        custom_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_data, Unset):
            custom_data = self.custom_data.to_dict()

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if primary_email is not UNSET:
            field_dict["primaryEmail"] = primary_email
        if primary_phone is not UNSET:
            field_dict["primaryPhone"] = primary_phone
        if name is not UNSET:
            field_dict["name"] = name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_users_user_id_body_custom_data import PatchApiUsersUserIdBodyCustomData
        from ..models.patch_api_users_user_id_body_profile import PatchApiUsersUserIdBodyProfile

        d = src_dict.copy()

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_primary_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_email = _parse_primary_email(d.pop("primaryEmail", UNSET))

        def _parse_primary_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_phone = _parse_primary_phone(d.pop("primaryPhone", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_avatar(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        _custom_data = d.pop("customData", UNSET)
        custom_data: Union[Unset, PatchApiUsersUserIdBodyCustomData]
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = PatchApiUsersUserIdBodyCustomData.from_dict(_custom_data)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, PatchApiUsersUserIdBodyProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = PatchApiUsersUserIdBodyProfile.from_dict(_profile)

        patch_api_users_user_id_body = cls(
            username=username,
            primary_email=primary_email,
            primary_phone=primary_phone,
            name=name,
            avatar=avatar,
            custom_data=custom_data,
            profile=profile,
        )

        patch_api_users_user_id_body.additional_properties = d
        return patch_api_users_user_id_body

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
