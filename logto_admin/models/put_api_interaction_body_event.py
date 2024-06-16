from enum import Enum


class PutApiInteractionBodyEvent(str, Enum):
    FORGOTPASSWORD = "ForgotPassword"
    REGISTER = "Register"
    SIGNIN = "SignIn"

    def __str__(self) -> str:
        return str(self.value)
