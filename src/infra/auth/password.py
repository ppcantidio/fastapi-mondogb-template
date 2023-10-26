import bcrypt


def generate_hashed_password(password) -> str:
    salt = bcrypt.gensalt()
    password = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
