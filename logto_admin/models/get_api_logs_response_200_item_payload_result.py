from enum import Enum


class GetApiLogsResponse200ItemPayloadResult(str, Enum):
    ERROR = "Error"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
