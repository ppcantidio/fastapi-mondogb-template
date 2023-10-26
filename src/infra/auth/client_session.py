from datetime import datetime, timedelta

import jwt

from config import settings
from src.errors.forbidden_err import ForbiddenError

from .token_data import TokenData


class ClientSession:
    algorithm = settings("ALGORITHM")
    secret_key = settings("SECRET_KEY")
    access_token_expiration_seconds = settings("ACESS_TOKEN_EXPIRATION_HOURS") * 3600

    def verify_session(self, token) -> TokenData:
        try:
            payload = jwt.decode(token.encode(), self.secret_key, algorithms=[self.algorithm])
            payload["token"] = token
            token_data = TokenData(**payload)
            return token_data
        except Exception as e:
            raise ForbiddenError(message="Invalid session", code_error="INVALID_SESSION")

    def create_session(self, user_id: str, groups=["CLIENT"]):
        expires_delta = timedelta(seconds=self.access_token_expiration_seconds)
        expire = datetime.utcnow() + expires_delta
        token_dict = {"exp": expire, "groups": groups, "user_id": user_id}
        token = jwt.encode(token_dict, self.secret_key, algorithm=self.algorithm)
        token_dict["token"] = token
        return TokenData(**token_dict)
