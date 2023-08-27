from dynaconf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

if settings["AMBIENTE"] == "PRD":
    username = settings["USERNAME"]
    password = settings["PASSWORD"]
    host = settings["HOST"]
    port = settings["PORT"]
    database = settings["DATABASE"]

    SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"


Base = declarative_base()


def get_db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return engine


# Cria uma fábrica de sessões usando o objeto de conexão com o banco de dados criado em `get_db_engine`
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_db_engine())


# Define uma função para criar uma sessão para cada requisição
def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
