from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item_detail import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItemDetail,
    )


T = TypeVar("T", bound="PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem")


@_attrs_define
class PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItem:
    """
    Attributes:
        issuer (str):
        identity_id (str):
        detail (PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItemDetail): arbitrary
    """

    issuer: str
    identity_id: str
    detail: "PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItemDetail"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer = self.issuer

        identity_id = self.identity_id

        detail = self.detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuer": issuer,
                "identityId": identity_id,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item_detail import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItemDetail,
        )

        d = src_dict.copy()
        issuer = d.pop("issuer")

        identity_id = d.pop("identityId")

        detail = PostApiConfigsJwtCustomizerTestBodyType0ContextUserSsoIdentitiesItemDetail.from_dict(d.pop("detail"))

        post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item = cls(
            issuer=issuer,
            identity_id=identity_id,
            detail=detail,
        )

        post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item.additional_properties = d
        return post_api_configs_jwt_customizer_test_body_type_0_context_user_sso_identities_item

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
