from sqlalchemy.orm import sessionmaker

from .engine import engine

Session = sessionmaker(engine, expire_on_commit=False)
session = Session()