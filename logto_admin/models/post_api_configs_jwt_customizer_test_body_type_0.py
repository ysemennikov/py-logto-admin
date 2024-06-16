from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_context import (
        PostApiConfigsJwtCustomizerTestBodyType0Context,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_environment_variables import (
        PostApiConfigsJwtCustomizerTestBodyType0EnvironmentVariables,
    )
    from ..models.post_api_configs_jwt_customizer_test_body_type_0_token import (
        PostApiConfigsJwtCustomizerTestBodyType0Token,
    )


T = TypeVar("T", bound="PostApiConfigsJwtCustomizerTestBodyType0")


@_attrs_define
class PostApiConfigsJwtCustomizerTestBodyType0:
    """
    Attributes:
        token_type (str):
        script (str):
        token (PostApiConfigsJwtCustomizerTestBodyType0Token):
        context (PostApiConfigsJwtCustomizerTestBodyType0Context):
        environment_variables (Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0EnvironmentVariables]):
    """

    token_type: str
    script: str
    token: "PostApiConfigsJwtCustomizerTestBodyType0Token"
    context: "PostApiConfigsJwtCustomizerTestBodyType0Context"
    environment_variables: Union[Unset, "PostApiConfigsJwtCustomizerTestBodyType0EnvironmentVariables"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_type = self.token_type

        script = self.script

        token = self.token.to_dict()

        context = self.context.to_dict()

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
                "context": context,
            }
        )
        if environment_variables is not UNSET:
            field_dict["environmentVariables"] = environment_variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_context import (
            PostApiConfigsJwtCustomizerTestBodyType0Context,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_environment_variables import (
            PostApiConfigsJwtCustomizerTestBodyType0EnvironmentVariables,
        )
        from ..models.post_api_configs_jwt_customizer_test_body_type_0_token import (
            PostApiConfigsJwtCustomizerTestBodyType0Token,
        )

        d = src_dict.copy()
        token_type = d.pop("tokenType")

        script = d.pop("script")

        token = PostApiConfigsJwtCustomizerTestBodyType0Token.from_dict(d.pop("token"))

        context = PostApiConfigsJwtCustomizerTestBodyType0Context.from_dict(d.pop("context"))

        _environment_variables = d.pop("environmentVariables", UNSET)
        environment_variables: Union[Unset, PostApiConfigsJwtCustomizerTestBodyType0EnvironmentVariables]
        if isinstance(_environment_variables, Unset):
            environment_variables = UNSET
        else:
            environment_variables = PostApiConfigsJwtCustomizerTestBodyType0EnvironmentVariables.from_dict(
                _environment_variables
            )

        post_api_configs_jwt_customizer_test_body_type_0 = cls(
            token_type=token_type,
            script=script,
            token=token,
            context=context,
            environment_variables=environment_variables,
        )

        post_api_configs_jwt_customizer_test_body_type_0.additional_properties = d
        return post_api_configs_jwt_customizer_test_body_type_0

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
