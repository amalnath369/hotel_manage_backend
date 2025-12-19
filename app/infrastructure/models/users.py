from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Integer, Enum
from . base import BaseModel

from app.domain.entities.enums import Role




class UserModel(BaseModel):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(100),nullable=False,index=True)
    email:  Mapped[str] = mapped_column(String(150), unique=True,nullable=False,index=True)
    password: Mapped[str] = mapped_column(String(255),nullable=False)
    phone: Mapped[int] = mapped_column(Integer,nullable=False,index=True)

    role:Mapped[Role] = mapped_column(Enum(Role, name = 'role'),default=Role.STAFF,index=True)