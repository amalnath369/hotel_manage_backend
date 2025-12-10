from app.domain.entities.users import User
from app.domain.repositories.user_repository import UserRepository
from app.domain.exceptions.users_exceptions import UserAlreadyExists
from typing import Optional,List
from app.auth import hash_password


class UserServices:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self,name: str, email: str, password: str, phone: int) -> User:
        try:
            existing_user = await self.user_repository.get_by_email(email)
            if existing_user:
                raise UserAlreadyExists("A user with this email already exists.")
            
            hashed_password = hash_password(password)
            user = User(name=name, email=email, password=hashed_password, phone=phone)
            await self.user_repository.save(user)
            return user
        except Exception as e:
            raise e
    

    async def make_user_admin(self, user_id: str) -> User:
        try:
            user = await self.user_repository.get_by_id(user_id)
            if not user:
                raise ValueError("User not found")
            
            if user.is_admin():
                raise ValueError("User is already an admin")
            
            user.make_admin()
            await self.user_repository.update(user)
            return user
        except Exception as e:
            raise e