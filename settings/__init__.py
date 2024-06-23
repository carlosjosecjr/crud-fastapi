import os

MAX_SLUG_SIZE = int(os.getenv("MAX_SLUG_SIZE"))
JWT_SECRET = os.getenv("JWT_SECRET") # openssl rand -base64 48

DESCRIPTION = """
### API for CRUD-FASTAPI
SUPER TEXT
"""