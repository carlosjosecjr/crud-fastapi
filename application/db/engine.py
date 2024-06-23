import os

from sqlalchemy import create_engine

# DNS: str = os.getenv("PGDNS", "")
engine = create_engine("postgresql+psycopg2://postgres:rYSJh5z4@localhost:5432/short")