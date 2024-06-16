from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_connectors_factory_id_test_body_config import PostApiConnectorsFactoryIdTestBodyConfig


T = TypeVar("T", bound="PostApiConnectorsFactoryIdTestBody")


@_attrs_define
class PostApiConnectorsFactoryIdTestBody:
    """
    Attributes:
        config (PostApiConnectorsFactoryIdTestBodyConfig): Connector configuration object for testing.
        phone (Union[Unset, str]): Phone number to send test message to. If this is set, email will be ignored.
        email (Union[Unset, str]): Email address to send test message to. If phone is set, this will be ignored.
    """

    config: "PostApiConnectorsFactoryIdTestBodyConfig"
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config = self.config.to_dict()

        phone = self.phone

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_connectors_factory_id_test_body_config import PostApiConnectorsFactoryIdTestBodyConfig

        d = src_dict.copy()
        config = PostApiConnectorsFactoryIdTestBodyConfig.from_dict(d.pop("config"))

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        post_api_connectors_factory_id_test_body = cls(
            config=config,
            phone=phone,
            email=email,
        )

        post_api_connectors_factory_id_test_body.additional_properties = d
        return post_api_connectors_factory_id_test_body

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
