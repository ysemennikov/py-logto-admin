from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_users_user_id_profile_response_200_address import (
        PatchApiUsersUserIdProfileResponse200Address,
    )


T = TypeVar("T", bound="PatchApiUsersUserIdProfileResponse200")


@_attrs_define
class PatchApiUsersUserIdProfileResponse200:
    """
    Attributes:
        family_name (Union[Unset, str]):
        given_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        nickname (Union[Unset, str]):
        preferred_username (Union[Unset, str]):
        profile (Union[Unset, str]):
        website (Union[Unset, str]):
        gender (Union[Unset, str]):
        birthdate (Union[Unset, str]):
        zoneinfo (Union[Unset, str]):
        locale (Union[Unset, str]):
        address (Union[Unset, PatchApiUsersUserIdProfileResponse200Address]):
    """

    family_name: Union[Unset, str] = UNSET
    given_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    preferred_username: Union[Unset, str] = UNSET
    profile: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    birthdate: Union[Unset, str] = UNSET
    zoneinfo: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    address: Union[Unset, "PatchApiUsersUserIdProfileResponse200Address"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        family_name = self.family_name

        given_name = self.given_name

        middle_name = self.middle_name

        nickname = self.nickname

        preferred_username = self.preferred_username

        profile = self.profile

        website = self.website

        gender = self.gender

        birthdate = self.birthdate

        zoneinfo = self.zoneinfo

        locale = self.locale

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if preferred_username is not UNSET:
            field_dict["preferredUsername"] = preferred_username
        if profile is not UNSET:
            field_dict["profile"] = profile
        if website is not UNSET:
            field_dict["website"] = website
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if zoneinfo is not UNSET:
            field_dict["zoneinfo"] = zoneinfo
        if locale is not UNSET:
            field_dict["locale"] = locale
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_users_user_id_profile_response_200_address import (
            PatchApiUsersUserIdProfileResponse200Address,
        )

        d = src_dict.copy()
        family_name = d.pop("familyName", UNSET)

        given_name = d.pop("givenName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        nickname = d.pop("nickname", UNSET)

        preferred_username = d.pop("preferredUsername", UNSET)

        profile = d.pop("profile", UNSET)

        website = d.pop("website", UNSET)

        gender = d.pop("gender", UNSET)

        birthdate = d.pop("birthdate", UNSET)

        zoneinfo = d.pop("zoneinfo", UNSET)

        locale = d.pop("locale", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, PatchApiUsersUserIdProfileResponse200Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PatchApiUsersUserIdProfileResponse200Address.from_dict(_address)

        patch_api_users_user_id_profile_response_200 = cls(
            family_name=family_name,
            given_name=given_name,
            middle_name=middle_name,
            nickname=nickname,
            preferred_username=preferred_username,
            profile=profile,
            website=website,
            gender=gender,
            birthdate=birthdate,
            zoneinfo=zoneinfo,
            locale=locale,
            address=address,
        )

        patch_api_users_user_id_profile_response_200.additional_properties = d
        return patch_api_users_user_id_profile_response_200

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
