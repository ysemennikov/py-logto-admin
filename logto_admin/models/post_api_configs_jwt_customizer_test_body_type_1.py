from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_configs_jwt_customizer_test_body_type_1_environment_variables import (
        PostApiConfigsJwtCustomizerTestBodyType1EnvironmentVariables,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_1_token import (
        PostApiConfigsJwtCustomizerTestBodyType1Token,
    )


T = TypeVar("T", bound="PostApiConfigsJwtCustomizerTestBodyType1")


@_attrs_define
class PostApiConfigsJwtCustomizerTestBodyType1:
    """
    Attributes:
        token_type (str):
        script (str):
        token (PostApiConfigsJwtCustomizerTestBodyType1Token):
        environment_variables (Union[Unset, PostApiConfigsJwtCustomizerTestBodyType1EnvironmentVariables]):
    """

    token_type: str
    script: str
    token: "PostApiConfigsJwtCustomizerTestBodyType1Token"
    environment_variables: Union[Unset, "PostApiConfigsJwtCustomizerTestBodyType1EnvironmentVariables"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_type = self.token_type

        script = self.script

        token = self.token.to_dict()

        environment_variables: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.environment_variables, Unset):
            environment_variables = self.environment_variables.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenType": token_type,
                "script": script,
                "token": token,
            }
        )
        if environment_variables is not UNSET:
            field_dict["environmentVariables"] = environment_variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_configs_jwt_customizer_test_body_type_1_environment_variables import (
            PostApiConfigsJwtCustomizerTestBodyType1EnvironmentVariables,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_1_token import (
            PostApiConfigsJwtCustomizerTestBodyType1Token,
        )

        d = src_dict.copy()
        token_type = d.pop("tokenType")

        script = d.pop("script")

        token = PostApiConfigsJwtCustomizerTestBodyType1Token.from_dict(d.pop("token"))

        _environment_variables = d.pop("environmentVariables", UNSET)
        environment_variables: Union[Unset, PostApiConfigsJwtCustomizerTestBodyType1EnvironmentVariables]
        if isinstance(_environment_variables, Unset):
            environment_variables = UNSET
        else:
            environment_variables = PostApiConfigsJwtCustomizerTestBodyType1EnvironmentVariables.from_dict(
                _environment_variables
            )

        post_api_configs_jwt_customizer_test_body_type_1 = cls(
            token_type=token_type,
            script=script,
            token=token,
            environment_variables=environment_variables,
        )

        post_api_configs_jwt_customizer_test_body_type_1.additional_properties = d
        return post_api_configs_jwt_customizer_test_body_type_1

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
