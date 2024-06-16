from enum import Enum


class PostApiConnectorsResponse200FormItemsItemType1Type(str, Enum):
    JSON = "Json"
    MULTILINETEXT = "MultilineText"
    NUMBER = "Number"
    SWITCH = "Switch"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)
