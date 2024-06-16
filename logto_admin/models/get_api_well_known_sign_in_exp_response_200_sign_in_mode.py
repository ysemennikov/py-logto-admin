from enum import Enum


class GetApiWellKnownSignInExpResponse200SignInMode(str, Enum):
    REGISTER = "Register"
    SIGNIN = "SignIn"
    SIGNINANDREGISTER = "SignInAndRegister"

    def __str__(self) -> str:
        return str(self.value)
