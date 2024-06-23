import datetime
import random
import string

import jwt
import sqlalchemy

from application.db.models import URL
from settings import JWT_SECRET

from .dto import LoginDataTransfer, ShortDataTransfer
from .responses import ControllerResponse, ErrorResponse, SuccessResponse
from .storage import LoginStorage, ShortStorage


class Short:
    storage: ShortStorage

    def __init__(self, storage: ShortStorage):
        self.storage = storage
        pass

    def __new_slug(self, size: int = 8) -> str:
        slug: str = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(size)
        )
        return slug

    @classmethod
    def slug(self, size: int = 8) -> str:
        return self.__new_slug(size)

    def create_link(self, user, long, short=None):
        if not short:
            short = self.slug()
        
        url = self.storage.save(long_url=long, short_url=short, user_id=user)
        return url
    
    def url(self, slug):
        return self.storage.url(slug)
    
    def delete_link(self, slug, user) -> URL:
        return self.storage.delete(slug=slug, user=user)


class Login:
    storage: LoginStorage

    def __init__(self, storage: LoginStorage) -> None:
        self.storage = storage

    @staticmethod
    def data_transfer(register: dict) -> LoginDataTransfer:
        try:
            dto = LoginDataTransfer(
                user=register.get("username"),
                email=register.get("email"),
                password=register.get("password"),
            )
            return dto
        except KeyError:
            return None

    def __gen_jwt_token(self, id, user, email) -> str:
        secret: str = JWT_SECRET
        load = self.__jwt_payload(id, user, email)
        return jwt.encode(load, secret)

    def __jwt_payload(self, id: int, user: str, email: str):
        iat: int = int(datetime.datetime.now().timestamp())
        exp: int = int(datetime.datetime.now().timestamp()) + (6 * 6 * 10 * 10)
        payload = {"sub": user, "iat": iat, "exp": exp, "user_id": id, "email": email}
        return payload

    def register(self, login: LoginDataTransfer) -> ControllerResponse:
        try:
            usr = self.storage.save(login=login)
            return ControllerResponse(
                message="SuccessResponse.value",
                code="SuccessResponse.name",
                content=usr,
            )

        except sqlalchemy.exc.IntegrityError:
            return ControllerResponse(
                code=ErrorResponse.DATABASE.name,
                message=ErrorResponse.DATABASE.value,
                content=ErrorResponse,
            )

    def authenticate(self, user: str, password: str) -> bool:
        buser = self.storage.user(user)
        dtour = self.data_transfer(
            {
                "username": user,
                "password": password,
            }
        )

        if buser.psswd == dtour.password:
            token: str = self.__gen_jwt_token(buser.id, buser.username, buser.email)
            return ControllerResponse(
                code=201,
                message="ok",
                content=token,
            )

        return ControllerResponse(
            code=401, message="unauthenticated", content=ErrorResponse.NOTAUTH
        )
