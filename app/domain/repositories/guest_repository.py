from .base_repository import BaseRepository
from app.domain.entities.guests import Guest
from typing import List

class BlacklistGuestRepository(BaseRepository[Guest]):

    async def get_by_phone(self, phone: int) -> Guest:
        pass

    async def list_by_name(self, name: str) -> List[Guest]:
        pass

    async def list_by_email(self, email: str) -> List[Guest]:
        pass

    

class GuestRepository(BaseRepository[Guest]):

    async def get_by_phone(self, phone: int) -> Guest:
        pass

    async def list_by_name(self, name: str) -> List[Guest]:
        pass

    async def list_by_email(self, email: str) -> List[Guest]:
        pass