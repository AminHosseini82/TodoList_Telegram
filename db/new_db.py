from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('sqlite:///test.db')
base = declarative_base()


class User(base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))

    def __repr__(self):
        return f"<User(user_id={self.user_id}, first_name='{self.first_name}')>"

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
