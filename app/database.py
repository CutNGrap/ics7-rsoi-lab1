# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import *
# from sqlalchemy import *

from fastapi import *
from sqlmodel import *
from pydantic import BaseModel

class PersonScheme(BaseModel):
    id: int = None
    name: str
    age: int = None
    address: str = None
    work: str = None

class Person(SQLModel, table=True):
    __tablename__ = "person"
    id: int = Field(primary_key=True)
    name: str = Form(...)
    age: int = Field(default=0)
    address: str | None = Field(default=None)
    work: str | None = Field(default=None)

    def __repr__(self):
        return f"id={self.id}, name={self.name}, age={self.age}, address={self.address}, work={self.work}"

