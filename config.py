from dataclasses import dataclass
from pydantic import BaseModel
from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Token:
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


@dataclass
class Config:
    db: DbConfig
    token: Token


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        token=Token(
            secret_key=env.str('SECRET_KEY'),
            algorithm=env.str('ALGORITHM'),
            access_token_expire_minutes=env.int('ACCESS_TOKEN_EXPIRE_MINUTES')
        )
    )


config = load_config(".env")
