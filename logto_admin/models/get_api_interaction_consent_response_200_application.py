from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_interaction_consent_response_200_application_branding import (
        GetApiInteractionConsentResponse200ApplicationBranding,
    )


T = TypeVar("T", bound="GetApiInteractionConsentResponse200Application")


@_attrs_define
class GetApiInteractionConsentResponse200Application:
    """
    Attributes:
        id (str):
        name (str):
        branding (Union[Unset, GetApiInteractionConsentResponse200ApplicationBranding]):
        display_name (Union[None, Unset, str]):
        privacy_policy_url (Union[None, Unset, str]):
        terms_of_use_url (Union[None, Unset, str]):
    """

    id: str
    name: str
    branding: Union[Unset, "GetApiInteractionConsentResponse200ApplicationBranding"] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    privacy_policy_url: Union[None, Unset, str] = UNSET
    terms_of_use_url: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        branding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branding, Unset):
            branding = self.branding.to_dict()

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        privacy_policy_url: Union[None, Unset, str]
        if isinstance(self.privacy_policy_url, Unset):
            privacy_policy_url = UNSET
        else:
            privacy_policy_url = self.privacy_policy_url

        terms_of_use_url: Union[None, Unset, str]
        if isinstance(self.terms_of_use_url, Unset):
            terms_of_use_url = UNSET
        else:
            terms_of_use_url = self.terms_of_use_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if branding is not UNSET:
            field_dict["branding"] = branding
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if privacy_policy_url is not UNSET:
            field_dict["privacyPolicyUrl"] = privacy_policy_url
        if terms_of_use_url is not UNSET:
            field_dict["termsOfUseUrl"] = terms_of_use_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_interaction_consent_response_200_application_branding import (
            GetApiInteractionConsentResponse200ApplicationBranding,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _branding = d.pop("branding", UNSET)
        branding: Union[Unset, GetApiInteractionConsentResponse200ApplicationBranding]
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = GetApiInteractionConsentResponse200ApplicationBranding.from_dict(_branding)

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_privacy_policy_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        privacy_policy_url = _parse_privacy_policy_url(d.pop("privacyPolicyUrl", UNSET))

        def _parse_terms_of_use_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        terms_of_use_url = _parse_terms_of_use_url(d.pop("termsOfUseUrl", UNSET))

        get_api_interaction_consent_response_200_application = cls(
            id=id,
            name=name,
            branding=branding,
            display_name=display_name,
            privacy_policy_url=privacy_policy_url,
            terms_of_use_url=terms_of_use_url,
        )

        get_api_interaction_consent_response_200_application.additional_properties = d
        return get_api_interaction_consent_response_200_application

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
