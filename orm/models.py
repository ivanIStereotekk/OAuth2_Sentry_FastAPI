from sqlalchemy import Column,ForeignKey,Integer,String,Text
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import base64


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    surname = Column(String)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    password = Column(String, nullable=False)
    pictures = relationship(
        "Picturepack",  cascade="all, delete-orphan"
    )
    @classmethod
    def get_user(cls,phone_number):
        return cls.get(phone_number=phone_number)

    def verify_password(self,password):
        if self.password:
            return True


    def __repr__(self):
        return f"User id={self.id}, name={self.name}, fullname={self.surname})"



class Picturepack(Base):
    __tablename__ = "picturepack"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    file_50 = Column(Text)
    file_100 = Column(Text)
    file_400 = Column(Text)
    def __repr__(self):
        return f"Picturepack{self.id}, user={self.user_id})"