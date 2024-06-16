from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_organizations_body_custom_data import PostApiOrganizationsBodyCustomData


T = TypeVar("T", bound="PostApiOrganizationsBody")


@_attrs_define
class PostApiOrganizationsBody:
    """
    Attributes:
        name (str): The name of the organization.
        description (Union[None, Unset, str]): The description of the organization.
        custom_data (Union[Unset, PostApiOrganizationsBodyCustomData]): arbitrary
        created_at (Union[Unset, float]):
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    custom_data: Union[Unset, "PostApiOrganizationsBodyCustomData"] = UNSET
    created_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        custom_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_data, Unset):
            custom_data = self.custom_data.to_dict()

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_organizations_body_custom_data import PostApiOrganizationsBodyCustomData

        d = src_dict.copy()
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _custom_data = d.pop("customData", UNSET)
        custom_data: Union[Unset, PostApiOrganizationsBodyCustomData]
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = PostApiOrganizationsBodyCustomData.from_dict(_custom_data)

        created_at = d.pop("createdAt", UNSET)

        post_api_organizations_body = cls(
            name=name,
            description=description,
            custom_data=custom_data,
            created_at=created_at,
        )

        post_api_organizations_body.additional_properties = d
        return post_api_organizations_body

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
