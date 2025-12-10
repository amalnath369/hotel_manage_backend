from dataclasses import dataclass
from typing import Optional

from .base import BaseEntity
from .booking import Booking
from .guests import Guest




@dataclass(kw_only=True)
class BookingGuest(BaseEntity):
    booking: Booking
    guest: Guest
    is_primary: bool = False     
    id_card_image_path: Optional[str] = None
    guest_photo_path: Optional[str] = None
