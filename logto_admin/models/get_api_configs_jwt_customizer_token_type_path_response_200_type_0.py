from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample import (
        GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample,
    )
    from ..models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0_environment_variables import (
        GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0EnvironmentVariables,
    )
    from ..models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0_token_sample import (
        GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0TokenSample,
    )


T = TypeVar("T", bound="GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0")


@_attrs_define
class GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0:
    """
    Attributes:
        script (str):
        environment_variables (Union[Unset,
            GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0EnvironmentVariables]):
        context_sample (Union[Unset, GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample]):
        token_sample (Union[Unset, GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0TokenSample]):
    """

    script: str
    environment_variables: Union[
        Unset, "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0EnvironmentVariables"
    ] = UNSET
    context_sample: Union[Unset, "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample"] = UNSET
    token_sample: Union[Unset, "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0TokenSample"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        script = self.script

        environment_variables: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.environment_variables, Unset):
            environment_variables = self.environment_variables.to_dict()

        context_sample: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context_sample, Unset):
            context_sample = self.context_sample.to_dict()

        token_sample: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token_sample, Unset):
            token_sample = self.token_sample.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "script": script,
            }
        )
        if environment_variables is not UNSET:
            field_dict["environmentVariables"] = environment_variables
        if context_sample is not UNSET:
            field_dict["contextSample"] = context_sample
        if token_sample is not UNSET:
            field_dict["tokenSample"] = token_sample

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0_context_sample import (
            GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample,
        )
        from ..models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0_environment_variables import (
            GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0EnvironmentVariables,
        )
        from ..models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0_token_sample import (
            GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0TokenSample,
        )

        d = src_dict.copy()
        script = d.pop("script")

        _environment_variables = d.pop("environmentVariables", UNSET)
        environment_variables: Union[Unset, GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0EnvironmentVariables]
        if isinstance(_environment_variables, Unset):
            environment_variables = UNSET
        else:
            environment_variables = (
                GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0EnvironmentVariables.from_dict(
                    _environment_variables
                )
            )

        _context_sample = d.pop("contextSample", UNSET)
        context_sample: Union[Unset, GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample]
        if isinstance(_context_sample, Unset):
            context_sample = UNSET
        else:
            context_sample = GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0ContextSample.from_dict(
                _context_sample
            )

        _token_sample = d.pop("tokenSample", UNSET)
        token_sample: Union[Unset, GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0TokenSample]
        if isinstance(_token_sample, Unset):
            token_sample = UNSET
        else:
            token_sample = GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0TokenSample.from_dict(_token_sample)

        get_api_configs_jwt_customizer_token_type_path_response_200_type_0 = cls(
            script=script,
            environment_variables=environment_variables,
            context_sample=context_sample,
            token_sample=token_sample,
        )

        get_api_configs_jwt_customizer_token_type_path_response_200_type_0.additional_properties = d
        return get_api_configs_jwt_customizer_token_type_path_response_200_type_0

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
