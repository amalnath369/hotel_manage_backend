from .base_repository import BaseRepository
from app.domain.entities.booking_guest import BookingGuest
from typing import List,Optional



class  BookingGuestRepository(BaseRepository[BookingGuest]):

    async def list_by_booking_room_id(self, booking_room_id: str) -> List[BookingGuest]:
        pass

    async def list_by_guest_id(self, guest_id: str) -> List[BookingGuest]:
        pass

    async def get_primary_guest_by_booking_room_id(self, booking_room_id: str) -> Optional[BookingGuest]:
        pass