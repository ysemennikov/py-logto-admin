from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_organizations_id_response_200_custom_data import (
        PatchApiOrganizationsIdResponse200CustomData,
    )


T = TypeVar("T", bound="PatchApiOrganizationsIdResponse200")


@_attrs_define
class PatchApiOrganizationsIdResponse200:
    """
    Attributes:
        id (str):
        name (str):
        description (Union[None, str]):
        custom_data (PatchApiOrganizationsIdResponse200CustomData): arbitrary
        created_at (float):
    """

    id: str
    name: str
    description: Union[None, str]
    custom_data: "PatchApiOrganizationsIdResponse200CustomData"
    created_at: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, str]
        description = self.description

        custom_data = self.custom_data.to_dict()

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "customData": custom_data,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_api_organizations_id_response_200_custom_data import (
            PatchApiOrganizationsIdResponse200CustomData,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        custom_data = PatchApiOrganizationsIdResponse200CustomData.from_dict(d.pop("customData"))

        created_at = d.pop("createdAt")

        patch_api_organizations_id_response_200 = cls(
            id=id,
            name=name,
            description=description,
            custom_data=custom_data,
            created_at=created_at,
        )

        patch_api_organizations_id_response_200.additional_properties = d
        return patch_api_organizations_id_response_200

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
