from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user import (
        PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUser,
    )


T = TypeVar("T", bound="PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample")


@_attrs_define
class PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample:
    """
    Attributes:
        user (PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUser):
    """

    user: "PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUser"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample_user import (
            PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUser,
        )

        d = src_dict.copy()
        user = PutApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSampleUser.from_dict(d.pop("user"))

        put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample = cls(
            user=user,
        )

        put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample.additional_properties = d
        return put_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample

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
