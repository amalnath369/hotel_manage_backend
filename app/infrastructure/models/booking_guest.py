import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey
from .base import BaseModel


class BookingGuestModel(BaseModel):
    __tablename__ = 'booking_guest'

    booking_room_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('booking_rooms.id'), nullable=False)
    guest_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('guests.id'), nullable=False)

    is_primary: Mapped[bool] = mapped_column(Boolean,default=False)
    