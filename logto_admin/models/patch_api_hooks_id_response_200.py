from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_hooks_id_response_200_event import PatchApiHooksIdResponse200Event
from ..models.patch_api_hooks_id_response_200_events_item import PatchApiHooksIdResponse200EventsItem

if TYPE_CHECKING:
    from ..models.patch_api_hooks_id_response_200_config import PatchApiHooksIdResponse200Config


T = TypeVar("T", bound="PatchApiHooksIdResponse200")


@_attrs_define
class PatchApiHooksIdResponse200:
    """
    Attributes:
        id (str):
        name (str):
        event (PatchApiHooksIdResponse200Event):
        events (List[PatchApiHooksIdResponse200EventsItem]):
        config (PatchApiHooksIdResponse200Config):
        signing_key (str):
        enabled (bool):
        created_at (float):
    """

    id: str
    name: str
    event: PatchApiHooksIdResponse200Event
    events: List[PatchApiHooksIdResponse200EventsItem]
    config: "PatchApiHooksIdResponse200Config"
    signing_key: str
    enabled: bool
    created_at: float
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_hooks_id_response_200_config import PatchApiHooksIdResponse200Config

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        event = PatchApiHooksIdResponse200Event(d.pop("event"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = PatchApiHooksIdResponse200EventsItem(events_item_data)

            events.append(events_item)

        config = PatchApiHooksIdResponse200Config.from_dict(d.pop("config"))

        signing_key = d.pop("signingKey")

        enabled = d.pop("enabled")

        created_at = d.pop("createdAt")

        patch_api_hooks_id_response_200 = cls(
            id=id,
            name=name,
            event=event,
            events=events,
            config=config,
            signing_key=signing_key,
            enabled=enabled,
            created_at=created_at,
        )

        patch_api_hooks_id_response_200.additional_properties = d
        return patch_api_hooks_id_response_200

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
