from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item_detail import (
        GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItemDetail,
    )


T = TypeVar("T", bound="GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem")


@_attrs_define
class GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItem:
    """
    Attributes:
        issuer (str):
        identity_id (str):
        detail (GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItemDetail): arbitrary
    """

    issuer: str
    identity_id: str
    detail: "GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItemDetail"
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
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item_detail import (
            GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItemDetail,
        )

        d = src_dict.copy()
        issuer = d.pop("issuer")

        identity_id = d.pop("identityId")

        detail = GetApiConfigsJwtCustomizerResponse200ItemType0ValueContextSampleUserSsoIdentitiesItemDetail.from_dict(
            d.pop("detail")
        )

        get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item = cls(
            issuer=issuer,
            identity_id=identity_id,
            detail=detail,
        )

        get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item.additional_properties = d
        return get_api_configs_jwt_customizer_response_200_item_type_0_value_context_sample_user_sso_identities_item

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
