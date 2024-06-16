from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_organizations_id_body_custom_data import PatchApiOrganizationsIdBodyCustomData


T = TypeVar("T", bound="PatchApiOrganizationsIdBody")


@_attrs_define
class PatchApiOrganizationsIdBody:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]): The updated name of the organization.
        description (Union[None, Unset, str]): The updated description of the organization.
        custom_data (Union[Unset, PatchApiOrganizationsIdBodyCustomData]): arbitrary
        created_at (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    custom_data: Union[Unset, "PatchApiOrganizationsIdBodyCustomData"] = UNSET
    created_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_organizations_id_body_custom_data import PatchApiOrganizationsIdBodyCustomData

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _custom_data = d.pop("customData", UNSET)
        custom_data: Union[Unset, PatchApiOrganizationsIdBodyCustomData]
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = PatchApiOrganizationsIdBodyCustomData.from_dict(_custom_data)

        created_at = d.pop("createdAt", UNSET)

        patch_api_organizations_id_body = cls(
            id=id,
            name=name,
            description=description,
            custom_data=custom_data,
            created_at=created_at,
        )

        patch_api_organizations_id_body.additional_properties = d
        return patch_api_organizations_id_body

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
