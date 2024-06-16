from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_users_user_id_password_response_200_sso_identities_item_detail import (
        PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItemDetail,
    )


T = TypeVar("T", bound="PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItem")


@_attrs_define
class PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItem:
    """
    Attributes:
        id (str):
        user_id (str):
        issuer (str):
        identity_id (str):
        detail (PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItemDetail): arbitrary
        created_at (float):
        sso_connector_id (str):
    """

    id: str
    user_id: str
    issuer: str
    identity_id: str
    detail: "PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItemDetail"
    created_at: float
    sso_connector_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        issuer = self.issuer

        identity_id = self.identity_id

        detail = self.detail.to_dict()

        created_at = self.created_at

        sso_connector_id = self.sso_connector_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "issuer": issuer,
                "identityId": identity_id,
                "detail": detail,
                "createdAt": created_at,
                "ssoConnectorId": sso_connector_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_users_user_id_password_response_200_sso_identities_item_detail import (
            PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItemDetail,
        )

        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        issuer = d.pop("issuer")

        identity_id = d.pop("identityId")

        detail = PatchApiUsersUserIdPasswordResponse200SsoIdentitiesItemDetail.from_dict(d.pop("detail"))

        created_at = d.pop("createdAt")

        sso_connector_id = d.pop("ssoConnectorId")

        patch_api_users_user_id_password_response_200_sso_identities_item = cls(
            id=id,
            user_id=user_id,
            issuer=issuer,
            identity_id=identity_id,
            detail=detail,
            created_at=created_at,
            sso_connector_id=sso_connector_id,
        )

        patch_api_users_user_id_password_response_200_sso_identities_item.additional_properties = d
        return patch_api_users_user_id_password_response_200_sso_identities_item

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
