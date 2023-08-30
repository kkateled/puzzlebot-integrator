from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.config.global_config import GlobalConfig

global_config = GlobalConfig()


def build_db_url() -> str:
    db = global_config.database
    return f"postgresql://{db.username}:{db.password}@{db.host}:{db.port}/{db.dbname}"


engine = create_engine(build_db_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
