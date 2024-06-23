from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from application.db.repository import LoginRepository
from application.db.session import session
from short.application import ctrl

from .responses import oauth_response, register_response
from .schemas import (
    CreatedRegister,
    CreateRegister,
    SuccessRegisterResponse,
    TokenResponse,
)

router = APIRouter(
    prefix="/oauth"
)

@router.post("/token",
             tags=["auth"],
             summary="OAuth2 Authentication",
             include_in_schema=False,
             responses=oauth_response)
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        login_ctrl = ctrl.Login(storage=LoginRepository(session))
        re = login_ctrl.authenticate(form_data.username, form_data.password)
        token: str = re.content
        return TokenResponse(
            access_token=token,
            token_type="bearer",
        )
    except:
        pass

@router.post("/register",
             tags=["register"],
             summary="User Register",
             responses=register_response)
async def register(response: Response, reg: CreateRegister):
    print(reg)
    register_ctrl = ctrl.Login(storage=LoginRepository(session))
    dto = register_ctrl.data_transfer(reg.model_dump())
    user = register_ctrl.register(dto).content
    usr_schm = CreatedRegister(
        id=user.id,
        username=user.username,
        email=user.email,
    )
    response.status_code=status.HTTP_201_CREATED
    return SuccessRegisterResponse(
        message="success created user",
        status_code=201,
        reg=usr_schm
    )