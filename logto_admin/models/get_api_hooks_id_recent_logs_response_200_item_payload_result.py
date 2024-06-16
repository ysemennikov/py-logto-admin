from enum import Enum


class GetApiHooksIdRecentLogsResponse200ItemPayloadResult(str, Enum):
    ERROR = "Error"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
