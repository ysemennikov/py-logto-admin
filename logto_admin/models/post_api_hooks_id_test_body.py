from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_hooks_id_test_body_events_item import PostApiHooksIdTestBodyEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_hooks_id_test_body_config import PostApiHooksIdTestBodyConfig


T = TypeVar("T", bound="PostApiHooksIdTestBody")


@_attrs_define
class PostApiHooksIdTestBody:
    """
    Attributes:
        events (List[PostApiHooksIdTestBodyEventsItem]): An array of hook events for testing.
        config (PostApiHooksIdTestBodyConfig): The hook configuration for testing.
        event (Union[Unset, Any]): Use `events` instead.
    """

    events: List[PostApiHooksIdTestBodyEventsItem]
    config: "PostApiHooksIdTestBodyConfig"
    event: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        config = self.config.to_dict()

        event = self.event

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "config": config,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_hooks_id_test_body_config import PostApiHooksIdTestBodyConfig

        d = src_dict.copy()
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = PostApiHooksIdTestBodyEventsItem(events_item_data)

            events.append(events_item)

        config = PostApiHooksIdTestBodyConfig.from_dict(d.pop("config"))

        event = d.pop("event", UNSET)

        post_api_hooks_id_test_body = cls(
            events=events,
            config=config,
            event=event,
        )

        post_api_hooks_id_test_body.additional_properties = d
        return post_api_hooks_id_test_body

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
