from .base_repository import BaseRepository
from app.domain.entities.booking_room import BookingRoom
from typing import List,Optional




class  BookingRoomRepository(BaseRepository[BookingRoom]):

    async def list_by_booking_id(self, booking_id: str) -> List[BookingRoom]:
        pass

    async def list_by_room_id(self, room_id: str) -> List[BookingRoom]:
        pass

    async def get_by_booking_and_room(self, booking_id: str, room_id: str) -> Optional[BookingRoom]:
        pass