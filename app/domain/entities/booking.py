from dataclasses import dataclass
from .base import BaseEntity
from .enums import BookingStatus,PaymentStatus,RoomStatus
from .guests import Guest
from .rooms import Room
from datetime import datetime




@dataclass(kw_only=True)
class Booking(BaseEntity):
    guest: Guest
    room: Room
    check_in: datetime
    check_out: datetime
    status: BookingStatus
    payment: PaymentStatus


    def __post_init__(self):

        if not isinstance(self.guest, Guest):
            raise TypeError(f'Guest must be a Guest instance, got {type(self.guest  )}')
        
        if not isinstance(self.room, Room):
            raise TypeError(f"Room must be an Room instance, got {type(self.room)}")
        
        if not isinstance(self.status, BookingStatus):
            raise TypeError(f"status must be a BookingStatus enum, got {type(self.status)}")
        
        if not isinstance(self.payment, PaymentStatus):
            raise TypeError(f"payment must be a PaymentStatus enum, got {type(self.payment)}")


    def duration(self) -> int:
        return (self.check_out - self.check_in).days

    def mark_checked_in(self):
        if self.status != BookingStatus.CONFIRMED:
            raise ValueError("Booking not confirmed")
        self.status = BookingStatus.CHECKED_IN

    def mark_checked_out(self):
        if self.status != BookingStatus.CHECKED_IN:
            raise ValueError("Guest not checked in")
        self.status = BookingStatus.CHECKED_OUT
        self.room.mark_status(RoomStatus.MAINTENANCE)
