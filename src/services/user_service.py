from src.entities.user import User
from src.errors.bad_request_err import BadRequestError
from src.errors.unauthorized import Unauthorized
from src.infra.auth.client_session import ClientSession
from src.infra.auth.password import check_password, generate_hashed_password
from src.infra.auth.token_data import TokenData
from src.infra.db.repositorys.user_repository import UserRepository


class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepository()

    def registrar_usuario(self, username: str, password: str) -> User:
        user_already_exists = self.user_repo.select_username(username=username)
        if user_already_exists:
            raise BadRequestError(message="Already exists an user with this username", code_error="USER_ALREADY_EXISTS")

        hashed_password = generate_hashed_password(password=password)
        user = User(username=username, hashed_password=hashed_password)
        inserted_id = self.user_repo.insert_one(user)
        user.id = inserted_id
        return user

    def login(self, username, password) -> TokenData:
        user = self.user_repo.select_username(username=username)
        wrong_credentials_exc = Unauthorized(message="Username or password incorrect.", code_error="WRONG_CREDENTIALS")
        if user is None:
            raise wrong_credentials_exc

        if check_password(password=password, hashed_password=user.hashed_password) is False:
            raise wrong_credentials_exc

        token_data = ClientSession().create_session(user_id=str(user.id))
        return token_data
