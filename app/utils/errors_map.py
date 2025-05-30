from enum import Enum


class ErrorCode(str, Enum):

    unknown: str = "UNKNOWN_ERROR"
    fastapi_exception: str = "BASE_EXCEPTION"
    system_error: str = "SYSTEM_ERROR"
    token_error: str = "TOKEN_ERROR"

    auth_error: str = "AUTH_ERROR"
    auth_validation_error: str = "AUTH_VALIDATION_ERROR"
    auth_credential_error: str = "CREDENTIALS_ERROR"

    account_not_found: str = "ACCOUNT_NOT_FOUND"
    account_already_exists: str = "ACCOUNT_ALREADY_EXISTS"

    notify_error: str = "NOTIFY_ERROR"
    database_error: str = "DATA_ERROR"
    not_found: str = "NOT_FOUND"

    validation_error: str = "VALIDATION_ERROR"
    unexpected_validation_error: str = "UNEXPECTED_VALIDATION_ERROR"

    external_client_error: str = "EXTERNAL_CLIENT_ERROR"

    # chat errors
    prohibited_to_delete: str = "PROHIBITED_TO_DELETE"
    member_not_found: str = "MEMBER_NOT_FOUND"
    chat_error: str = "CHAT_ERROR"
