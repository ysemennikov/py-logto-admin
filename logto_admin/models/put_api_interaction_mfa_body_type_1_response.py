from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiInteractionMfaBodyType1Response")


@_attrs_define
class PutApiInteractionMfaBodyType1Response:
    """
    Attributes:
        client_data_json (str):
        authenticator_data (str):
        signature (str):
        user_handle (Union[Unset, str]):
    """

    client_data_json: str
    authenticator_data: str
    signature: str
    user_handle: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_data_json = self.client_data_json

        authenticator_data = self.authenticator_data

        signature = self.signature

        user_handle = self.user_handle

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientDataJSON": client_data_json,
                "authenticatorData": authenticator_data,
                "signature": signature,
            }
        )
        if user_handle is not UNSET:
            field_dict["userHandle"] = user_handle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_data_json = d.pop("clientDataJSON")

        authenticator_data = d.pop("authenticatorData")

        signature = d.pop("signature")

        user_handle = d.pop("userHandle", UNSET)

        put_api_interaction_mfa_body_type_1_response = cls(
            client_data_json=client_data_json,
            authenticator_data=authenticator_data,
            signature=signature,
            user_handle=user_handle,
        )

        put_api_interaction_mfa_body_type_1_response.additional_properties = d
        return put_api_interaction_mfa_body_type_1_response

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
