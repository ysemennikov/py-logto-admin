from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_applications_id_body_custom_client_metadata import (
        PatchApiApplicationsIdBodyCustomClientMetadata,
    )
    from ..models.patch_api_applications_id_body_oidc_client_metadata import (
        PatchApiApplicationsIdBodyOidcClientMetadata,
    )
    from ..models.patch_api_applications_id_body_protected_app_metadata import (
        PatchApiApplicationsIdBodyProtectedAppMetadata,
    )


T = TypeVar("T", bound="PatchApiApplicationsIdBody")


@_attrs_define
class PatchApiApplicationsIdBody:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        oidc_client_metadata (Union[Unset, PatchApiApplicationsIdBodyOidcClientMetadata]):
        custom_client_metadata (Union[Unset, PatchApiApplicationsIdBodyCustomClientMetadata]):
        protected_app_metadata (Union[Unset, PatchApiApplicationsIdBodyProtectedAppMetadata]):
        is_admin (Union[Unset, bool]): Whether the application has admin access. User can enable the admin access for
            Machine-to-Machine apps.
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    oidc_client_metadata: Union[Unset, "PatchApiApplicationsIdBodyOidcClientMetadata"] = UNSET
    custom_client_metadata: Union[Unset, "PatchApiApplicationsIdBodyCustomClientMetadata"] = UNSET
    protected_app_metadata: Union[Unset, "PatchApiApplicationsIdBodyProtectedAppMetadata"] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

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

        protected_app_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.protected_app_metadata, Unset):
            protected_app_metadata = self.protected_app_metadata.to_dict()

        is_admin = self.is_admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if oidc_client_metadata is not UNSET:
            field_dict["oidcClientMetadata"] = oidc_client_metadata
        if custom_client_metadata is not UNSET:
            field_dict["customClientMetadata"] = custom_client_metadata
        if protected_app_metadata is not UNSET:
            field_dict["protectedAppMetadata"] = protected_app_metadata
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_applications_id_body_custom_client_metadata import (
            PatchApiApplicationsIdBodyCustomClientMetadata,
        )
        from ..models.patch_api_applications_id_body_oidc_client_metadata import (
            PatchApiApplicationsIdBodyOidcClientMetadata,
        )
        from ..models.patch_api_applications_id_body_protected_app_metadata import (
            PatchApiApplicationsIdBodyProtectedAppMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _oidc_client_metadata = d.pop("oidcClientMetadata", UNSET)
        oidc_client_metadata: Union[Unset, PatchApiApplicationsIdBodyOidcClientMetadata]
        if isinstance(_oidc_client_metadata, Unset):
            oidc_client_metadata = UNSET
        else:
            oidc_client_metadata = PatchApiApplicationsIdBodyOidcClientMetadata.from_dict(_oidc_client_metadata)

        _custom_client_metadata = d.pop("customClientMetadata", UNSET)
        custom_client_metadata: Union[Unset, PatchApiApplicationsIdBodyCustomClientMetadata]
        if isinstance(_custom_client_metadata, Unset):
            custom_client_metadata = UNSET
        else:
            custom_client_metadata = PatchApiApplicationsIdBodyCustomClientMetadata.from_dict(_custom_client_metadata)

        _protected_app_metadata = d.pop("protectedAppMetadata", UNSET)
        protected_app_metadata: Union[Unset, PatchApiApplicationsIdBodyProtectedAppMetadata]
        if isinstance(_protected_app_metadata, Unset):
            protected_app_metadata = UNSET
        else:
            protected_app_metadata = PatchApiApplicationsIdBodyProtectedAppMetadata.from_dict(_protected_app_metadata)

        is_admin = d.pop("isAdmin", UNSET)

        patch_api_applications_id_body = cls(
            name=name,
            description=description,
            oidc_client_metadata=oidc_client_metadata,
            custom_client_metadata=custom_client_metadata,
            protected_app_metadata=protected_app_metadata,
            is_admin=is_admin,
        )

        patch_api_applications_id_body.additional_properties = d
        return patch_api_applications_id_body

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
