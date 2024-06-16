from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_applications_application_id_user_consent_scopes_body_user_scopes_item import (
    PostApiApplicationsApplicationIdUserConsentScopesBodyUserScopesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiApplicationsApplicationIdUserConsentScopesBody")


@_attrs_define
class PostApiApplicationsApplicationIdUserConsentScopesBody:
    """
    Attributes:
        organization_scopes (Union[Unset, List[str]]): A list of organization scope id to assign to the application.
            Throws error if any given organization scope is not found.
        resource_scopes (Union[Unset, List[str]]): A list of resource scope id to assign to the application. Throws
            error if any given resource scope is not found.
        organization_resource_scopes (Union[Unset, List[str]]): A list of organization resource scope id to assign to
            the application. Throws error if any given resource scope is not found.
        user_scopes (Union[Unset, List[PostApiApplicationsApplicationIdUserConsentScopesBodyUserScopesItem]]): A list of
            user scope enum value to assign to the application.
    """

    organization_scopes: Union[Unset, List[str]] = UNSET
    resource_scopes: Union[Unset, List[str]] = UNSET
    organization_resource_scopes: Union[Unset, List[str]] = UNSET
    user_scopes: Union[Unset, List[PostApiApplicationsApplicationIdUserConsentScopesBodyUserScopesItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organization_scopes, Unset):
            organization_scopes = self.organization_scopes

        resource_scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.resource_scopes, Unset):
            resource_scopes = self.resource_scopes

        organization_resource_scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organization_resource_scopes, Unset):
            organization_resource_scopes = self.organization_resource_scopes

        user_scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_scopes, Unset):
            user_scopes = []
            for user_scopes_item_data in self.user_scopes:
                user_scopes_item = user_scopes_item_data.value
                user_scopes.append(user_scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_scopes is not UNSET:
            field_dict["organizationScopes"] = organization_scopes
        if resource_scopes is not UNSET:
            field_dict["resourceScopes"] = resource_scopes
        if organization_resource_scopes is not UNSET:
            field_dict["organizationResourceScopes"] = organization_resource_scopes
        if user_scopes is not UNSET:
            field_dict["userScopes"] = user_scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_scopes = cast(List[str], d.pop("organizationScopes", UNSET))

        resource_scopes = cast(List[str], d.pop("resourceScopes", UNSET))

        organization_resource_scopes = cast(List[str], d.pop("organizationResourceScopes", UNSET))

        user_scopes = []
        _user_scopes = d.pop("userScopes", UNSET)
        for user_scopes_item_data in _user_scopes or []:
            user_scopes_item = PostApiApplicationsApplicationIdUserConsentScopesBodyUserScopesItem(
                user_scopes_item_data
            )

            user_scopes.append(user_scopes_item)

        post_api_applications_application_id_user_consent_scopes_body = cls(
            organization_scopes=organization_scopes,
            resource_scopes=resource_scopes,
            organization_resource_scopes=organization_resource_scopes,
            user_scopes=user_scopes,
        )

        post_api_applications_application_id_user_consent_scopes_body.additional_properties = d
        return post_api_applications_application_id_user_consent_scopes_body

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
