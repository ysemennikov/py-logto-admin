from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1TokenSample")


@_attrs_define
class GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1TokenSample:
    """
    Attributes:
        jti (Union[Unset, str]):
        aud (Union[List[str], Unset, str]):
        scope (Union[Unset, str]):
        client_id (Union[Unset, str]):
        kind (Union[Unset, str]):
    """

    jti: Union[Unset, str] = UNSET
    aud: Union[List[str], Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jti = self.jti

        aud: Union[List[str], Unset, str]
        if isinstance(self.aud, Unset):
            aud = UNSET
        elif isinstance(self.aud, list):
            aud = self.aud

        else:
            aud = self.aud

        scope = self.scope

        client_id = self.client_id

        kind = self.kind

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jti is not UNSET:
            field_dict["jti"] = jti
        if aud is not UNSET:
            field_dict["aud"] = aud
        if scope is not UNSET:
            field_dict["scope"] = scope
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        jti = d.pop("jti", UNSET)

        def _parse_aud(data: object) -> Union[List[str], Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aud_type_1 = cast(List[str], data)

                return aud_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[str], Unset, str], data)

        aud = _parse_aud(d.pop("aud", UNSET))

        scope = d.pop("scope", UNSET)

        client_id = d.pop("clientId", UNSET)

        kind = d.pop("kind", UNSET)

        get_api_configs_jwt_customizer_token_type_path_response_200_type_1_token_sample = cls(
            jti=jti,
            aud=aud,
            scope=scope,
            client_id=client_id,
            kind=kind,
        )

        get_api_configs_jwt_customizer_token_type_path_response_200_type_1_token_sample.additional_properties = d
        return get_api_configs_jwt_customizer_token_type_path_response_200_type_1_token_sample

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
