from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_hooks_body_event import PostApiHooksBodyEvent
from ..models.post_api_hooks_body_events_item import PostApiHooksBodyEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_hooks_body_config import PostApiHooksBodyConfig


T = TypeVar("T", bound="PostApiHooksBody")


@_attrs_define
class PostApiHooksBody:
    """
    Attributes:
        config (PostApiHooksBodyConfig):
        name (Union[Unset, str]): The name of the hook.
        event (Union[Unset, PostApiHooksBodyEvent]): Use `events` instead.
        events (Union[Unset, List[PostApiHooksBodyEventsItem]]): An array of hook events.
        enabled (Union[Unset, bool]):
        created_at (Union[Unset, float]):
    """

    config: "PostApiHooksBodyConfig"
    name: Union[Unset, str] = UNSET
    event: Union[Unset, PostApiHooksBodyEvent] = UNSET
    events: Union[Unset, List[PostApiHooksBodyEventsItem]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    created_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config = self.config.to_dict()

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

        enabled = self.enabled

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if event is not UNSET:
            field_dict["event"] = event
        if events is not UNSET:
            field_dict["events"] = events
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_hooks_body_config import PostApiHooksBodyConfig

        d = src_dict.copy()
        config = PostApiHooksBodyConfig.from_dict(d.pop("config"))

        name = d.pop("name", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, PostApiHooksBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = PostApiHooksBodyEvent(_event)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = PostApiHooksBodyEventsItem(events_item_data)

            events.append(events_item)

        enabled = d.pop("enabled", UNSET)

        created_at = d.pop("createdAt", UNSET)

        post_api_hooks_body = cls(
            config=config,
            name=name,
            event=event,
            events=events,
            enabled=enabled,
            created_at=created_at,
        )

        post_api_hooks_body.additional_properties = d
        return post_api_hooks_body

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
