from sqlmodel import Field, SQLModel, create_engine, Session

from balaaj_book_centre import config

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    
    

conn_str = str(config.BOOK_DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)


engine = create_engine(conn_str, connect_args={"sslmode": "require"}, pool_recycle=300, pool_size=5, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db()->None:
    SQLModel.metadata.create_all(engine)