from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum
from . base import BaseModel

from app.domain.entities.enums import RoomStatus,RoomType,ACType



class RoomModel(BaseModel):
    __tablename__ = 'rooms'

    room_number: Mapped[str] = mapped_column(String(5), unique=True,nullable=False,index=True)
    room_type: Mapped[RoomType] = mapped_column(Enum(RoomType, name = 'room_type'), nullable=False,index=True)
    ac_or_non_ac: Mapped[ACType] = mapped_column(Enum(ACType, name = 'ac_or_non_ac'), nullable=False, index=True)
    floor: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    status : Mapped[RoomStatus] = mapped_column(Enum(RoomStatus, name = 'room_status'), default=RoomStatus.AVAILABLE, index=True)

    bookings = relationship( "BookingModel", back_populates="guest", lazy="selectin")