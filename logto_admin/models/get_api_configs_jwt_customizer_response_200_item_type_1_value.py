from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value_context_sample import (
        GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value_environment_variables import (
        GetApiConfigsJwtCustomizerResponse200ItemType1ValueEnvironmentVariables,
    )
    from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value_token_sample import (
        GetApiConfigsJwtCustomizerResponse200ItemType1ValueTokenSample,
    )


T = TypeVar("T", bound="GetApiConfigsJwtCustomizerResponse200ItemType1Value")


@_attrs_define
class GetApiConfigsJwtCustomizerResponse200ItemType1Value:
    """
    Attributes:
        script (str):
        environment_variables (Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType1ValueEnvironmentVariables]):
        context_sample (Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample]): arbitrary
        token_sample (Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType1ValueTokenSample]):
    """

    script: str
    environment_variables: Union[Unset, "GetApiConfigsJwtCustomizerResponse200ItemType1ValueEnvironmentVariables"] = (
        UNSET
    )
    context_sample: Union[Unset, "GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample"] = UNSET
    token_sample: Union[Unset, "GetApiConfigsJwtCustomizerResponse200ItemType1ValueTokenSample"] = UNSET
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
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value_context_sample import (
            GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value_environment_variables import (
            GetApiConfigsJwtCustomizerResponse200ItemType1ValueEnvironmentVariables,
        )
        from ..models.get_api_configs_jwt_customizer_response_200_item_type_1_value_token_sample import (
            GetApiConfigsJwtCustomizerResponse200ItemType1ValueTokenSample,
        )

        d = src_dict.copy()
        script = d.pop("script")

        _environment_variables = d.pop("environmentVariables", UNSET)
        environment_variables: Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType1ValueEnvironmentVariables]
        if isinstance(_environment_variables, Unset):
            environment_variables = UNSET
        else:
            environment_variables = GetApiConfigsJwtCustomizerResponse200ItemType1ValueEnvironmentVariables.from_dict(
                _environment_variables
            )

        _context_sample = d.pop("contextSample", UNSET)
        context_sample: Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample]
        if isinstance(_context_sample, Unset):
            context_sample = UNSET
        else:
            context_sample = GetApiConfigsJwtCustomizerResponse200ItemType1ValueContextSample.from_dict(_context_sample)

        _token_sample = d.pop("tokenSample", UNSET)
        token_sample: Union[Unset, GetApiConfigsJwtCustomizerResponse200ItemType1ValueTokenSample]
        if isinstance(_token_sample, Unset):
            token_sample = UNSET
        else:
            token_sample = GetApiConfigsJwtCustomizerResponse200ItemType1ValueTokenSample.from_dict(_token_sample)

        get_api_configs_jwt_customizer_response_200_item_type_1_value = cls(
            script=script,
            environment_variables=environment_variables,
            context_sample=context_sample,
            token_sample=token_sample,
        )

        get_api_configs_jwt_customizer_response_200_item_type_1_value.additional_properties = d
        return get_api_configs_jwt_customizer_response_200_item_type_1_value

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
