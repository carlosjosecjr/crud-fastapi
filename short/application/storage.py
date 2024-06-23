import abc

from .dto import LoginDataTransfer


class ShortStorage(abc.ABC):

    @classmethod
    def save(self, long_url: str, short_url: str, user_id: int):
        pass

    @classmethod
    def url(self, slug: str) -> str:
        pass

    @classmethod
    def delete(self, slug: str, user: str):
        pass

class LoginStorage(abc.ABC):

    @classmethod
    def save(self, login: LoginDataTransfer) -> any:
        pass

    @classmethod
    def exists(self, user, email = None) -> bool:
        pass

    @classmethod
    def user(self, user) -> any:
        pass