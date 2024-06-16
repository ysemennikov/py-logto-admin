from enum import Enum


class PostApiUsersBodyPasswordAlgorithm(str, Enum):
    ARGON2I = "Argon2i"
    BCRYPT = "Bcrypt"
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"

    def __str__(self) -> str:
        return str(self.value)
