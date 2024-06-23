from fastapi import status

from .schemas import ErrorResponse, SuccessRegisterResponse, TokenResponse

oauth_response = {
    status.HTTP_200_OK: {},
    status.HTTP_401_UNAUTHORIZED: {},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {}
}

register_response = {
    status.HTTP_200_OK: {
        "description": "successful registering user",
        "model": SuccessRegisterResponse,
    },
    status.HTTP_201_CREATED: {
        "description": "successful registering user",
        "model": SuccessRegisterResponse,
    },
    status.HTTP_400_BAD_REQUEST: {
        "description": "invalid request",
        "model": ErrorResponse},
    status.HTTP_409_CONFLICT: {
        "description": "previously registered user",
        "model": ErrorResponse,
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "internal server error",
        "model": ErrorResponse,
    },
}
