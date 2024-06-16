from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_applications_body_type import PostApiApplicationsBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_applications_body_custom_client_metadata import PostApiApplicationsBodyCustomClientMetadata
    from ..models.post_api_applications_body_oidc_client_metadata import PostApiApplicationsBodyOidcClientMetadata
    from ..models.post_api_applications_body_protected_app_metadata import PostApiApplicationsBodyProtectedAppMetadata


T = TypeVar("T", bound="PostApiApplicationsBody")


@_attrs_define
class PostApiApplicationsBody:
    """
    Attributes:
        name (str):
        type (PostApiApplicationsBodyType):
        description (Union[None, Unset, str]):
        oidc_client_metadata (Union[Unset, PostApiApplicationsBodyOidcClientMetadata]):
        custom_client_metadata (Union[Unset, PostApiApplicationsBodyCustomClientMetadata]):
        is_third_party (Union[Unset, bool]):
        protected_app_metadata (Union[Unset, PostApiApplicationsBodyProtectedAppMetadata]): The data for protected app,
            this feature is not available for open source version.
    """

    name: str
    type: PostApiApplicationsBodyType
    description: Union[None, Unset, str] = UNSET
    oidc_client_metadata: Union[Unset, "PostApiApplicationsBodyOidcClientMetadata"] = UNSET
    custom_client_metadata: Union[Unset, "PostApiApplicationsBodyCustomClientMetadata"] = UNSET
    is_third_party: Union[Unset, bool] = UNSET
    protected_app_metadata: Union[Unset, "PostApiApplicationsBodyProtectedAppMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type = self.type.value

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        oidc_client_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oidc_client_metadata, Unset):
            oidc_client_metadata = self.oidc_client_metadata.to_dict()

        custom_client_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_client_metadata, Unset):
            custom_client_metadata = self.custom_client_metadata.to_dict()

        is_third_party = self.is_third_party

        protected_app_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.protected_app_metadata, Unset):
            protected_app_metadata = self.protected_app_metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if oidc_client_metadata is not UNSET:
            field_dict["oidcClientMetadata"] = oidc_client_metadata
        if custom_client_metadata is not UNSET:
            field_dict["customClientMetadata"] = custom_client_metadata
        if is_third_party is not UNSET:
            field_dict["isThirdParty"] = is_third_party
        if protected_app_metadata is not UNSET:
            field_dict["protectedAppMetadata"] = protected_app_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_applications_body_custom_client_metadata import (
            PostApiApplicationsBodyCustomClientMetadata,
        )
        from ..models.post_api_applications_body_oidc_client_metadata import PostApiApplicationsBodyOidcClientMetadata
        from ..models.post_api_applications_body_protected_app_metadata import (
            PostApiApplicationsBodyProtectedAppMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name")

        type = PostApiApplicationsBodyType(d.pop("type"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _oidc_client_metadata = d.pop("oidcClientMetadata", UNSET)
        oidc_client_metadata: Union[Unset, PostApiApplicationsBodyOidcClientMetadata]
        if isinstance(_oidc_client_metadata, Unset):
            oidc_client_metadata = UNSET
        else:
            oidc_client_metadata = PostApiApplicationsBodyOidcClientMetadata.from_dict(_oidc_client_metadata)

        _custom_client_metadata = d.pop("customClientMetadata", UNSET)
        custom_client_metadata: Union[Unset, PostApiApplicationsBodyCustomClientMetadata]
        if isinstance(_custom_client_metadata, Unset):
            custom_client_metadata = UNSET
        else:
            custom_client_metadata = PostApiApplicationsBodyCustomClientMetadata.from_dict(_custom_client_metadata)

        is_third_party = d.pop("isThirdParty", UNSET)

        _protected_app_metadata = d.pop("protectedAppMetadata", UNSET)
        protected_app_metadata: Union[Unset, PostApiApplicationsBodyProtectedAppMetadata]
        if isinstance(_protected_app_metadata, Unset):
            protected_app_metadata = UNSET
        else:
            protected_app_metadata = PostApiApplicationsBodyProtectedAppMetadata.from_dict(_protected_app_metadata)

        post_api_applications_body = cls(
            name=name,
            type=type,
            description=description,
            oidc_client_metadata=oidc_client_metadata,
            custom_client_metadata=custom_client_metadata,
            is_third_party=is_third_party,
            protected_app_metadata=protected_app_metadata,
        )

        post_api_applications_body.additional_properties = d
        return post_api_applications_body

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
