from starlette.config import Config
from starlette.datastructures import Secret


try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

BOOK_DATABASE_URL = config("BOOK_DATABASE_URL", cast=Secret)