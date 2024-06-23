import pytest
import sqlalchemy

from application.db.repository.repository import LoginRepository, URLRepository
from application.db.session import Session
from short.application.dto import LoginDataTransfer
from short.application.storage import LoginStorage


def test_already_exist_user():
    with pytest.raises(sqlalchemy.exc.IntegrityError):
        with Session() as session:
            usr_repo: LoginStorage = LoginRepository(session)
            dto = LoginDataTransfer(
                user="example", email="example@example.com", password="superpass"
            )

            usr_repo.save(dto)


def test_save_user():

    with Session() as session:
        usr_repo: LoginStorage = LoginRepository(session)
        dto = LoginDataTransfer(
            user="examplee", email="example@examplee.com", password="superpass"
        )

        user = usr_repo.save(dto)
        print(user)

        assert dto.user == user.username
        assert dto.email == user.email
        assert user.id != None


def test_get_user():

    with Session() as session:
        usr_repo: LoginStorage = LoginRepository(session)
        user = usr_repo.user("example")
        assert user.username == "example"


def test_hellp():

    with Session() as session:
        url_repo = URLRepository(session)
        url = url_repo.create_url(
            long_url="https://www.google.com", short_url="8fRzZ6", user_id=1
        )
        print(url)
