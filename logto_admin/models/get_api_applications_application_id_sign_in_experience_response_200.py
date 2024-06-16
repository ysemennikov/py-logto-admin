from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_applications_application_id_sign_in_experience_response_200_branding import (
        GetApiApplicationsApplicationIdSignInExperienceResponse200Branding,
    )


T = TypeVar("T", bound="GetApiApplicationsApplicationIdSignInExperienceResponse200")


@_attrs_define
class GetApiApplicationsApplicationIdSignInExperienceResponse200:
    """
    Attributes:
        application_id (str):
        branding (GetApiApplicationsApplicationIdSignInExperienceResponse200Branding):
        terms_of_use_url (Union[None, str]):
        privacy_policy_url (Union[None, str]):
        display_name (Union[None, str]):
    """

    application_id: str
    branding: "GetApiApplicationsApplicationIdSignInExperienceResponse200Branding"
    terms_of_use_url: Union[None, str]
    privacy_policy_url: Union[None, str]
    display_name: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        application_id = self.application_id

        branding = self.branding.to_dict()

        terms_of_use_url: Union[None, str]
        terms_of_use_url = self.terms_of_use_url

        privacy_policy_url: Union[None, str]
        privacy_policy_url = self.privacy_policy_url

        display_name: Union[None, str]
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationId": application_id,
                "branding": branding,
                "termsOfUseUrl": terms_of_use_url,
                "privacyPolicyUrl": privacy_policy_url,
                "displayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_applications_application_id_sign_in_experience_response_200_branding import (
            GetApiApplicationsApplicationIdSignInExperienceResponse200Branding,
        )

        d = src_dict.copy()
        application_id = d.pop("applicationId")

        branding = GetApiApplicationsApplicationIdSignInExperienceResponse200Branding.from_dict(d.pop("branding"))

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

        def _parse_display_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        display_name = _parse_display_name(d.pop("displayName"))

        get_api_applications_application_id_sign_in_experience_response_200 = cls(
            application_id=application_id,
            branding=branding,
            terms_of_use_url=terms_of_use_url,
            privacy_policy_url=privacy_policy_url,
            display_name=display_name,
        )

        get_api_applications_application_id_sign_in_experience_response_200.additional_properties = d
        return get_api_applications_application_id_sign_in_experience_response_200

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
