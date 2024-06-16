from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_applications_response_200_type import PostApiApplicationsResponse200Type

if TYPE_CHECKING:
    from ..models.post_api_applications_response_200_custom_client_metadata import (
        PostApiApplicationsResponse200CustomClientMetadata,
    )
    from ..models.post_api_applications_response_200_oidc_client_metadata import (
        PostApiApplicationsResponse200OidcClientMetadata,
    )
    from ..models.post_api_applications_response_200_protected_app_metadata_type_0 import (
        PostApiApplicationsResponse200ProtectedAppMetadataType0,
    )


T = TypeVar("T", bound="PostApiApplicationsResponse200")


@_attrs_define
class PostApiApplicationsResponse200:
    """
    Attributes:
        id (str):
        name (str):
        secret (str):
        description (Union[None, str]):
        type (PostApiApplicationsResponse200Type):
        oidc_client_metadata (PostApiApplicationsResponse200OidcClientMetadata):
        custom_client_metadata (PostApiApplicationsResponse200CustomClientMetadata):
        protected_app_metadata (Union['PostApiApplicationsResponse200ProtectedAppMetadataType0', None]):
        is_third_party (bool):
        created_at (float):
    """

    id: str
    name: str
    secret: str
    description: Union[None, str]
    type: PostApiApplicationsResponse200Type
    oidc_client_metadata: "PostApiApplicationsResponse200OidcClientMetadata"
    custom_client_metadata: "PostApiApplicationsResponse200CustomClientMetadata"
    protected_app_metadata: Union["PostApiApplicationsResponse200ProtectedAppMetadataType0", None]
    is_third_party: bool
    created_at: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.post_api_applications_response_200_protected_app_metadata_type_0 import (
            PostApiApplicationsResponse200ProtectedAppMetadataType0,
        )

        id = self.id

        name = self.name

        secret = self.secret

        description: Union[None, str]
        description = self.description

        type = self.type.value

        oidc_client_metadata = self.oidc_client_metadata.to_dict()

        custom_client_metadata = self.custom_client_metadata.to_dict()

        protected_app_metadata: Union[Dict[str, Any], None]
        if isinstance(self.protected_app_metadata, PostApiApplicationsResponse200ProtectedAppMetadataType0):
            protected_app_metadata = self.protected_app_metadata.to_dict()
        else:
            protected_app_metadata = self.protected_app_metadata

        is_third_party = self.is_third_party

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "secret": secret,
                "description": description,
                "type": type,
                "oidcClientMetadata": oidc_client_metadata,
                "customClientMetadata": custom_client_metadata,
                "protectedAppMetadata": protected_app_metadata,
                "isThirdParty": is_third_party,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_applications_response_200_custom_client_metadata import (
            PostApiApplicationsResponse200CustomClientMetadata,
        )
        from ..models.post_api_applications_response_200_oidc_client_metadata import (
            PostApiApplicationsResponse200OidcClientMetadata,
        )
        from ..models.post_api_applications_response_200_protected_app_metadata_type_0 import (
            PostApiApplicationsResponse200ProtectedAppMetadataType0,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        secret = d.pop("secret")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        type = PostApiApplicationsResponse200Type(d.pop("type"))

        oidc_client_metadata = PostApiApplicationsResponse200OidcClientMetadata.from_dict(d.pop("oidcClientMetadata"))

        custom_client_metadata = PostApiApplicationsResponse200CustomClientMetadata.from_dict(
            d.pop("customClientMetadata")
        )

        def _parse_protected_app_metadata(
            data: object,
        ) -> Union["PostApiApplicationsResponse200ProtectedAppMetadataType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                protected_app_metadata_type_0 = PostApiApplicationsResponse200ProtectedAppMetadataType0.from_dict(data)

                return protected_app_metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PostApiApplicationsResponse200ProtectedAppMetadataType0", None], data)

        protected_app_metadata = _parse_protected_app_metadata(d.pop("protectedAppMetadata"))

        is_third_party = d.pop("isThirdParty")

        created_at = d.pop("createdAt")

        post_api_applications_response_200 = cls(
            id=id,
            name=name,
            secret=secret,
            description=description,
            type=type,
            oidc_client_metadata=oidc_client_metadata,
            custom_client_metadata=custom_client_metadata,
            protected_app_metadata=protected_app_metadata,
            is_third_party=is_third_party,
            created_at=created_at,
        )

        post_api_applications_response_200.additional_properties = d
        return post_api_applications_response_200

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
