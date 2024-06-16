from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_well_known_sign_in_exp_response_200_sign_in_mode import (
    GetApiWellKnownSignInExpResponse200SignInMode,
)

if TYPE_CHECKING:
    from ..models.get_api_well_known_sign_in_exp_response_200_branding import (
        GetApiWellKnownSignInExpResponse200Branding,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_color import GetApiWellKnownSignInExpResponse200Color
    from ..models.get_api_well_known_sign_in_exp_response_200_custom_content import (
        GetApiWellKnownSignInExpResponse200CustomContent,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_forgot_password import (
        GetApiWellKnownSignInExpResponse200ForgotPassword,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_language_info import (
        GetApiWellKnownSignInExpResponse200LanguageInfo,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_mfa import GetApiWellKnownSignInExpResponse200Mfa
    from ..models.get_api_well_known_sign_in_exp_response_200_password_policy import (
        GetApiWellKnownSignInExpResponse200PasswordPolicy,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_sign_in import GetApiWellKnownSignInExpResponse200SignIn
    from ..models.get_api_well_known_sign_in_exp_response_200_sign_up import GetApiWellKnownSignInExpResponse200SignUp
    from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item import (
        GetApiWellKnownSignInExpResponse200SocialConnectorsItem,
    )
    from ..models.get_api_well_known_sign_in_exp_response_200_sso_connectors_item import (
        GetApiWellKnownSignInExpResponse200SsoConnectorsItem,
    )


T = TypeVar("T", bound="GetApiWellKnownSignInExpResponse200")


@_attrs_define
class GetApiWellKnownSignInExpResponse200:
    """
    Attributes:
        id (str):
        color (GetApiWellKnownSignInExpResponse200Color):
        branding (GetApiWellKnownSignInExpResponse200Branding):
        language_info (GetApiWellKnownSignInExpResponse200LanguageInfo):
        terms_of_use_url (Union[None, str]):
        privacy_policy_url (Union[None, str]):
        sign_in (GetApiWellKnownSignInExpResponse200SignIn):
        sign_up (GetApiWellKnownSignInExpResponse200SignUp):
        social_sign_in_connector_targets (List[str]):
        sign_in_mode (GetApiWellKnownSignInExpResponse200SignInMode):
        custom_css (Union[None, str]):
        custom_content (GetApiWellKnownSignInExpResponse200CustomContent):
        password_policy (GetApiWellKnownSignInExpResponse200PasswordPolicy):
        mfa (GetApiWellKnownSignInExpResponse200Mfa):
        single_sign_on_enabled (bool):
        social_connectors (List['GetApiWellKnownSignInExpResponse200SocialConnectorsItem']):
        sso_connectors (List['GetApiWellKnownSignInExpResponse200SsoConnectorsItem']):
        forgot_password (GetApiWellKnownSignInExpResponse200ForgotPassword):
        is_development_tenant (bool):
    """

    id: str
    color: "GetApiWellKnownSignInExpResponse200Color"
    branding: "GetApiWellKnownSignInExpResponse200Branding"
    language_info: "GetApiWellKnownSignInExpResponse200LanguageInfo"
    terms_of_use_url: Union[None, str]
    privacy_policy_url: Union[None, str]
    sign_in: "GetApiWellKnownSignInExpResponse200SignIn"
    sign_up: "GetApiWellKnownSignInExpResponse200SignUp"
    social_sign_in_connector_targets: List[str]
    sign_in_mode: GetApiWellKnownSignInExpResponse200SignInMode
    custom_css: Union[None, str]
    custom_content: "GetApiWellKnownSignInExpResponse200CustomContent"
    password_policy: "GetApiWellKnownSignInExpResponse200PasswordPolicy"
    mfa: "GetApiWellKnownSignInExpResponse200Mfa"
    single_sign_on_enabled: bool
    social_connectors: List["GetApiWellKnownSignInExpResponse200SocialConnectorsItem"]
    sso_connectors: List["GetApiWellKnownSignInExpResponse200SsoConnectorsItem"]
    forgot_password: "GetApiWellKnownSignInExpResponse200ForgotPassword"
    is_development_tenant: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        color = self.color.to_dict()

        branding = self.branding.to_dict()

        language_info = self.language_info.to_dict()

        terms_of_use_url: Union[None, str]
        terms_of_use_url = self.terms_of_use_url

        privacy_policy_url: Union[None, str]
        privacy_policy_url = self.privacy_policy_url

        sign_in = self.sign_in.to_dict()

        sign_up = self.sign_up.to_dict()

        social_sign_in_connector_targets = self.social_sign_in_connector_targets

        sign_in_mode = self.sign_in_mode.value

        custom_css: Union[None, str]
        custom_css = self.custom_css

        custom_content = self.custom_content.to_dict()

        password_policy = self.password_policy.to_dict()

        mfa = self.mfa.to_dict()

        single_sign_on_enabled = self.single_sign_on_enabled

        social_connectors = []
        for social_connectors_item_data in self.social_connectors:
            social_connectors_item = social_connectors_item_data.to_dict()
            social_connectors.append(social_connectors_item)

        sso_connectors = []
        for sso_connectors_item_data in self.sso_connectors:
            sso_connectors_item = sso_connectors_item_data.to_dict()
            sso_connectors.append(sso_connectors_item)

        forgot_password = self.forgot_password.to_dict()

        is_development_tenant = self.is_development_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "color": color,
                "branding": branding,
                "languageInfo": language_info,
                "termsOfUseUrl": terms_of_use_url,
                "privacyPolicyUrl": privacy_policy_url,
                "signIn": sign_in,
                "signUp": sign_up,
                "socialSignInConnectorTargets": social_sign_in_connector_targets,
                "signInMode": sign_in_mode,
                "customCss": custom_css,
                "customContent": custom_content,
                "passwordPolicy": password_policy,
                "mfa": mfa,
                "singleSignOnEnabled": single_sign_on_enabled,
                "socialConnectors": social_connectors,
                "ssoConnectors": sso_connectors,
                "forgotPassword": forgot_password,
                "isDevelopmentTenant": is_development_tenant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_well_known_sign_in_exp_response_200_branding import (
            GetApiWellKnownSignInExpResponse200Branding,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_color import GetApiWellKnownSignInExpResponse200Color
        from ..models.get_api_well_known_sign_in_exp_response_200_custom_content import (
            GetApiWellKnownSignInExpResponse200CustomContent,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_forgot_password import (
            GetApiWellKnownSignInExpResponse200ForgotPassword,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_language_info import (
            GetApiWellKnownSignInExpResponse200LanguageInfo,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_mfa import GetApiWellKnownSignInExpResponse200Mfa
        from ..models.get_api_well_known_sign_in_exp_response_200_password_policy import (
            GetApiWellKnownSignInExpResponse200PasswordPolicy,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_sign_in import (
            GetApiWellKnownSignInExpResponse200SignIn,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_sign_up import (
            GetApiWellKnownSignInExpResponse200SignUp,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_social_connectors_item import (
            GetApiWellKnownSignInExpResponse200SocialConnectorsItem,
        )
        from ..models.get_api_well_known_sign_in_exp_response_200_sso_connectors_item import (
            GetApiWellKnownSignInExpResponse200SsoConnectorsItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        color = GetApiWellKnownSignInExpResponse200Color.from_dict(d.pop("color"))

        branding = GetApiWellKnownSignInExpResponse200Branding.from_dict(d.pop("branding"))

        language_info = GetApiWellKnownSignInExpResponse200LanguageInfo.from_dict(d.pop("languageInfo"))

        def _parse_terms_of_use_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        terms_of_use_url = _parse_terms_of_use_url(d.pop("termsOfUseUrl"))

        def _parse_privacy_policy_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        privacy_policy_url = _parse_privacy_policy_url(d.pop("privacyPolicyUrl"))

        sign_in = GetApiWellKnownSignInExpResponse200SignIn.from_dict(d.pop("signIn"))

        sign_up = GetApiWellKnownSignInExpResponse200SignUp.from_dict(d.pop("signUp"))

        social_sign_in_connector_targets = cast(List[str], d.pop("socialSignInConnectorTargets"))

        sign_in_mode = GetApiWellKnownSignInExpResponse200SignInMode(d.pop("signInMode"))

        def _parse_custom_css(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        custom_css = _parse_custom_css(d.pop("customCss"))

        custom_content = GetApiWellKnownSignInExpResponse200CustomContent.from_dict(d.pop("customContent"))

        password_policy = GetApiWellKnownSignInExpResponse200PasswordPolicy.from_dict(d.pop("passwordPolicy"))

        mfa = GetApiWellKnownSignInExpResponse200Mfa.from_dict(d.pop("mfa"))

        single_sign_on_enabled = d.pop("singleSignOnEnabled")

        social_connectors = []
        _social_connectors = d.pop("socialConnectors")
        for social_connectors_item_data in _social_connectors:
            social_connectors_item = GetApiWellKnownSignInExpResponse200SocialConnectorsItem.from_dict(
                social_connectors_item_data
            )

            social_connectors.append(social_connectors_item)

        sso_connectors = []
        _sso_connectors = d.pop("ssoConnectors")
        for sso_connectors_item_data in _sso_connectors:
            sso_connectors_item = GetApiWellKnownSignInExpResponse200SsoConnectorsItem.from_dict(
                sso_connectors_item_data
            )

            sso_connectors.append(sso_connectors_item)

        forgot_password = GetApiWellKnownSignInExpResponse200ForgotPassword.from_dict(d.pop("forgotPassword"))

        is_development_tenant = d.pop("isDevelopmentTenant")

        get_api_well_known_sign_in_exp_response_200 = cls(
            id=id,
            color=color,
            branding=branding,
            language_info=language_info,
            terms_of_use_url=terms_of_use_url,
            privacy_policy_url=privacy_policy_url,
            sign_in=sign_in,
            sign_up=sign_up,
            social_sign_in_connector_targets=social_sign_in_connector_targets,
            sign_in_mode=sign_in_mode,
            custom_css=custom_css,
            custom_content=custom_content,
            password_policy=password_policy,
            mfa=mfa,
            single_sign_on_enabled=single_sign_on_enabled,
            social_connectors=social_connectors,
            sso_connectors=sso_connectors,
            forgot_password=forgot_password,
            is_development_tenant=is_development_tenant,
        )

        get_api_well_known_sign_in_exp_response_200.additional_properties = d
        return get_api_well_known_sign_in_exp_response_200

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
