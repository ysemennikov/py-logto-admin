from enum import Enum


class PostApiInteractionVerificationWebauthnRegistrationResponse200ExcludeCredentialsItemTransportsItem(str, Enum):
    BLE = "ble"
    CABLE = "cable"
    HYBRID = "hybrid"
    INTERNAL = "internal"
    NFC = "nfc"
    SMART_CARD = "smart-card"
    USB = "usb"

    def __str__(self) -> str:
        return str(self.value)
