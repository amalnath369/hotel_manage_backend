from .base_repository import BaseRepository
from app.domain.entities.users import User


class UserRepository(BaseRepository[User]):

    async def get_by_email(self, email: str) -> User:
        pass
