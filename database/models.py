import bcrypt
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()


# --------------------------------------------UserClass------------------------------------------------

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)  # user_id will unique=True in Telegram
    firstname = Column(String(100))
    lastname = Column(String(100))
    password = Column(String(100))
    # relationship with Todo_class
    todos = relationship("Todo", back_populates="users")

    def __repr__(self):
        return f"<User {self.user_id}>"

    def __str__(self):
        return f"User {self.user_id} , name is :{self.firstname}, {self.lastname})"

    def set_password(self, password):
        # Generate a salt (random string)
        salt = bcrypt.gensalt()
        # Encode the password string to bytes (UTF-8 is common)
        password_bytes = password.encode('utf-8')
        # Hash the password with the salt
        self.password = bcrypt.hashpw(password_bytes, salt)

    def check_password(self, password):
        return bcrypt.checkpw(password, self.password)

# --------------------------------------------TodoClass------------------------------------------------
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(300))
    description = Column(String)
    # the ForeignKey to user
    user_id = Column(String, ForeignKey('users.id'))  # کلید خارجی به جدول users
    # relationship with users
    users = relationship("User", back_populates="todos")

    def __repr__(self):
        return f"title: {self.title}"

    def __str__(self):
        return self.title


# create database and tables
Base.metadata.create_all(engine)

# create session for work with database.
Session = sessionmaker(bind=engine)
session = Session()
