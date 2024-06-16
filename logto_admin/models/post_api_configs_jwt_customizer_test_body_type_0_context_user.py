from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_mfa_verification_factors_item import (
    PostApiConfigsJwtCustomizerTestBodyType0ContextUserMfaVerificationFactorsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_custom_data import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserCustomData,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_identities import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserIdentities,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_organization_roles_item import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationRolesItem,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_organizations_item import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationsItem,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_profile import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserProfile,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem,
    )


T = TypeVar("T", bound="PostApiConfigsJwtCustomizerTestBodyType0ContextUser")


@_attrs_define
class PostApiConfigsJwtCustomizerTestBodyType0ContextUser:
    """
    Attributes:
        id (Union[Unset, str]):
        username (Union[None, Unset, str]):
        primary_email (Union[None, Unset, str]):
        primary_phone (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        avatar (Union[None, Unset, str]):
        custom_data (Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0ContextUserCustomData]): arbitrary
        identities (Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0ContextUserIdentities]):
        last_sign_in_at (Union[None, Unset, float]):
        created_at (Union[Unset, float]):
        updated_at (Union[Unset, float]):
        profile (Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0ContextUserProfile]):
        application_id (Union[None, Unset, str]):
        is_suspended (Union[Unset, bool]):
        sso_identities (Union[Unset, List['PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem']]):
        mfa_verification_factors (Union[Unset,
            List[PostApiConfigsJwtCustomizerTestBodyType0ContextUserMfaVerificationFactorsItem]]):
        roles (Union[Unset, List['PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem']]):
        organizations (Union[Unset, List['PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationsItem']]):
        organization_roles (Union[Unset,
            List['PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationRolesItem']]):
    """

    id: Union[Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    primary_email: Union[None, Unset, str] = UNSET
    primary_phone: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    avatar: Union[None, Unset, str] = UNSET
    custom_data: Union[Unset, "PostApiConfigsJwtCustomizerTestBodyType0ContextUserCustomData"] = UNSET
    identities: Union[Unset, "PostApiConfigsJwtCustomizerTestBodyType0ContextUserIdentities"] = UNSET
    last_sign_in_at: Union[None, Unset, float] = UNSET
    created_at: Union[Unset, float] = UNSET
    updated_at: Union[Unset, float] = UNSET
    profile: Union[Unset, "PostApiConfigsJwtCustomizerTestBodyType0ContextUserProfile"] = UNSET
    application_id: Union[None, Unset, str] = UNSET
    is_suspended: Union[Unset, bool] = UNSET
    sso_identities: Union[Unset, List["PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem"]] = UNSET
    mfa_verification_factors: Union[
        Unset, List[PostApiConfigsJwtCustomizerTestBodyType0ContextUserMfaVerificationFactorsItem]
    ] = UNSET
    roles: Union[Unset, List["PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem"]] = UNSET
    organizations: Union[Unset, List["PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationsItem"]] = UNSET
    organization_roles: Union[
        Unset, List["PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationRolesItem"]
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
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_custom_data import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserCustomData,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_identities import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserIdentities,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_organization_roles_item import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationRolesItem,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_organizations_item import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationsItem,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_profile import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserProfile,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_roles_item import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem,
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
        custom_data: Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0ContextUserCustomData]
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = PostApiConfigsJwtCustomizerTestBodyType0ContextUserCustomData.from_dict(_custom_data)

        _identities = d.pop("identities", UNSET)
        identities: Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0ContextUserIdentities]
        if isinstance(_identities, Unset):
            identities = UNSET
        else:
            identities = PostApiConfigsJwtCustomizerTestBodyType0ContextUserIdentities.from_dict(_identities)

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
        profile: Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0ContextUserProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = PostApiConfigsJwtCustomizerTestBodyType0ContextUserProfile.from_dict(_profile)

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
            sso_identities_item = PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem.from_dict(
                sso_identities_item_data
            )

            sso_identities.append(sso_identities_item)

        mfa_verification_factors = []
        _mfa_verification_factors = d.pop("mfaVerificationFactors", UNSET)
        for mfa_verification_factors_item_data in _mfa_verification_factors or []:
            mfa_verification_factors_item = (
                PostApiConfigsJwtCustomizerTestBodyType0ContextUserMfaVerificationFactorsItem(
                    mfa_verification_factors_item_data
                )
            )

            mfa_verification_factors.append(mfa_verification_factors_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = PostApiConfigsJwtCustomizerTestBodyType0ContextUserRolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationsItem.from_dict(
                organizations_item_data
            )

            organizations.append(organizations_item)

        organization_roles = []
        _organization_roles = d.pop("organizationRoles", UNSET)
        for organization_roles_item_data in _organization_roles or []:
            organization_roles_item = (
                PostApiConfigsJwtCustomizerTestBodyType0ContextUserOrganizationRolesItem.from_dict(
                    organization_roles_item_data
                )
            )

            organization_roles.append(organization_roles_item)

        post_api_configs_jwt_customizer_test_body_type_0_context_user = cls(
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

        post_api_configs_jwt_customizer_test_body_type_0_context_user.additional_properties = d
        return post_api_configs_jwt_customizer_test_body_type_0_context_user

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
