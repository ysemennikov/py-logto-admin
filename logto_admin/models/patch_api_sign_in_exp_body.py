from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_sign_in_exp_body_sign_in_mode import PatchApiSignInExpBodySignInMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_sign_in_exp_body_branding import PatchApiSignInExpBodyBranding
    from ..models.patch_api_sign_in_exp_body_color import PatchApiSignInExpBodyColor
    from ..models.patch_api_sign_in_exp_body_custom_content import PatchApiSignInExpBodyCustomContent
    from ..models.patch_api_sign_in_exp_body_language_info import PatchApiSignInExpBodyLanguageInfo
    from ..models.patch_api_sign_in_exp_body_mfa import PatchApiSignInExpBodyMfa
    from ..models.patch_api_sign_in_exp_body_password_policy import PatchApiSignInExpBodyPasswordPolicy
    from ..models.patch_api_sign_in_exp_body_sign_in import PatchApiSignInExpBodySignIn
    from ..models.patch_api_sign_in_exp_body_sign_up import PatchApiSignInExpBodySignUp


T = TypeVar("T", bound="PatchApiSignInExpBody")


@_attrs_define
class PatchApiSignInExpBody:
    """
    Attributes:
        color (Union[Unset, PatchApiSignInExpBodyColor]): Specify the primary branding color for the sign-in page (both
            light/dark mode).
        branding (Union[Unset, PatchApiSignInExpBodyBranding]):
        language_info (Union[Unset, PatchApiSignInExpBodyLanguageInfo]): Control the language detection policy for the
            sign-in page.
        sign_in (Union[Unset, PatchApiSignInExpBodySignIn]): Sign-in method settings
        sign_up (Union[Unset, PatchApiSignInExpBodySignUp]): Sign-up method settings
        social_sign_in_connector_targets (Union[Unset, List[str]]): Specify the social sign-in connectors to display on
            the sign-in page.
        sign_in_mode (Union[Unset, PatchApiSignInExpBodySignInMode]):
        custom_css (Union[None, Unset, str]):
        custom_content (Union[Unset, PatchApiSignInExpBodyCustomContent]): Custom content to display on experience flow
            pages. the page pathname will be the config key, the content will be the config value.
        password_policy (Union[Unset, PatchApiSignInExpBodyPasswordPolicy]): Password policies to adjust the password
            strength requirements.
        mfa (Union[Unset, PatchApiSignInExpBodyMfa]): MFA settings
        single_sign_on_enabled (Union[Unset, bool]):
        terms_of_use_url (Union[None, Unset, str]):
        privacy_policy_url (Union[None, Unset, str]):
    """

    color: Union[Unset, "PatchApiSignInExpBodyColor"] = UNSET
    branding: Union[Unset, "PatchApiSignInExpBodyBranding"] = UNSET
    language_info: Union[Unset, "PatchApiSignInExpBodyLanguageInfo"] = UNSET
    sign_in: Union[Unset, "PatchApiSignInExpBodySignIn"] = UNSET
    sign_up: Union[Unset, "PatchApiSignInExpBodySignUp"] = UNSET
    social_sign_in_connector_targets: Union[Unset, List[str]] = UNSET
    sign_in_mode: Union[Unset, PatchApiSignInExpBodySignInMode] = UNSET
    custom_css: Union[None, Unset, str] = UNSET
    custom_content: Union[Unset, "PatchApiSignInExpBodyCustomContent"] = UNSET
    password_policy: Union[Unset, "PatchApiSignInExpBodyPasswordPolicy"] = UNSET
    mfa: Union[Unset, "PatchApiSignInExpBodyMfa"] = UNSET
    single_sign_on_enabled: Union[Unset, bool] = UNSET
    terms_of_use_url: Union[None, Unset, str] = UNSET
    privacy_policy_url: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        branding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branding, Unset):
            branding = self.branding.to_dict()

        language_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.language_info, Unset):
            language_info = self.language_info.to_dict()

        sign_in: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sign_in, Unset):
            sign_in = self.sign_in.to_dict()

        sign_up: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sign_up, Unset):
            sign_up = self.sign_up.to_dict()

        social_sign_in_connector_targets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.social_sign_in_connector_targets, Unset):
            social_sign_in_connector_targets = self.social_sign_in_connector_targets

        sign_in_mode: Union[Unset, str] = UNSET
        if not isinstance(self.sign_in_mode, Unset):
            sign_in_mode = self.sign_in_mode.value

        custom_css: Union[None, Unset, str]
        if isinstance(self.custom_css, Unset):
            custom_css = UNSET
        else:
            custom_css = self.custom_css

        custom_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_content, Unset):
            custom_content = self.custom_content.to_dict()

        password_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password_policy, Unset):
            password_policy = self.password_policy.to_dict()

        mfa: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mfa, Unset):
            mfa = self.mfa.to_dict()

        single_sign_on_enabled = self.single_sign_on_enabled

        terms_of_use_url: Union[None, Unset, str]
        if isinstance(self.terms_of_use_url, Unset):
            terms_of_use_url = UNSET
        else:
            terms_of_use_url = self.terms_of_use_url

        privacy_policy_url: Union[None, Unset, str]
        if isinstance(self.privacy_policy_url, Unset):
            privacy_policy_url = UNSET
        else:
            privacy_policy_url = self.privacy_policy_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if branding is not UNSET:
            field_dict["branding"] = branding
        if language_info is not UNSET:
            field_dict["languageInfo"] = language_info
        if sign_in is not UNSET:
            field_dict["signIn"] = sign_in
        if sign_up is not UNSET:
            field_dict["signUp"] = sign_up
        if social_sign_in_connector_targets is not UNSET:
            field_dict["socialSignInConnectorTargets"] = social_sign_in_connector_targets
        if sign_in_mode is not UNSET:
            field_dict["signInMode"] = sign_in_mode
        if custom_css is not UNSET:
            field_dict["customCss"] = custom_css
        if custom_content is not UNSET:
            field_dict["customContent"] = custom_content
        if password_policy is not UNSET:
            field_dict["passwordPolicy"] = password_policy
        if mfa is not UNSET:
            field_dict["mfa"] = mfa
        if single_sign_on_enabled is not UNSET:
            field_dict["singleSignOnEnabled"] = single_sign_on_enabled
        if terms_of_use_url is not UNSET:
            field_dict["termsOfUseUrl"] = terms_of_use_url
        if privacy_policy_url is not UNSET:
            field_dict["privacyPolicyUrl"] = privacy_policy_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_sign_in_exp_body_branding import PatchApiSignInExpBodyBranding
        from ..models.patch_api_sign_in_exp_body_color import PatchApiSignInExpBodyColor
        from ..models.patch_api_sign_in_exp_body_custom_content import PatchApiSignInExpBodyCustomContent
        from ..models.patch_api_sign_in_exp_body_language_info import PatchApiSignInExpBodyLanguageInfo
        from ..models.patch_api_sign_in_exp_body_mfa import PatchApiSignInExpBodyMfa
        from ..models.patch_api_sign_in_exp_body_password_policy import PatchApiSignInExpBodyPasswordPolicy
        from ..models.patch_api_sign_in_exp_body_sign_in import PatchApiSignInExpBodySignIn
        from ..models.patch_api_sign_in_exp_body_sign_up import PatchApiSignInExpBodySignUp

        d = src_dict.copy()
        _color = d.pop("color", UNSET)
        color: Union[Unset, PatchApiSignInExpBodyColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = PatchApiSignInExpBodyColor.from_dict(_color)

        _branding = d.pop("branding", UNSET)
        branding: Union[Unset, PatchApiSignInExpBodyBranding]
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = PatchApiSignInExpBodyBranding.from_dict(_branding)

        _language_info = d.pop("languageInfo", UNSET)
        language_info: Union[Unset, PatchApiSignInExpBodyLanguageInfo]
        if isinstance(_language_info, Unset):
            language_info = UNSET
        else:
            language_info = PatchApiSignInExpBodyLanguageInfo.from_dict(_language_info)

        _sign_in = d.pop("signIn", UNSET)
        sign_in: Union[Unset, PatchApiSignInExpBodySignIn]
        if isinstance(_sign_in, Unset):
            sign_in = UNSET
        else:
            sign_in = PatchApiSignInExpBodySignIn.from_dict(_sign_in)

        _sign_up = d.pop("signUp", UNSET)
        sign_up: Union[Unset, PatchApiSignInExpBodySignUp]
        if isinstance(_sign_up, Unset):
            sign_up = UNSET
        else:
            sign_up = PatchApiSignInExpBodySignUp.from_dict(_sign_up)

        social_sign_in_connector_targets = cast(List[str], d.pop("socialSignInConnectorTargets", UNSET))

        _sign_in_mode = d.pop("signInMode", UNSET)
        sign_in_mode: Union[Unset, PatchApiSignInExpBodySignInMode]
        if isinstance(_sign_in_mode, Unset):
            sign_in_mode = UNSET
        else:
            sign_in_mode = PatchApiSignInExpBodySignInMode(_sign_in_mode)

        def _parse_custom_css(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_css = _parse_custom_css(d.pop("customCss", UNSET))

        _custom_content = d.pop("customContent", UNSET)
        custom_content: Union[Unset, PatchApiSignInExpBodyCustomContent]
        if isinstance(_custom_content, Unset):
            custom_content = UNSET
        else:
            custom_content = PatchApiSignInExpBodyCustomContent.from_dict(_custom_content)

        _password_policy = d.pop("passwordPolicy", UNSET)
        password_policy: Union[Unset, PatchApiSignInExpBodyPasswordPolicy]
        if isinstance(_password_policy, Unset):
            password_policy = UNSET
        else:
            password_policy = PatchApiSignInExpBodyPasswordPolicy.from_dict(_password_policy)

        _mfa = d.pop("mfa", UNSET)
        mfa: Union[Unset, PatchApiSignInExpBodyMfa]
        if isinstance(_mfa, Unset):
            mfa = UNSET
        else:
            mfa = PatchApiSignInExpBodyMfa.from_dict(_mfa)

        single_sign_on_enabled = d.pop("singleSignOnEnabled", UNSET)

        def _parse_terms_of_use_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        terms_of_use_url = _parse_terms_of_use_url(d.pop("termsOfUseUrl", UNSET))

        def _parse_privacy_policy_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        privacy_policy_url = _parse_privacy_policy_url(d.pop("privacyPolicyUrl", UNSET))

        patch_api_sign_in_exp_body = cls(
            color=color,
            branding=branding,
            language_info=language_info,
            sign_in=sign_in,
            sign_up=sign_up,
            social_sign_in_connector_targets=social_sign_in_connector_targets,
            sign_in_mode=sign_in_mode,
            custom_css=custom_css,
            custom_content=custom_content,
            password_policy=password_policy,
            mfa=mfa,
            single_sign_on_enabled=single_sign_on_enabled,
            terms_of_use_url=terms_of_use_url,
            privacy_policy_url=privacy_policy_url,
        )

        patch_api_sign_in_exp_body.additional_properties = d
        return patch_api_sign_in_exp_body

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
