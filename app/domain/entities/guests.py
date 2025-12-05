from dataclasses import dataclass
from .base import BaseEntity
from .users import User
from .rooms import Room
from .enums import IDCard,BookingStatus,PaymentStatus,RoomStatus
from typing import Optional
from datetime import datetime



@dataclass(kw_only=True)
class BlacklistGuest(BaseEntity):
    name : str
    email : str
    phone : int
    reason : str
    id_card :  IDCard
    id_card_num : str
    id_card_image_path : Optional[str] = None
    guest_photo_path: Optional[str] = None
    added_by : User



@dataclass(kw_only=True)
class Guest(BaseEntity):
    name : str
    place : str
    address : str
    email : str
    phone : int
    id_card : IDCard
    
    id_card_num : str
    id_card_image_path : str

    room : Room

    check_in : datetime
    check_out : datetime

    status : BookingStatus
    payment : PaymentStatus

    guest_photo_path: Optional[str] = None
    


    def __post_init__(self):
        req_fields = ['name', 'place', 'email', 'phone', 'address','id_card_num',
                      'id_card_image_path','id_card','room','check_in','check_out','status','payment']
        missing_fields = [i for i in req_fields if  getattr(self, i) is None]

        if missing_fields:
           raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        
        if not isinstance(self.id_card, IDCard):
            raise TypeError(f"id_card must be an IDCard enum, got {type(self.id_card)}")
        
        if not isinstance(self.room, Room):
            raise TypeError(f"Room must be an Room instance, got {type(self.room)}")
        
        if not isinstance(self.status, BookingStatus):
            raise TypeError(f"status must be a BookingStatus enum, got {type(self.status)}")
        
        if not isinstance(self.payment, PaymentStatus):
            raise TypeError(f"payment must be a PaymentStatus enum, got {type(self.payment)}")


    def duration(self) -> int:
        return (self.check_out - self.check_in).days
    

    def is_checked_in(self) -> bool:
        return self.status == BookingStatus.CHECKED_IN
    
    def is_checked_out(self) -> bool:   
        return self.status == BookingStatus.CHECKED_OUT
    
    def mark_checked_in(self) -> None:
        if self.status != BookingStatus.CONFIRMED:
            raise ValueError("Guest booking is not confirmed")
        self.status = BookingStatus.CHECKED_IN

    def mark_checked_out(self) -> None:
        if self.status != BookingStatus.CHECKED_IN:
            raise ValueError("Guest is not checked in")
        self.status = BookingStatus.CHECKED_OUT
        self.room.mark_status(RoomStatus.MAINTENANCE)
        self.mark_inactive()


    def mark_cancelled(self) -> None:
        if self.status == BookingStatus.CANCELLED:
            raise ValueError("Guest booking is already cancelled")
        self.status = BookingStatus.CANCELLED

