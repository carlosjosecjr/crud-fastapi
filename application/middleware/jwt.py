from os import getenv

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from settings import JWT_SECRET

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="http://localhost:8000/oauth/token",
    # TODO: add fastapi dinamic url
    # ----  há configurações no fastapi onde isso fica dinâmico
)

async def token_handler(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.InvalidSignatureError:
        raise HTTPException(
            status_code=401,
            detail="unauthorized: token problems."
        )
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError):
        raise HTTPException(
            status_code=401,
            detail="unauthorized: another problem."
        )
