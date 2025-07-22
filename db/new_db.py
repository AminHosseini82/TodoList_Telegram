import bcrypt
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    first_name = Column(String(100))
    last_name = Column(String(100))
    # strong password
    password = Column(String(120))

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode(), salt).decode()

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password.encode())

    def __repr__(self):
        return f"user_id {self.user_id},first name {self.first_name},last name {self.last_name}"


Base.metadata.create_all(engine)
# 5. ایجاد نشست (Session) برای کار با دیتابیس
Session = sessionmaker(bind=engine)
session = Session()