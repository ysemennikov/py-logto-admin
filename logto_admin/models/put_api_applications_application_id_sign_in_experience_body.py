from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_applications_application_id_sign_in_experience_body_branding import (
        PutApiApplicationsApplicationIdSignInExperienceBodyBranding,
    )


T = TypeVar("T", bound="PutApiApplicationsApplicationIdSignInExperienceBody")


@_attrs_define
class PutApiApplicationsApplicationIdSignInExperienceBody:
    """
    Attributes:
        terms_of_use_url (Union[None, str]):
        privacy_policy_url (Union[None, str]):
        branding (Union[Unset, PutApiApplicationsApplicationIdSignInExperienceBodyBranding]):
        display_name (Union[None, Unset, str]):
    """

    terms_of_use_url: Union[None, str]
    privacy_policy_url: Union[None, str]
    branding: Union[Unset, "PutApiApplicationsApplicationIdSignInExperienceBodyBranding"] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        terms_of_use_url: Union[None, str]
        terms_of_use_url = self.terms_of_use_url

        privacy_policy_url: Union[None, str]
        privacy_policy_url = self.privacy_policy_url

        branding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branding, Unset):
            branding = self.branding.to_dict()

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "termsOfUseUrl": terms_of_use_url,
                "privacyPolicyUrl": privacy_policy_url,
            }
        )
        if branding is not UNSET:
            field_dict["branding"] = branding
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_applications_application_id_sign_in_experience_body_branding import (
            PutApiApplicationsApplicationIdSignInExperienceBodyBranding,
        )

        d = src_dict.copy()

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

        _branding = d.pop("branding", UNSET)
        branding: Union[Unset, PutApiApplicationsApplicationIdSignInExperienceBodyBranding]
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = PutApiApplicationsApplicationIdSignInExperienceBodyBranding.from_dict(_branding)

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        put_api_applications_application_id_sign_in_experience_body = cls(
            terms_of_use_url=terms_of_use_url,
            privacy_policy_url=privacy_policy_url,
            branding=branding,
            display_name=display_name,
        )

        put_api_applications_application_id_sign_in_experience_body.additional_properties = d
        return put_api_applications_application_id_sign_in_experience_body

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
