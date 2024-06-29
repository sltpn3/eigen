from app.libs.deps import IS_DEBUG
from app.libs.messages import error_messages
from fastapi import HTTPException, status
from typing import List, Tuple
from app.libs import deps
from sqlalchemy.exc import IntegrityError
# from sentry_sdk import capture_exception
import sys


class UploadFileTypeError(Exception):
    def __init__(self, accepted_files: List[str]):
        self.message = f"Accepted files are {', '.join(accepted_files)}"
        super().__init__(self.message)


class DuplicateError(Exception):
    def __init__(self, message: Tuple[str, str]):
        self.message = f"{message[0]} {message[1]} already in use"
        super().__init__(self.message)


class UploadFileTemplateError(Exception):
    def __init__(self, message: str):
        self.message = "Gunakan File Template Yang Disediakan"
        super().__init__(self.message)


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_messages.INVALID_CREDENTIAL,
    headers={"WWW-Authenticate": "Bearer"},
)

member_penalized_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_messages.MEMBER_PENALIZED,
    headers={"WWW-Authenticate": "Bearer"},
)

borrow_limit_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_messages.BORROW_LIMIT,
    headers={"WWW-Authenticate": "Bearer"},
)


user_inactive_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_messages.USER_INACTIVE
)

ws_inactive_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_messages.WS_INACTIVE
)

scopes_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail=error_messages.INCOMPLETE,
)

permission_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail=error_messages.FORBIDDEN,
)

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=error_messages.NOT_FOUND,
)

inactive_exception = HTTPException(
    status_code=status.HTTP_410_GONE,
    detail=error_messages.GONE,
)

code_unusable_exception = HTTPException(
    status_code=status.HTTP_410_GONE,
    detail=error_messages.GONE,
)


def handle_exception(e: Exception):
    if isinstance(e, HTTPException):
        status_code = e.status_code
        message = e.detail
    elif isinstance(e, UploadFileTypeError):
        message = e.message
        status_code = 500
    elif isinstance(e, IntegrityError):
        if 'Duplicate entry' in str(e):
            message = error_messages.DUPLICATE_ENTRY
        elif 'foreign key constraint fails' in str(e):
            message = error_messages.FOREIGN_KEY_FAIL
        else:
            message = str(type(e))
            # capture_exception(e)
        status_code = 500
    elif isinstance(e, DuplicateError):
        message = e.message
        status_code = 409
    elif isinstance(e, UploadFileTemplateError):
        message = e.message
        status_code = 422
    else:
        # capture_exception(e)
        status_code = 500
        message = str(type(e))
    return status_code, message


def print_debug(e: Exception):
    if IS_DEBUG:
        print(e)
        print(sys.exc_info())
