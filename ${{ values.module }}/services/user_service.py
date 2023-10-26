from sqlalchemy.orm import Session

from ..models.payloads.user_payloads import CreateExample, UpdateExample, UserLogin


class UserService:
    def __init__(self, session: Session) -> None:
        example_repository = ExampleRepository(session=session)

    def create_example(self, obj_in: CreateExample):
        pass

    def update_example(self):
        pass

    def get_example(self):
        pass

    def delete_example(self):
        pass

    def login(self, login_credentials: UserLogin):
        pass
