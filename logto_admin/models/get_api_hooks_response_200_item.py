from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_hooks_response_200_item_event import GetApiHooksResponse200ItemEvent
from ..models.get_api_hooks_response_200_item_events_item import GetApiHooksResponse200ItemEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_hooks_response_200_item_config import GetApiHooksResponse200ItemConfig
    from ..models.get_api_hooks_response_200_item_execution_stats import GetApiHooksResponse200ItemExecutionStats


T = TypeVar("T", bound="GetApiHooksResponse200Item")


@_attrs_define
class GetApiHooksResponse200Item:
    """
    Attributes:
        id (str):
        name (str):
        event (GetApiHooksResponse200ItemEvent):
        events (List[GetApiHooksResponse200ItemEventsItem]):
        config (GetApiHooksResponse200ItemConfig):
        signing_key (str):
        enabled (bool):
        created_at (float):
        execution_stats (Union[Unset, GetApiHooksResponse200ItemExecutionStats]):
    """

    id: str
    name: str
    event: GetApiHooksResponse200ItemEvent
    events: List[GetApiHooksResponse200ItemEventsItem]
    config: "GetApiHooksResponse200ItemConfig"
    signing_key: str
    enabled: bool
    created_at: float
    execution_stats: Union[Unset, "GetApiHooksResponse200ItemExecutionStats"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        event = self.event.value

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        config = self.config.to_dict()

        signing_key = self.signing_key

        enabled = self.enabled

        created_at = self.created_at

        execution_stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_stats, Unset):
            execution_stats = self.execution_stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "event": event,
                "events": events,
                "config": config,
                "signingKey": signing_key,
                "enabled": enabled,
                "createdAt": created_at,
            }
        )
        if execution_stats is not UNSET:
            field_dict["executionStats"] = execution_stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_api_hooks_response_200_item_config import GetApiHooksResponse200ItemConfig
        from ..models.get_api_hooks_response_200_item_execution_stats import GetApiHooksResponse200ItemExecutionStats

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        event = GetApiHooksResponse200ItemEvent(d.pop("event"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = GetApiHooksResponse200ItemEventsItem(events_item_data)

            events.append(events_item)

        config = GetApiHooksResponse200ItemConfig.from_dict(d.pop("config"))

        signing_key = d.pop("signingKey")

        enabled = d.pop("enabled")

        created_at = d.pop("createdAt")

        _execution_stats = d.pop("executionStats", UNSET)
        execution_stats: Union[Unset, GetApiHooksResponse200ItemExecutionStats]
        if isinstance(_execution_stats, Unset):
            execution_stats = UNSET
        else:
            execution_stats = GetApiHooksResponse200ItemExecutionStats.from_dict(_execution_stats)

        get_api_hooks_response_200_item = cls(
            id=id,
            name=name,
            event=event,
            events=events,
            config=config,
            signing_key=signing_key,
            enabled=enabled,
            created_at=created_at,
            execution_stats=execution_stats,
        )

        get_api_hooks_response_200_item.additional_properties = d
        return get_api_hooks_response_200_item

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
