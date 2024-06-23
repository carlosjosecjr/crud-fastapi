from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    psswd = Column(String(), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    urls = relationship('URL', backref='user', lazy='dynamic')

    def __str__(self):
        return f"<User '{self.id}'', '{self.username}'>"

    def __repr__(self):
        return f"<User '{self.id}'', '{self.username}'>"

class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    long_url = Column(String(2048), nullable=False)
    short_url = Column(String(50), nullable=False, unique=True)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<URL {self.short_url}>'
