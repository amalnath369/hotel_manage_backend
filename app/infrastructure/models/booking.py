import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Enum

from . base import BaseModel
from app.domain.entities.enums import BookingStatus,PaymentStatus



class BookingModel(BaseModel):
    __tablename__ = 'bookings'

    primary_guest_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('guests.id'), nullable=False)

    check_in: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    check_out: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    booking_status: Mapped[BookingStatus] = mapped_column( Enum(BookingStatus, name="booking_status_enum"),nullable=False)

    payment_status: Mapped[PaymentStatus] = mapped_column( Enum(PaymentStatus, name="payment_status_enum"), nullable=False,
                                                          default=PaymentStatus.PENDING)
    
    guest = relationship("GuestModel", lazy="joined")
    