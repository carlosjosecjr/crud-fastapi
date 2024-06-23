from datetime import datetime

from sqlalchemy import delete, exists, select
from sqlalchemy.orm import Session

from application.db.models import URL, User
from short.application.dto import LoginDataTransfer
from short.application.storage import LoginStorage, ShortStorage


class LoginRepository(LoginStorage):

    db: Session

    def __init__(self, db: Session):
        self.db: Session = db

    def save(self, login: LoginDataTransfer) -> User:
        print(self)
        user = User(username=login.user, email=login.email, psswd=login.password)
        self.db.add(user)
        self.db.commit()
        return user

    def user(self, user, email=None) -> User:
        if user:
            return self.db.query(User).filter(User.username == user).first()
        return self.db.query(User).filter(User.email == email).first()
    
    def exists(self, user, email=None) -> bool:
        return self.db.execute(
            select(
                exists().where(User.username == user)
            )
        )


class URLRepository(ShortStorage):
    def __init__(self, db: Session):
        self.db = db

    def url(self, slug: str) -> URL:
        return self.db.query(URL).filter(URL.short_url == slug).first()

    def save(self, long_url: str, short_url: str, user_id: int) -> URL:
        url = URL(
            long_url=long_url,
            short_url=short_url,
            user_id=user_id,
            clicks=0,
            created_at=datetime.now(),
        )
        self.db.add(url)
        self.db.commit()
        return url

    def delete(self, slug, user):
        result = self.db.execute(
            delete(URL).where(URL.short_url == slug, URL.user_id == user).returning(URL)
        )
        url = result.scalar_one()
        self.db.commit()
        return url

    def increment_clicks(self, url: URL):
        url.clicks += 1
        self.db.commit()
