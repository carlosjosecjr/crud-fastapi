import os

from sqlalchemy import create_engine

DNS: str = os.getenv("PGDNS", "")
engine = create_engine(DNS)