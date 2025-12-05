from .base_repository import BaseRepository
from app.domain.entities.rooms import Room

class RoomRepository(BaseRepository[Room]):

    async def get_by_number(self, number: int) -> Room:
        pass

    async def list_by_status(self, status) -> list[Room]:
        pass

    async def list_by_category(self, category) -> list[Room]:
        pass