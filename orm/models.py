from xmlrpc.client import Boolean

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, Column, String, ForeignKey, Text,Boolean
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from typing import List
class Base(DeclarativeBase):
    pass


class AuthUser(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(30))
    surname: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String, nullable=False)
    phone_number: Mapped[str] = Column(String, nullable=False)
    hashed_password: Mapped[str] = Column(String, nullable=False)
    pictures: Mapped[List["Picture"]] = relationship(back_populates="picture_user_id")
    is_active: Mapped[bool] = Column(Boolean, nullable=True)
    is_superuser: Mapped[bool] = Column(Boolean, nullable=True)
    is_verified: Mapped[bool] = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"User= {self.name} {self.surname} "


class Picture(Base):
    __tablename__ = "picture"
    id: Mapped[int] = Column(Integer, primary_key=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey("FastapiUser.id"), nullable=False)
    file_50: Mapped[str] = Column(Text)
    file_100: Mapped[str] = Column(Text)
    file_400: Mapped[str] = Column(Text)

    def __repr__(self):
        return f"Picture={self.id}, user={self.user_id})"




# from sqlalchemy import Column,ForeignKey,Integer,String,Text
# from sqlalchemy import ForeignKey
# from sqlalchemy import Integer
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import relationship
# import base64
#
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = "user_account"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     surname = Column(String)
#     email = Column(String, nullable=False)
#     phone_number = Column(String, nullable=False)
#     password = Column(String, nullable=False)
#     pictures = relationship(
#         "Picturepack",  cascade="all, delete-orphan"
#     )
#     @classmethod
#     def get_user(cls,phone_number):
#         return cls.get(phone_number=phone_number)
#
#     def verify_password(self,password):
#         if self.password:
#             return True
#
#
#     def __repr__(self):
#         return f"User id={self.id}, name={self.name}, fullname={self.surname})"
#
#
#
# class Picturepack(Base):
#     __tablename__ = "picturepack"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
#     file_50 = Column(Text)
#     file_100 = Column(Text)
#     file_400 = Column(Text)
#     def __repr__(self):
#         return f"Picturepack{self.id}, user={self.user_id})"