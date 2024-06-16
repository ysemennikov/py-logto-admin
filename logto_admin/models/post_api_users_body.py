from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_users_body_password_algorithm import PostApiUsersBodyPasswordAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_users_body_custom_data import PostApiUsersBodyCustomData
    from ..models.post_api_users_body_profile import PostApiUsersBodyProfile


T = TypeVar("T", bound="PostApiUsersBody")


@_attrs_define
class PostApiUsersBody:
    """User data to create a new user. All properties are optional.

    Attributes:
        primary_phone (Union[Unset, str]): Primary phone number for the user. It should be unique across all users.
        primary_email (Union[Unset, str]): Primary email address for the user. It should be unique across all users.
        username (Union[Unset, str]): Username for the user. It should be unique across all users.
        password (Union[Unset, str]): Plain text password for the user.
        password_digest (Union[Unset, str]): In case you already have the password digests and not the passwords, you
            can use them for the newly created user via this property. The value should be generated with one of the
            supported algorithms. The algorithm can be specified using the `passwordAlgorithm` property.
        password_algorithm (Union[Unset, PostApiUsersBodyPasswordAlgorithm]): The hash algorithm used for the password.
            It should be one of the supported algorithms: argon2, md5, sha1, sha256. Should the encryption algorithm differ
            from argon2, it will automatically be upgraded to argon2 upon the user's next sign-in.
        name (Union[Unset, str]):
        avatar (Union[None, Unset, str]):
        custom_data (Union[Unset, PostApiUsersBodyCustomData]): arbitrary
        profile (Union[Unset, PostApiUsersBodyProfile]):
    """

    primary_phone: Union[Unset, str] = UNSET
    primary_email: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    password_digest: Union[Unset, str] = UNSET
    password_algorithm: Union[Unset, PostApiUsersBodyPasswordAlgorithm] = UNSET
    name: Union[Unset, str] = UNSET
    avatar: Union[None, Unset, str] = UNSET
    custom_data: Union[Unset, "PostApiUsersBodyCustomData"] = UNSET
    profile: Union[Unset, "PostApiUsersBodyProfile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary_phone = self.primary_phone

        primary_email = self.primary_email

        username = self.username

        password = self.password

        password_digest = self.password_digest

        password_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.password_algorithm, Unset):
            password_algorithm = self.password_algorithm.value

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
        if primary_phone is not UNSET:
            field_dict["primaryPhone"] = primary_phone
        if primary_email is not UNSET:
            field_dict["primaryEmail"] = primary_email
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if password_digest is not UNSET:
            field_dict["passwordDigest"] = password_digest
        if password_algorithm is not UNSET:
            field_dict["passwordAlgorithm"] = password_algorithm
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
        from ..models.post_api_users_body_custom_data import PostApiUsersBodyCustomData
        from ..models.post_api_users_body_profile import PostApiUsersBodyProfile

        d = src_dict.copy()
        primary_phone = d.pop("primaryPhone", UNSET)

        primary_email = d.pop("primaryEmail", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        password_digest = d.pop("passwordDigest", UNSET)

        _password_algorithm = d.pop("passwordAlgorithm", UNSET)
        password_algorithm: Union[Unset, PostApiUsersBodyPasswordAlgorithm]
        if isinstance(_password_algorithm, Unset):
            password_algorithm = UNSET
        else:
            password_algorithm = PostApiUsersBodyPasswordAlgorithm(_password_algorithm)

        name = d.pop("name", UNSET)

        def _parse_avatar(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        _custom_data = d.pop("customData", UNSET)
        custom_data: Union[Unset, PostApiUsersBodyCustomData]
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = PostApiUsersBodyCustomData.from_dict(_custom_data)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, PostApiUsersBodyProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = PostApiUsersBodyProfile.from_dict(_profile)

        post_api_users_body = cls(
            primary_phone=primary_phone,
            primary_email=primary_email,
            username=username,
            password=password,
            password_digest=password_digest,
            password_algorithm=password_algorithm,
            name=name,
            avatar=avatar,
            custom_data=custom_data,
            profile=profile,
        )

        post_api_users_body.additional_properties = d
        return post_api_users_body

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
