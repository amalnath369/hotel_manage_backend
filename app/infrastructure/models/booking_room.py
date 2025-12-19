import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey
from .base import BaseModel



class BookingRoomModel(BaseModel):
    __tablename__ = 'booking_rooms'

    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'), nullable=False)
    room_id:  Mapped[uuid.UUID] = mapped_column(ForeignKey('rooms.id'), nullable=False)

    extra_bed: Mapped[bool] = mapped_column(Boolean, default=False)

    booking = relationship('BookingModel', lazy='joined')
    room = relationship('RoomModel', lazy='joined')
