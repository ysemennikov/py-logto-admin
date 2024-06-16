from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_sign_in_exp_response_200_sign_in_mode import PatchApiSignInExpResponse200SignInMode

if TYPE_CHECKING:
    from ..models.patch_api_sign_in_exp_response_200_branding import PatchApiSignInExpResponse200Branding
    from ..models.patch_api_sign_in_exp_response_200_color import PatchApiSignInExpResponse200Color
    from ..models.patch_api_sign_in_exp_response_200_custom_content import PatchApiSignInExpResponse200CustomContent
    from ..models.patch_api_sign_in_exp_response_200_language_info import PatchApiSignInExpResponse200LanguageInfo
    from ..models.patch_api_sign_in_exp_response_200_mfa import PatchApiSignInExpResponse200Mfa
    from ..models.patch_api_sign_in_exp_response_200_password_policy import PatchApiSignInExpResponse200PasswordPolicy
    from ..models.patch_api_sign_in_exp_response_200_sign_in import PatchApiSignInExpResponse200SignIn
    from ..models.patch_api_sign_in_exp_response_200_sign_up import PatchApiSignInExpResponse200SignUp


T = TypeVar("T", bound="PatchApiSignInExpResponse200")


@_attrs_define
class PatchApiSignInExpResponse200:
    """
    Attributes:
        id (str):
        color (PatchApiSignInExpResponse200Color):
        branding (PatchApiSignInExpResponse200Branding):
        language_info (PatchApiSignInExpResponse200LanguageInfo):
        terms_of_use_url (Union[None, str]):
        privacy_policy_url (Union[None, str]):
        sign_in (PatchApiSignInExpResponse200SignIn):
        sign_up (PatchApiSignInExpResponse200SignUp):
        social_sign_in_connector_targets (List[str]):
        sign_in_mode (PatchApiSignInExpResponse200SignInMode):
        custom_css (Union[None, str]):
        custom_content (PatchApiSignInExpResponse200CustomContent):
        password_policy (PatchApiSignInExpResponse200PasswordPolicy):
        mfa (PatchApiSignInExpResponse200Mfa):
        single_sign_on_enabled (bool):
    """

    id: str
    color: "PatchApiSignInExpResponse200Color"
    branding: "PatchApiSignInExpResponse200Branding"
    language_info: "PatchApiSignInExpResponse200LanguageInfo"
    terms_of_use_url: Union[None, str]
    privacy_policy_url: Union[None, str]
    sign_in: "PatchApiSignInExpResponse200SignIn"
    sign_up: "PatchApiSignInExpResponse200SignUp"
    social_sign_in_connector_targets: List[str]
    sign_in_mode: PatchApiSignInExpResponse200SignInMode
    custom_css: Union[None, str]
    custom_content: "PatchApiSignInExpResponse200CustomContent"
    password_policy: "PatchApiSignInExpResponse200PasswordPolicy"
    mfa: "PatchApiSignInExpResponse200Mfa"
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
        from ..models.patch_api_sign_in_exp_response_200_branding import PatchApiSignInExpResponse200Branding
        from ..models.patch_api_sign_in_exp_response_200_color import PatchApiSignInExpResponse200Color
        from ..models.patch_api_sign_in_exp_response_200_custom_content import PatchApiSignInExpResponse200CustomContent
        from ..models.patch_api_sign_in_exp_response_200_language_info import PatchApiSignInExpResponse200LanguageInfo
        from ..models.patch_api_sign_in_exp_response_200_mfa import PatchApiSignInExpResponse200Mfa
        from ..models.patch_api_sign_in_exp_response_200_password_policy import (
            PatchApiSignInExpResponse200PasswordPolicy,
        )
        from ..models.patch_api_sign_in_exp_response_200_sign_in import PatchApiSignInExpResponse200SignIn
        from ..models.patch_api_sign_in_exp_response_200_sign_up import PatchApiSignInExpResponse200SignUp

        d = src_dict.copy()
        id = d.pop("id")

        color = PatchApiSignInExpResponse200Color.from_dict(d.pop("color"))

        branding = PatchApiSignInExpResponse200Branding.from_dict(d.pop("branding"))

        language_info = PatchApiSignInExpResponse200LanguageInfo.from_dict(d.pop("languageInfo"))

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

        sign_in = PatchApiSignInExpResponse200SignIn.from_dict(d.pop("signIn"))

        sign_up = PatchApiSignInExpResponse200SignUp.from_dict(d.pop("signUp"))

        social_sign_in_connector_targets = cast(List[str], d.pop("socialSignInConnectorTargets"))

        sign_in_mode = PatchApiSignInExpResponse200SignInMode(d.pop("signInMode"))

        def _parse_custom_css(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        custom_css = _parse_custom_css(d.pop("customCss"))

        custom_content = PatchApiSignInExpResponse200CustomContent.from_dict(d.pop("customContent"))

        password_policy = PatchApiSignInExpResponse200PasswordPolicy.from_dict(d.pop("passwordPolicy"))

        mfa = PatchApiSignInExpResponse200Mfa.from_dict(d.pop("mfa"))

        single_sign_on_enabled = d.pop("singleSignOnEnabled")

        patch_api_sign_in_exp_response_200 = cls(
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

        patch_api_sign_in_exp_response_200.additional_properties = d
        return patch_api_sign_in_exp_response_200

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
