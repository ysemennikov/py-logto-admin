from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user import (
        PostApiConfigsJwtCustomizerTestBodyType0ContextUser,
    )


T = TypeVar("T", bound="PostApiConfigsJwtCustomizerTestBodyType0Context")


@_attrs_define
class PostApiConfigsJwtCustomizerTestBodyType0Context:
    """
    Attributes:
        user (PostApiConfigsJwtCustomizerTestBodyType0ContextUser):
    """

    user: "PostApiConfigsJwtCustomizerTestBodyType0ContextUser"
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
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context_user import (
            PostApiConfigsJwtCustomizerTestBodyType0ContextUser,
        )

        d = src_dict.copy()
        user = PostApiConfigsJwtCustomizerTestBodyType0ContextUser.from_dict(d.pop("user"))

        post_api_configs_jwt_customizer_test_body_type_0_context = cls(
            user=user,
        )

        post_api_configs_jwt_customizer_test_body_type_0_context.additional_properties = d
        return post_api_configs_jwt_customizer_test_body_type_0_context

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
