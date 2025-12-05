from .base import BaseEntity
from enum import Enum
from dataclasses import dataclass
from app.domain.exceptions.users_exceptions import UserIsAdmin
from .enums import Role


@dataclass(kw_only=True)
class User(BaseEntity):
    name : str
    email : str
    password : str
    phone : int
    role : Role = Role.STAFF

    def __post_init__(self):
        if not isinstance(self.role, Role):
            raise TypeError(f'Role must be a Role enum ,got {type(self.role)}')

    def is_admin(self) -> bool:
        return self.role == Role.ADMIN
    

    def make_admin(self) -> None:
        if self.role == Role.ADMIN:
            raise UserIsAdmin("The User is admin")
        self.role =Role.ADMIN

    
    
a = User(name="amal",email="a@gmail.com",phone=1234,role=Role.ADMIN,password="asdasd")

print(a.role)
print(a.is_admin())
