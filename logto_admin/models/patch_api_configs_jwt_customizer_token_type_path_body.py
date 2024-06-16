from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiConfigsJwtCustomizerTokenTypePathBody")


@_attrs_define
class PatchApiConfigsJwtCustomizerTokenTypePathBody:
    """
    Attributes:
        script (Union[Unset, Any]): The script of the JWT customizer.
        environment_variables (Union[Unset, Any]): The environment variables for the JWT customizer.
        context_sample (Union[Unset, Any]): The sample context for the JWT customizer script testing purpose.
        token_sample (Union[Unset, Any]): The sample raw token payload for the JWT customizer script testing purpose.
    """

    script: Union[Unset, Any] = UNSET
    environment_variables: Union[Unset, Any] = UNSET
    context_sample: Union[Unset, Any] = UNSET
    token_sample: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        script = self.script

        environment_variables = self.environment_variables

        context_sample = self.context_sample

        token_sample = self.token_sample

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if script is not UNSET:
            field_dict["script"] = script
        if environment_variables is not UNSET:
            field_dict["environmentVariables"] = environment_variables
        if context_sample is not UNSET:
            field_dict["contextSample"] = context_sample
        if token_sample is not UNSET:
            field_dict["tokenSample"] = token_sample

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        script = d.pop("script", UNSET)

        environment_variables = d.pop("environmentVariables", UNSET)

        context_sample = d.pop("contextSample", UNSET)

        token_sample = d.pop("tokenSample", UNSET)

        patch_api_configs_jwt_customizer_token_type_path_body = cls(
            script=script,
            environment_variables=environment_variables,
            context_sample=context_sample,
            token_sample=token_sample,
        )

        patch_api_configs_jwt_customizer_token_type_path_body.additional_properties = d
        return patch_api_configs_jwt_customizer_token_type_path_body

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
