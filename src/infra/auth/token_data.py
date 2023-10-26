from dataclasses import dataclass
from datetime import datetime


@dataclass
class TokenData:
    exp: datetime
    groups: list
    user_id: str
    token: str

    def __post_init__(self):
        if isinstance(self.exp, int):
            self.exp = datetime.fromtimestamp(self.exp)
