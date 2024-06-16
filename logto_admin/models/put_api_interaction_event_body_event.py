from enum import Enum


class PutApiInteractionEventBodyEvent(str, Enum):
    FORGOTPASSWORD = "ForgotPassword"
    REGISTER = "Register"
    SIGNIN = "SignIn"

    def __str__(self) -> str:
        return str(self.value)
