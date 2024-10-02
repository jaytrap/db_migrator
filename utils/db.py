from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_engine(db_url):
    return create_engine(db_url)

def get_db_session(engine):
    session = sessionmaker(bind=engine)
    return session()
