from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_identities_additional_property import (
        PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentitiesAdditionalProperty,
    )


T = TypeVar("T", bound="PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentities")


@_attrs_define
class PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentities:
    """ """

    additional_properties: Dict[
        str, "PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentitiesAdditionalProperty"
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_identities_additional_property import (
            PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentitiesAdditionalProperty,
        )

        d = src_dict.copy()
        put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_identities = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentitiesAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_identities.additional_properties = additional_properties
        return put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user_identities

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> "PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentitiesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: "PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUserIdentitiesAdditionalProperty",
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
