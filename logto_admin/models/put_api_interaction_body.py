from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_interaction_body_event import PutApiInteractionBodyEvent
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_interaction_body_identifier_type_0 import PutApiInteractionBodyIdentifierType0
    from ..models.put_api_interaction_body_identifier_type_1 import PutApiInteractionBodyIdentifierType1
    from ..models.put_api_interaction_body_identifier_type_2 import PutApiInteractionBodyIdentifierType2
    from ..models.put_api_interaction_body_identifier_type_3 import PutApiInteractionBodyIdentifierType3
    from ..models.put_api_interaction_body_identifier_type_4 import PutApiInteractionBodyIdentifierType4
    from ..models.put_api_interaction_body_identifier_type_5 import PutApiInteractionBodyIdentifierType5
    from ..models.put_api_interaction_body_identifier_type_6 import PutApiInteractionBodyIdentifierType6
    from ..models.put_api_interaction_body_identifier_type_7 import PutApiInteractionBodyIdentifierType7
    from ..models.put_api_interaction_body_profile import PutApiInteractionBodyProfile


T = TypeVar("T", bound="PutApiInteractionBody")


@_attrs_define
class PutApiInteractionBody:
    """
    Attributes:
        event (PutApiInteractionBodyEvent):
        identifier (Union['PutApiInteractionBodyIdentifierType0', 'PutApiInteractionBodyIdentifierType1',
            'PutApiInteractionBodyIdentifierType2', 'PutApiInteractionBodyIdentifierType3',
            'PutApiInteractionBodyIdentifierType4', 'PutApiInteractionBodyIdentifierType5',
            'PutApiInteractionBodyIdentifierType6', 'PutApiInteractionBodyIdentifierType7', Unset]):
        profile (Union[Unset, PutApiInteractionBodyProfile]):
    """

    event: PutApiInteractionBodyEvent
    identifier: Union[
        "PutApiInteractionBodyIdentifierType0",
        "PutApiInteractionBodyIdentifierType1",
        "PutApiInteractionBodyIdentifierType2",
        "PutApiInteractionBodyIdentifierType3",
        "PutApiInteractionBodyIdentifierType4",
        "PutApiInteractionBodyIdentifierType5",
        "PutApiInteractionBodyIdentifierType6",
        "PutApiInteractionBodyIdentifierType7",
        Unset,
    ] = UNSET
    profile: Union[Unset, "PutApiInteractionBodyProfile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.put_api_interaction_body_identifier_type_0 import PutApiInteractionBodyIdentifierType0
        from ..models.put_api_interaction_body_identifier_type_1 import PutApiInteractionBodyIdentifierType1
        from ..models.put_api_interaction_body_identifier_type_2 import PutApiInteractionBodyIdentifierType2
        from ..models.put_api_interaction_body_identifier_type_3 import PutApiInteractionBodyIdentifierType3
        from ..models.put_api_interaction_body_identifier_type_4 import PutApiInteractionBodyIdentifierType4
        from ..models.put_api_interaction_body_identifier_type_5 import PutApiInteractionBodyIdentifierType5
        from ..models.put_api_interaction_body_identifier_type_6 import PutApiInteractionBodyIdentifierType6

        event = self.event.value

        identifier: Union[Dict[str, Any], Unset]
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType0):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType1):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType2):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType3):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType4):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType5):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, PutApiInteractionBodyIdentifierType6):
            identifier = self.identifier.to_dict()
        else:
            identifier = self.identifier.to_dict()

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_api_interaction_body_identifier_type_0 import PutApiInteractionBodyIdentifierType0
        from ..models.put_api_interaction_body_identifier_type_1 import PutApiInteractionBodyIdentifierType1
        from ..models.put_api_interaction_body_identifier_type_2 import PutApiInteractionBodyIdentifierType2
        from ..models.put_api_interaction_body_identifier_type_3 import PutApiInteractionBodyIdentifierType3
        from ..models.put_api_interaction_body_identifier_type_4 import PutApiInteractionBodyIdentifierType4
        from ..models.put_api_interaction_body_identifier_type_5 import PutApiInteractionBodyIdentifierType5
        from ..models.put_api_interaction_body_identifier_type_6 import PutApiInteractionBodyIdentifierType6
        from ..models.put_api_interaction_body_identifier_type_7 import PutApiInteractionBodyIdentifierType7
        from ..models.put_api_interaction_body_profile import PutApiInteractionBodyProfile

        d = src_dict.copy()
        event = PutApiInteractionBodyEvent(d.pop("event"))

        def _parse_identifier(
            data: object,
        ) -> Union[
            "PutApiInteractionBodyIdentifierType0",
            "PutApiInteractionBodyIdentifierType1",
            "PutApiInteractionBodyIdentifierType2",
            "PutApiInteractionBodyIdentifierType3",
            "PutApiInteractionBodyIdentifierType4",
            "PutApiInteractionBodyIdentifierType5",
            "PutApiInteractionBodyIdentifierType6",
            "PutApiInteractionBodyIdentifierType7",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_0 = PutApiInteractionBodyIdentifierType0.from_dict(data)

                return identifier_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_1 = PutApiInteractionBodyIdentifierType1.from_dict(data)

                return identifier_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_2 = PutApiInteractionBodyIdentifierType2.from_dict(data)

                return identifier_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_3 = PutApiInteractionBodyIdentifierType3.from_dict(data)

                return identifier_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_4 = PutApiInteractionBodyIdentifierType4.from_dict(data)

                return identifier_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_5 = PutApiInteractionBodyIdentifierType5.from_dict(data)

                return identifier_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_6 = PutApiInteractionBodyIdentifierType6.from_dict(data)

                return identifier_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            identifier_type_7 = PutApiInteractionBodyIdentifierType7.from_dict(data)

            return identifier_type_7

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, PutApiInteractionBodyProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = PutApiInteractionBodyProfile.from_dict(_profile)

        put_api_interaction_body = cls(
            event=event,
            identifier=identifier,
            profile=profile,
        )

        put_api_interaction_body.additional_properties = d
        return put_api_interaction_body

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
