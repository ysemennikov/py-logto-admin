from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_sign_in_exp_response_200_sign_in_mode import GetApiSignInExpResponse200SignInMode

if TYPE_CHECKING:
    from ..models.get_api_sign_in_exp_response_200_branding import GetApiSignInExpResponse200Branding
    from ..models.get_api_sign_in_exp_response_200_color import GetApiSignInExpResponse200Color
    from ..models.get_api_sign_in_exp_response_200_custom_content import GetApiSignInExpResponse200CustomContent
    from ..models.get_api_sign_in_exp_response_200_language_info import GetApiSignInExpResponse200LanguageInfo
    from ..models.get_api_sign_in_exp_response_200_mfa import GetApiSignInExpResponse200Mfa
    from ..models.get_api_sign_in_exp_response_200_password_policy import GetApiSignInExpResponse200PasswordPolicy
    from ..models.get_api_sign_in_exp_response_200_sign_in import GetApiSignInExpResponse200SignIn
    from ..models.get_api_sign_in_exp_response_200_sign_up import GetApiSignInExpResponse200SignUp


T = TypeVar("T", bound="GetApiSignInExpResponse200")


@_attrs_define
class GetApiSignInExpResponse200:
    """
    Attributes:
        id (str):
        color (GetApiSignInExpResponse200Color): The primary branding color for the sign-in page (both light/dark mode).
        branding (GetApiSignInExpResponse200Branding):
        language_info (GetApiSignInExpResponse200LanguageInfo): The language detection policy for the sign-in page.
        terms_of_use_url (Union[None, str]):
        privacy_policy_url (Union[None, str]):
        sign_in (GetApiSignInExpResponse200SignIn): Sign-in method settings.
        sign_up (GetApiSignInExpResponse200SignUp): Sign-up method settings.
        social_sign_in_connector_targets (List[str]): Enabled social sign-in connectors, will displayed on the sign-in
            page.
        sign_in_mode (GetApiSignInExpResponse200SignInMode):
        custom_css (Union[None, str]):
        custom_content (GetApiSignInExpResponse200CustomContent): Custom content to display on experience flow pages.
            the page pathname will be the config key, the content will be the config value.
        password_policy (GetApiSignInExpResponse200PasswordPolicy): Password policies to adjust the password strength
            requirements.
        mfa (GetApiSignInExpResponse200Mfa): MFA settings
        single_sign_on_enabled (bool):
    """

    id: str
    color: "GetApiSignInExpResponse200Color"
    branding: "GetApiSignInExpResponse200Branding"
    language_info: "GetApiSignInExpResponse200LanguageInfo"
    terms_of_use_url: Union[None, str]
    privacy_policy_url: Union[None, str]
    sign_in: "GetApiSignInExpResponse200SignIn"
    sign_up: "GetApiSignInExpResponse200SignUp"
    social_sign_in_connector_targets: List[str]
    sign_in_mode: GetApiSignInExpResponse200SignInMode
    custom_css: Union[None, str]
    custom_content: "GetApiSignInExpResponse200CustomContent"
    password_policy: "GetApiSignInExpResponse200PasswordPolicy"
    mfa: "GetApiSignInExpResponse200Mfa"
    single_sign_on_enabled: bool
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
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_sign_in_exp_response_200_branding import GetApiSignInExpResponse200Branding
        from ..models.get_api_sign_in_exp_response_200_color import GetApiSignInExpResponse200Color
        from ..models.get_api_sign_in_exp_response_200_custom_content import GetApiSignInExpResponse200CustomContent
        from ..models.get_api_sign_in_exp_response_200_language_info import GetApiSignInExpResponse200LanguageInfo
        from ..models.get_api_sign_in_exp_response_200_mfa import GetApiSignInExpResponse200Mfa
        from ..models.get_api_sign_in_exp_response_200_password_policy import GetApiSignInExpResponse200PasswordPolicy
        from ..models.get_api_sign_in_exp_response_200_sign_in import GetApiSignInExpResponse200SignIn
        from ..models.get_api_sign_in_exp_response_200_sign_up import GetApiSignInExpResponse200SignUp

        d = src_dict.copy()
        id = d.pop("id")

        color = GetApiSignInExpResponse200Color.from_dict(d.pop("color"))

        branding = GetApiSignInExpResponse200Branding.from_dict(d.pop("branding"))

        language_info = GetApiSignInExpResponse200LanguageInfo.from_dict(d.pop("languageInfo"))

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

        sign_in = GetApiSignInExpResponse200SignIn.from_dict(d.pop("signIn"))

        sign_up = GetApiSignInExpResponse200SignUp.from_dict(d.pop("signUp"))

        social_sign_in_connector_targets = cast(List[str], d.pop("socialSignInConnectorTargets"))

        sign_in_mode = GetApiSignInExpResponse200SignInMode(d.pop("signInMode"))

        def _parse_custom_css(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        custom_css = _parse_custom_css(d.pop("customCss"))

        custom_content = GetApiSignInExpResponse200CustomContent.from_dict(d.pop("customContent"))

        password_policy = GetApiSignInExpResponse200PasswordPolicy.from_dict(d.pop("passwordPolicy"))

        mfa = GetApiSignInExpResponse200Mfa.from_dict(d.pop("mfa"))

        single_sign_on_enabled = d.pop("singleSignOnEnabled")

        get_api_sign_in_exp_response_200 = cls(
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
        )

        get_api_sign_in_exp_response_200.additional_properties = d
        return get_api_sign_in_exp_response_200

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
