from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_mfa_verification_factors_item import (
    GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserMfaVerificationFactorsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_custom_data import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserCustomData,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_identities import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserIdentities,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_organization_roles_item import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationRolesItem,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_organizations_item import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationsItem,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_profile import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserProfile,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_roles_item import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItem,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem,
    )


T = TypeVar("T", bound="GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUser")


@_attrs_define
class GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUser:
    """
    Attributes:
        id (Union[Unset, str]):
        username (Union[None, Unset, str]):
        primary_email (Union[None, Unset, str]):
        primary_phone (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        avatar (Union[None, Unset, str]):
        custom_data (Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserCustomData]):
            arbitrary
        identities (Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserIdentities]):
        last_sign_in_at (Union[None, Unset, float]):
        created_at (Union[Unset, float]):
        updated_at (Union[Unset, float]):
        profile (Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserProfile]):
        application_id (Union[None, Unset, str]):
        is_suspended (Union[Unset, bool]):
        sso_identities (Union[Unset,
            List['GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem']]):
        mfa_verification_factors (Union[Unset,
            List[GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserMfaVerificationFactorsItem]]):
        roles (Union[Unset, List['GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItem']]):
        organizations (Union[Unset,
            List['GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationsItem']]):
        organization_roles (Union[Unset,
            List['GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationRolesItem']]):
    """

    id: Union[Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    primary_email: Union[None, Unset, str] = UNSET
    primary_phone: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    avatar: Union[None, Unset, str] = UNSET
    custom_data: Union[Unset, "GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserCustomData"] = UNSET
    identities: Union[Unset, "GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserIdentities"] = UNSET
    last_sign_in_at: Union[None, Unset, float] = UNSET
    created_at: Union[Unset, float] = UNSET
    updated_at: Union[Unset, float] = UNSET
    profile: Union[Unset, "GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserProfile"] = UNSET
    application_id: Union[None, Unset, str] = UNSET
    is_suspended: Union[Unset, bool] = UNSET
    sso_identities: Union[
        Unset, List["GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem"]
    ] = UNSET
    mfa_verification_factors: Union[
        Unset, List[GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserMfaVerificationFactorsItem]
    ] = UNSET
    roles: Union[Unset, List["GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItem"]] = UNSET
    organizations: Union[
        Unset, List["GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationsItem"]
    ] = UNSET
    organization_roles: Union[
        Unset, List["GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationRolesItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

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

        identities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identities, Unset):
            identities = self.identities.to_dict()

        last_sign_in_at: Union[None, Unset, float]
        if isinstance(self.last_sign_in_at, Unset):
            last_sign_in_at = UNSET
        else:
            last_sign_in_at = self.last_sign_in_at

        created_at = self.created_at

        updated_at = self.updated_at

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        application_id: Union[None, Unset, str]
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        else:
            application_id = self.application_id

        is_suspended = self.is_suspended

        sso_identities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sso_identities, Unset):
            sso_identities = []
            for sso_identities_item_data in self.sso_identities:
                sso_identities_item = sso_identities_item_data.to_dict()
                sso_identities.append(sso_identities_item)

        mfa_verification_factors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mfa_verification_factors, Unset):
            mfa_verification_factors = []
            for mfa_verification_factors_item_data in self.mfa_verification_factors:
                mfa_verification_factors_item = mfa_verification_factors_item_data.value
                mfa_verification_factors.append(mfa_verification_factors_item)

        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        organization_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organization_roles, Unset):
            organization_roles = []
            for organization_roles_item_data in self.organization_roles:
                organization_roles_item = organization_roles_item_data.to_dict()
                organization_roles.append(organization_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        if identities is not UNSET:
            field_dict["identities"] = identities
        if last_sign_in_at is not UNSET:
            field_dict["lastSignInAt"] = last_sign_in_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if profile is not UNSET:
            field_dict["profile"] = profile
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if is_suspended is not UNSET:
            field_dict["isSuspended"] = is_suspended
        if sso_identities is not UNSET:
            field_dict["ssoIdentities"] = sso_identities
        if mfa_verification_factors is not UNSET:
            field_dict["mfaVerificationFactors"] = mfa_verification_factors
        if roles is not UNSET:
            field_dict["roles"] = roles
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if organization_roles is not UNSET:
            field_dict["organizationRoles"] = organization_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_custom_data import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserCustomData,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_identities import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserIdentities,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_organization_roles_item import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationRolesItem,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_organizations_item import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationsItem,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_profile import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserProfile,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_roles_item import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItem,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

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
        custom_data: Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserCustomData]
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserCustomData.from_dict(
                _custom_data
            )

        _identities = d.pop("identities", UNSET)
        identities: Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserIdentities]
        if isinstance(_identities, Unset):
            identities = UNSET
        else:
            identities = GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserIdentities.from_dict(
                _identities
            )

        def _parse_last_sign_in_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_sign_in_at = _parse_last_sign_in_at(d.pop("lastSignInAt", UNSET))

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserProfile.from_dict(_profile)

        def _parse_application_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))

        is_suspended = d.pop("isSuspended", UNSET)

        sso_identities = []
        _sso_identities = d.pop("ssoIdentities", UNSET)
        for sso_identities_item_data in _sso_identities or []:
            sso_identities_item = (
                GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem.from_dict(
                    sso_identities_item_data
                )
            )

            sso_identities.append(sso_identities_item)

        mfa_verification_factors = []
        _mfa_verification_factors = d.pop("mfaVerificationFactors", UNSET)
        for mfa_verification_factors_item_data in _mfa_verification_factors or []:
            mfa_verification_factors_item = (
                GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserMfaVerificationFactorsItem(
                    mfa_verification_factors_item_data
                )
            )

            mfa_verification_factors.append(mfa_verification_factors_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserRolesItem.from_dict(
                roles_item_data
            )

            roles.append(roles_item)

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = (
                GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationsItem.from_dict(
                    organizations_item_data
                )
            )

            organizations.append(organizations_item)

        organization_roles = []
        _organization_roles = d.pop("organizationRoles", UNSET)
        for organization_roles_item_data in _organization_roles or []:
            organization_roles_item = (
                GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserOrganizationRolesItem.from_dict(
                    organization_roles_item_data
                )
            )

            organization_roles.append(organization_roles_item)

        get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user = cls(
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
            sso_identities=sso_identities,
            mfa_verification_factors=mfa_verification_factors,
            roles=roles,
            organizations=organizations,
            organization_roles=organization_roles,
        )

        get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user.additional_properties = d
        return get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user

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
