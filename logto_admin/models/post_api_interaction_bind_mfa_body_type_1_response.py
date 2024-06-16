from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_interaction_bind_mfa_body_type_1_response_transports_item import (
    PostApiInteractionBindMfaBodyType1ResponseTransportsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiInteractionBindMfaBodyType1Response")


@_attrs_define
class PostApiInteractionBindMfaBodyType1Response:
    """
    Attributes:
        client_data_json (str):
        attestation_object (str):
        authenticator_data (Union[Unset, str]):
        transports (Union[Unset, List[PostApiInteractionBindMfaBodyType1ResponseTransportsItem]]):
        public_key_algorithm (Union[Unset, float]):
        public_key (Union[Unset, str]):
    """

    client_data_json: str
    attestation_object: str
    authenticator_data: Union[Unset, str] = UNSET
    transports: Union[Unset, List[PostApiInteractionBindMfaBodyType1ResponseTransportsItem]] = UNSET
    public_key_algorithm: Union[Unset, float] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_data_json = self.client_data_json

        attestation_object = self.attestation_object

        authenticator_data = self.authenticator_data

        transports: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transports, Unset):
            transports = []
            for transports_item_data in self.transports:
                transports_item = transports_item_data.value
                transports.append(transports_item)

        public_key_algorithm = self.public_key_algorithm

        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientDataJSON": client_data_json,
                "attestationObject": attestation_object,
            }
        )
        if authenticator_data is not UNSET:
            field_dict["authenticatorData"] = authenticator_data
        if transports is not UNSET:
            field_dict["transports"] = transports
        if public_key_algorithm is not UNSET:
            field_dict["publicKeyAlgorithm"] = public_key_algorithm
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_data_json = d.pop("clientDataJSON")

        attestation_object = d.pop("attestationObject")

        authenticator_data = d.pop("authenticatorData", UNSET)

        transports = []
        _transports = d.pop("transports", UNSET)
        for transports_item_data in _transports or []:
            transports_item = PostApiInteractionBindMfaBodyType1ResponseTransportsItem(transports_item_data)

            transports.append(transports_item)

        public_key_algorithm = d.pop("publicKeyAlgorithm", UNSET)

        public_key = d.pop("publicKey", UNSET)

        post_api_interaction_bind_mfa_body_type_1_response = cls(
            client_data_json=client_data_json,
            attestation_object=attestation_object,
            authenticator_data=authenticator_data,
            transports=transports,
            public_key_algorithm=public_key_algorithm,
            public_key=public_key,
        )

        post_api_interaction_bind_mfa_body_type_1_response.additional_properties = d
        return post_api_interaction_bind_mfa_body_type_1_response

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
