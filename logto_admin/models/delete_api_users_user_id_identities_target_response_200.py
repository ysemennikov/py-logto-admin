from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_api_users_user_id_identities_target_response_200_custom_data import (
        DeleteApiUsersUserIdIdentitiesTargetResponse200CustomData,
    )
    from ..models.delete_api_users_user_id_identities_target_response_200_identities import (
        DeleteApiUsersUserIdIdentitiesTargetResponse200Identities,
    )
    from ..models.delete_api_users_user_id_identities_target_response_200_profile import (
        DeleteApiUsersUserIdIdentitiesTargetResponse200Profile,
    )
    from ..models.delete_api_users_user_id_identities_target_response_200_sso_identities_item import (
        DeleteApiUsersUserIdIdentitiesTargetResponse200SsoIdentitiesItem,
    )


T = TypeVar("T", bound="DeleteApiUsersUserIdIdentitiesTargetResponse200")


@_attrs_define
class DeleteApiUsersUserIdIdentitiesTargetResponse200:
    """
    Attributes:
        id (str):
        username (Union[None, str]):
        primary_email (Union[None, str]):
        primary_phone (Union[None, str]):
        name (Union[None, str]):
        avatar (Union[None, str]):
        custom_data (DeleteApiUsersUserIdIdentitiesTargetResponse200CustomData): arbitrary
        identities (DeleteApiUsersUserIdIdentitiesTargetResponse200Identities):
        last_sign_in_at (Union[None, float]):
        created_at (float):
        updated_at (float):
        profile (DeleteApiUsersUserIdIdentitiesTargetResponse200Profile):
        application_id (Union[None, str]):
        is_suspended (bool):
        has_password (Union[Unset, bool]):
        sso_identities (Union[Unset, List['DeleteApiUsersUserIdIdentitiesTargetResponse200SsoIdentitiesItem']]):
    """

    id: str
    username: Union[None, str]
    primary_email: Union[None, str]
    primary_phone: Union[None, str]
    name: Union[None, str]
    avatar: Union[None, str]
    custom_data: "DeleteApiUsersUserIdIdentitiesTargetResponse200CustomData"
    identities: "DeleteApiUsersUserIdIdentitiesTargetResponse200Identities"
    last_sign_in_at: Union[None, float]
    created_at: float
    updated_at: float
    profile: "DeleteApiUsersUserIdIdentitiesTargetResponse200Profile"
    application_id: Union[None, str]
    is_suspended: bool
    has_password: Union[Unset, bool] = UNSET
    sso_identities: Union[Unset, List["DeleteApiUsersUserIdIdentitiesTargetResponse200SsoIdentitiesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        username: Union[None, str]
        username = self.username

        primary_email: Union[None, str]
        primary_email = self.primary_email

        primary_phone: Union[None, str]
        primary_phone = self.primary_phone

        name: Union[None, str]
        name = self.name

        avatar: Union[None, str]
        avatar = self.avatar

        custom_data = self.custom_data.to_dict()

        identities = self.identities.to_dict()

        last_sign_in_at: Union[None, float]
        last_sign_in_at = self.last_sign_in_at

        created_at = self.created_at

        updated_at = self.updated_at

        profile = self.profile.to_dict()

        application_id: Union[None, str]
        application_id = self.application_id

        is_suspended = self.is_suspended

        has_password = self.has_password

        sso_identities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sso_identities, Unset):
            sso_identities = []
            for sso_identities_item_data in self.sso_identities:
                sso_identities_item = sso_identities_item_data.to_dict()
                sso_identities.append(sso_identities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "primaryEmail": primary_email,
                "primaryPhone": primary_phone,
                "name": name,
                "avatar": avatar,
                "customData": custom_data,
                "identities": identities,
                "lastSignInAt": last_sign_in_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "profile": profile,
                "applicationId": application_id,
                "isSuspended": is_suspended,
            }
        )
        if has_password is not UNSET:
            field_dict["hasPassword"] = has_password
        if sso_identities is not UNSET:
            field_dict["ssoIdentities"] = sso_identities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delete_api_users_user_id_identities_target_response_200_custom_data import (
            DeleteApiUsersUserIdIdentitiesTargetResponse200CustomData,
        )
        from ..models.delete_api_users_user_id_identities_target_response_200_identities import (
            DeleteApiUsersUserIdIdentitiesTargetResponse200Identities,
        )
        from ..models.delete_api_users_user_id_identities_target_response_200_profile import (
            DeleteApiUsersUserIdIdentitiesTargetResponse200Profile,
        )
        from ..models.delete_api_users_user_id_identities_target_response_200_sso_identities_item import (
            DeleteApiUsersUserIdIdentitiesTargetResponse200SsoIdentitiesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

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

        custom_data = DeleteApiUsersUserIdIdentitiesTargetResponse200CustomData.from_dict(d.pop("customData"))

        identities = DeleteApiUsersUserIdIdentitiesTargetResponse200Identities.from_dict(d.pop("identities"))

        def _parse_last_sign_in_at(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        last_sign_in_at = _parse_last_sign_in_at(d.pop("lastSignInAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        profile = DeleteApiUsersUserIdIdentitiesTargetResponse200Profile.from_dict(d.pop("profile"))

        def _parse_application_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        application_id = _parse_application_id(d.pop("applicationId"))

        is_suspended = d.pop("isSuspended")

        has_password = d.pop("hasPassword", UNSET)

        sso_identities = []
        _sso_identities = d.pop("ssoIdentities", UNSET)
        for sso_identities_item_data in _sso_identities or []:
            sso_identities_item = DeleteApiUsersUserIdIdentitiesTargetResponse200SsoIdentitiesItem.from_dict(
                sso_identities_item_data
            )

            sso_identities.append(sso_identities_item)

        delete_api_users_user_id_identities_target_response_200 = cls(
            id=id,
            username=username,
            primary_email=primary_email,
            primary_phone=primary_phone,
            name=name,
            avatar=avatar,
            custom_data=custom_data,
            identities=identities,
            last_sign_in_at=last_sign_in_at,
            created_at=created_at,
            updated_at=updated_at,
            profile=profile,
            application_id=application_id,
            is_suspended=is_suspended,
            has_password=has_password,
            sso_identities=sso_identities,
        )

        delete_api_users_user_id_identities_target_response_200.additional_properties = d
        return delete_api_users_user_id_identities_target_response_200

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
