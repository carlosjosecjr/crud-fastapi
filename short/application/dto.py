import hashlib


class ShortDataTransfer:
    pass


class LoginDataTransfer:
    user: str
    email: str
    password: str

    def __init__(self, user: str, email: str, password: str):
        self.user = user
        self.email = email
        self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        # bypass use of salt to password hashing
        # TODO: implment salt util function to password hash
        #       diferent users can use same password.
        #       9fa7b1c3f5ae1bbcd5a9a444acbeba2c0ce3eeecea3508d25964dac2fb29bd64

    def domain(self) -> any:
        pass

    def __str__(self) -> str:
        return f"{self.user} {self.email} {self.password}"

    def __repr__(self) -> str:
        return f"Login('{self.user}', '{self.email}', '{self.password}')"
