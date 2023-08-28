from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import get_settings

config = get_settings()

SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{config.db_username}:{config.db_password}@{config.db_host}:{config.db_port}/${config.db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
