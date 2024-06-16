from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_hooks_id_recent_logs_response_200_item_payload_result import (
    GetApiHooksIdRecentLogsResponse200ItemPayloadResult,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_hooks_id_recent_logs_response_200_item_payload_error_type_0 import (
        GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0,
    )


T = TypeVar("T", bound="GetApiHooksIdRecentLogsResponse200ItemPayload")


@_attrs_define
class GetApiHooksIdRecentLogsResponse200ItemPayload:
    """
    Attributes:
        key (str):
        result (GetApiHooksIdRecentLogsResponse200ItemPayloadResult):
        error (Union['GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0', Unset, str]):
        ip (Union[Unset, str]):
        user_agent (Union[Unset, str]):
        user_id (Union[Unset, str]):
        application_id (Union[Unset, str]):
        session_id (Union[Unset, str]):
    """

    key: str
    result: GetApiHooksIdRecentLogsResponse200ItemPayloadResult
    error: Union["GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0", Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    application_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_api_hooks_id_recent_logs_response_200_item_payload_error_type_0 import (
            GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0,
        )

        key = self.key

        result = self.result.value

        error: Union[Dict[str, Any], Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        ip = self.ip

        user_agent = self.user_agent

        user_id = self.user_id

        application_id = self.application_id

        session_id = self.session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "result": result,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if ip is not UNSET:
            field_dict["ip"] = ip
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_hooks_id_recent_logs_response_200_item_payload_error_type_0 import (
            GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0,
        )

        d = src_dict.copy()
        key = d.pop("key")

        result = GetApiHooksIdRecentLogsResponse200ItemPayloadResult(d.pop("result"))

        def _parse_error(data: object) -> Union["GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0.from_dict(data)

                return error_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetApiHooksIdRecentLogsResponse200ItemPayloadErrorType0", Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        ip = d.pop("ip", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        user_id = d.pop("userId", UNSET)

        application_id = d.pop("applicationId", UNSET)

        session_id = d.pop("sessionId", UNSET)

        get_api_hooks_id_recent_logs_response_200_item_payload = cls(
            key=key,
            result=result,
            error=error,
            ip=ip,
            user_agent=user_agent,
            user_id=user_id,
            application_id=application_id,
            session_id=session_id,
        )

        get_api_hooks_id_recent_logs_response_200_item_payload.additional_properties = d
        return get_api_hooks_id_recent_logs_response_200_item_payload

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
