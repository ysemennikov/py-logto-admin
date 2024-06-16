from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_users_user_id_identities_response_200_additional_property_details import (
        PostApiUsersUserIdIdentitiesResponse200AdditionalPropertyDetails,
    )


T = TypeVar("T", bound="PostApiUsersUserIdIdentitiesResponse200AdditionalProperty")


@_attrs_define
class PostApiUsersUserIdIdentitiesResponse200AdditionalProperty:
    """
    Attributes:
        user_id (str):
        details (Union[Unset, PostApiUsersUserIdIdentitiesResponse200AdditionalPropertyDetails]): arbitrary
    """

    user_id: str
    details: Union[Unset, "PostApiUsersUserIdIdentitiesResponse200AdditionalPropertyDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_users_user_id_identities_response_200_additional_property_details import (
            PostApiUsersUserIdIdentitiesResponse200AdditionalPropertyDetails,
        )

        d = src_dict.copy()
        user_id = d.pop("userId")

        _details = d.pop("details", UNSET)
        details: Union[Unset, PostApiUsersUserIdIdentitiesResponse200AdditionalPropertyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PostApiUsersUserIdIdentitiesResponse200AdditionalPropertyDetails.from_dict(_details)

        post_api_users_user_id_identities_response_200_additional_property = cls(
            user_id=user_id,
            details=details,
        )

        post_api_users_user_id_identities_response_200_additional_property.additional_properties = d
        return post_api_users_user_id_identities_response_200_additional_property

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
