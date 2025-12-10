from dataclasses import dataclass
from typing import Optional

from .base import BaseEntity
from .guests import Guest
from .booking_room import BookingRoom




@dataclass(kw_only=True)
class BookingGuest(BaseEntity):
    booking_room: BookingRoom
    guest: Guest
    is_primary: bool = False     
    id_card_image_path: Optional[str] = None
    guest_photo_path: Optional[str] = None
