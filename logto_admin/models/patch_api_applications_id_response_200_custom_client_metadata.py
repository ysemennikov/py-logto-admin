from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiApplicationsIdResponse200CustomClientMetadata")


@_attrs_define
class PatchApiApplicationsIdResponse200CustomClientMetadata:
    """
    Attributes:
        cors_allowed_origins (Union[Unset, List[str]]):
        id_token_ttl (Union[Unset, float]):
        refresh_token_ttl (Union[Unset, float]):
        refresh_token_ttl_in_days (Union[Unset, float]):
        always_issue_refresh_token (Union[Unset, bool]):
        rotate_refresh_token (Union[Unset, bool]):
    """

    cors_allowed_origins: Union[Unset, List[str]] = UNSET
    id_token_ttl: Union[Unset, float] = UNSET
    refresh_token_ttl: Union[Unset, float] = UNSET
    refresh_token_ttl_in_days: Union[Unset, float] = UNSET
    always_issue_refresh_token: Union[Unset, bool] = UNSET
    rotate_refresh_token: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cors_allowed_origins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cors_allowed_origins, Unset):
            cors_allowed_origins = self.cors_allowed_origins

        id_token_ttl = self.id_token_ttl

        refresh_token_ttl = self.refresh_token_ttl

        refresh_token_ttl_in_days = self.refresh_token_ttl_in_days

        always_issue_refresh_token = self.always_issue_refresh_token

        rotate_refresh_token = self.rotate_refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cors_allowed_origins is not UNSET:
            field_dict["corsAllowedOrigins"] = cors_allowed_origins
        if id_token_ttl is not UNSET:
            field_dict["idTokenTtl"] = id_token_ttl
        if refresh_token_ttl is not UNSET:
            field_dict["refreshTokenTtl"] = refresh_token_ttl
        if refresh_token_ttl_in_days is not UNSET:
            field_dict["refreshTokenTtlInDays"] = refresh_token_ttl_in_days
        if always_issue_refresh_token is not UNSET:
            field_dict["alwaysIssueRefreshToken"] = always_issue_refresh_token
        if rotate_refresh_token is not UNSET:
            field_dict["rotateRefreshToken"] = rotate_refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cors_allowed_origins = cast(List[str], d.pop("corsAllowedOrigins", UNSET))

        id_token_ttl = d.pop("idTokenTtl", UNSET)

        refresh_token_ttl = d.pop("refreshTokenTtl", UNSET)

        refresh_token_ttl_in_days = d.pop("refreshTokenTtlInDays", UNSET)

        always_issue_refresh_token = d.pop("alwaysIssueRefreshToken", UNSET)

        rotate_refresh_token = d.pop("rotateRefreshToken", UNSET)

        patch_api_applications_id_response_200_custom_client_metadata = cls(
            cors_allowed_origins=cors_allowed_origins,
            id_token_ttl=id_token_ttl,
            refresh_token_ttl=refresh_token_ttl,
            refresh_token_ttl_in_days=refresh_token_ttl_in_days,
            always_issue_refresh_token=always_issue_refresh_token,
            rotate_refresh_token=rotate_refresh_token,
        )

        patch_api_applications_id_response_200_custom_client_metadata.additional_properties = d
        return patch_api_applications_id_response_200_custom_client_metadata

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
