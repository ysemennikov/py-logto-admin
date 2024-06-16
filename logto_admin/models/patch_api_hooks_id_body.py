from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_hooks_id_body_event import PatchApiHooksIdBodyEvent
from ..models.patch_api_hooks_id_body_events_item import PatchApiHooksIdBodyEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_hooks_id_body_config import PatchApiHooksIdBodyConfig


T = TypeVar("T", bound="PatchApiHooksIdBody")


@_attrs_define
class PatchApiHooksIdBody:
    """
    Attributes:
        name (Union[Unset, str]): The updated name of the hook.
        event (Union[Unset, PatchApiHooksIdBodyEvent]): Use `events` instead.
        events (Union[Unset, List[PatchApiHooksIdBodyEventsItem]]): An array of updated hook events.
        config (Union[Unset, PatchApiHooksIdBodyConfig]):
        enabled (Union[Unset, bool]):
        created_at (Union[Unset, float]):
    """

    name: Union[Unset, str] = UNSET
    event: Union[Unset, PatchApiHooksIdBodyEvent] = UNSET
    events: Union[Unset, List[PatchApiHooksIdBodyEventsItem]] = UNSET
    config: Union[Unset, "PatchApiHooksIdBodyConfig"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    created_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        enabled = self.enabled

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if event is not UNSET:
            field_dict["event"] = event
        if events is not UNSET:
            field_dict["events"] = events
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_hooks_id_body_config import PatchApiHooksIdBodyConfig

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, PatchApiHooksIdBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = PatchApiHooksIdBodyEvent(_event)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = PatchApiHooksIdBodyEventsItem(events_item_data)

            events.append(events_item)

        _config = d.pop("config", UNSET)
        config: Union[Unset, PatchApiHooksIdBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PatchApiHooksIdBodyConfig.from_dict(_config)

        enabled = d.pop("enabled", UNSET)

        created_at = d.pop("createdAt", UNSET)

        patch_api_hooks_id_body = cls(
            name=name,
            event=event,
            events=events,
            config=config,
            enabled=enabled,
            created_at=created_at,
        )

        patch_api_hooks_id_body.additional_properties = d
        return patch_api_hooks_id_body

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
