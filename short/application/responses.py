from dataclasses import dataclass
from enum import Enum


@dataclass
class ControllerResponse:
    message: str
    code: str
    content: any

class SuccessResponse(Enum):
    pass

class ErrorResponse(Enum):
    DATABASE = 'Database problem or constraint violation'
    NOTAUTH = 'unauthenticated'