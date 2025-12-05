from .base_repository import BaseRepository
from app.domain.entities.booking import Booking



class BookingRepository(BaseRepository[Booking]):

    async def get_by_guest_id(self, guest_id: str) -> Booking:
        pass

    async def list_by_status(self, status) -> list[Booking]:
        pass

    async def list_by_check_in_date(self, check_in_date: str) -> list[Booking]:
        pass

    async def list_by_check_out_date(self, check_out_date: str) -> list[Booking]:
        pass