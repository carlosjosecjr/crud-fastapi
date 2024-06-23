from pydantic import BaseModel, EmailStr


class CreateRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


class CreatedRegister(BaseModel):
    id: int
    username: str
    email: EmailStr


class SuccessRegisterResponse(BaseModel):
    message: str
    status_code: int
    reg: CreatedRegister

class ErrorResponse(BaseModel):
    message: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    # expires_in: str