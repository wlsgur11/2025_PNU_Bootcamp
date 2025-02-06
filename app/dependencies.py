import os
from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, Session, create_engine, select

# dependencies
load_dotenv()

db_url = os.getenv("DB_HOST")
db_conn_args = {"check_same_thread": False}
db_engine = create_engine(db_url, connect_args=db_conn_args)
def get_db_session():
    with Session(db_engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)