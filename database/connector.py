from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base


def connect():
    engine = create_engine('sqlite:///test.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()