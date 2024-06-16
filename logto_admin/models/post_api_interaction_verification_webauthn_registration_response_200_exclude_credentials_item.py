from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_interaction_verification_webauthn_registration_response_200_exclude_credentials_item_transports_item import (
    PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItemTransportsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem")


@_attrs_define
class PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItem:
    """
    Attributes:
        type (str):
        id (str):
        transports (Union[Unset,
            List[PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItemTransportsItem]]):
    """

    type: str
    id: str
    transports: Union[
        Unset, List[PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItemTransportsItem]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id = self.id

        transports: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transports, Unset):
            transports = []
            for transports_item_data in self.transports:
                transports_item = transports_item_data.value
                transports.append(transports_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
            }
        )
        if transports is not UNSET:
            field_dict["transports"] = transports

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id")

        transports = []
        _transports = d.pop("transports", UNSET)
        for transports_item_data in _transports or []:
            transports_item = (
                PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItemTransportsItem(
                    transports_item_data
                )
            )

            transports.append(transports_item)

        post_api_interaction_verification_webauthn_registration_response_200_exclude_credentials_item = cls(
            type=type,
            id=id,
            transports=transports,
        )

        post_api_interaction_verification_webauthn_registration_response_200_exclude_credentials_item.additional_properties = d
        return post_api_interaction_verification_webauthn_registration_response_200_exclude_credentials_item

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
