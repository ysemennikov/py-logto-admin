from enum import Enum


class GetApiUserAssetsServiceStatusResponse200AllowUploadMimeTypesItem(str, Enum):
    IMAGEBMP = "image/bmp"
    IMAGEGIF = "image/gif"
    IMAGEJPEG = "image/jpeg"
    IMAGEPNG = "image/png"
    IMAGESVGXML = "image/svg+xml"
    IMAGETIFF = "image/tiff"
    IMAGEVND_MICROSOFT_ICON = "image/vnd.microsoft.icon"
    IMAGEWEBP = "image/webp"
    IMAGEX_ICON = "image/x-icon"

    def __str__(self) -> str:
        return str(self.value)
