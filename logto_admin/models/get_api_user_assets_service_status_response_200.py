from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_user_assets_service_status_response_200_allow_upload_mime_types_item import (
    GetApiUserAssetsServiceStatusResponse200AllowUploadMimeTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiUserAssetsServiceStatusResponse200")


@_attrs_define
class GetApiUserAssetsServiceStatusResponse200:
    """
    Attributes:
        status (str):
        allow_upload_mime_types (Union[Unset, List[GetApiUserAssetsServiceStatusResponse200AllowUploadMimeTypesItem]]):
        max_upload_file_size (Union[Unset, float]):
    """

    status: str
    allow_upload_mime_types: Union[Unset, List[GetApiUserAssetsServiceStatusResponse200AllowUploadMimeTypesItem]] = (
        UNSET
    )
    max_upload_file_size: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: str
        status = self.status

        allow_upload_mime_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_upload_mime_types, Unset):
            allow_upload_mime_types = []
            for allow_upload_mime_types_item_data in self.allow_upload_mime_types:
                allow_upload_mime_types_item = allow_upload_mime_types_item_data.value
                allow_upload_mime_types.append(allow_upload_mime_types_item)

        max_upload_file_size = self.max_upload_file_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if allow_upload_mime_types is not UNSET:
            field_dict["allowUploadMimeTypes"] = allow_upload_mime_types
        if max_upload_file_size is not UNSET:
            field_dict["maxUploadFileSize"] = max_upload_file_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_status(data: object) -> str:
            return cast(str, data)

        status = _parse_status(d.pop("status"))

        allow_upload_mime_types = []
        _allow_upload_mime_types = d.pop("allowUploadMimeTypes", UNSET)
        for allow_upload_mime_types_item_data in _allow_upload_mime_types or []:
            allow_upload_mime_types_item = GetApiUserAssetsServiceStatusResponse200AllowUploadMimeTypesItem(
                allow_upload_mime_types_item_data
            )

            allow_upload_mime_types.append(allow_upload_mime_types_item)

        max_upload_file_size = d.pop("maxUploadFileSize", UNSET)

        get_api_user_assets_service_status_response_200 = cls(
            status=status,
            allow_upload_mime_types=allow_upload_mime_types,
            max_upload_file_size=max_upload_file_size,
        )

        get_api_user_assets_service_status_response_200.additional_properties = d
        return get_api_user_assets_service_status_response_200

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
