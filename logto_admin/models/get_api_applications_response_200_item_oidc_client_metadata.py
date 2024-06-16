from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_applications_response_200_item_oidc_client_metadata_redirect_uris_item_type_0 import (
        GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0,
    )
    from ..models.get_api_applications_response_200_item_oidc_client_metadata_redirect_uris_item_type_1 import (
        GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType1,
    )


T = TypeVar("T", bound="GetApiApplicationsResponse200ItemOidcClientMetadata")


@_attrs_define
class GetApiApplicationsResponse200ItemOidcClientMetadata:
    """
    Attributes:
        redirect_uris (List[Union['GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0',
            'GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType1']]):
        post_logout_redirect_uris (List[str]):
        logo_uri (Union[Unset, str]):
    """

    redirect_uris: List[
        Union[
            "GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0",
            "GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType1",
        ]
    ]
    post_logout_redirect_uris: List[str]
    logo_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_applications_response_200_item_oidc_client_metadata_redirect_uris_item_type_0 import (
            GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0,
        )

        redirect_uris = []
        for redirect_uris_item_data in self.redirect_uris:
            redirect_uris_item: Dict[str, Any]
            if isinstance(
                redirect_uris_item_data, GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0
            ):
                redirect_uris_item = redirect_uris_item_data.to_dict()
            else:
                redirect_uris_item = redirect_uris_item_data.to_dict()

            redirect_uris.append(redirect_uris_item)

        post_logout_redirect_uris = self.post_logout_redirect_uris

        logo_uri = self.logo_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redirectUris": redirect_uris,
                "postLogoutRedirectUris": post_logout_redirect_uris,
            }
        )
        if logo_uri is not UNSET:
            field_dict["logoUri"] = logo_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_applications_response_200_item_oidc_client_metadata_redirect_uris_item_type_0 import (
            GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0,
        )
        from ..models.get_api_applications_response_200_item_oidc_client_metadata_redirect_uris_item_type_1 import (
            GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType1,
        )

        d = src_dict.copy()
        redirect_uris = []
        _redirect_uris = d.pop("redirectUris")
        for redirect_uris_item_data in _redirect_uris:

            def _parse_redirect_uris_item(
                data: object,
            ) -> Union[
                "GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0",
                "GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    redirect_uris_item_type_0 = (
                        GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType0.from_dict(data)
                    )

                    return redirect_uris_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                redirect_uris_item_type_1 = (
                    GetApiApplicationsResponse200ItemOidcClientMetadataRedirectUrisItemType1.from_dict(data)
                )

                return redirect_uris_item_type_1

            redirect_uris_item = _parse_redirect_uris_item(redirect_uris_item_data)

            redirect_uris.append(redirect_uris_item)

        post_logout_redirect_uris = cast(List[str], d.pop("postLogoutRedirectUris"))

        logo_uri = d.pop("logoUri", UNSET)

        get_api_applications_response_200_item_oidc_client_metadata = cls(
            redirect_uris=redirect_uris,
            post_logout_redirect_uris=post_logout_redirect_uris,
            logo_uri=logo_uri,
        )

        get_api_applications_response_200_item_oidc_client_metadata.additional_properties = d
        return get_api_applications_response_200_item_oidc_client_metadata

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
