from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')



class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    async def get_by_id(self, id) -> T:
        pass
    
    @abstractmethod
    async def list_all(self) -> List[T]:
        pass

    @abstractmethod
    async def save(self, entity) -> T:
        pass    

    @abstractmethod
    async def update(self, entity) -> T:
        pass


    @abstractmethod
    async def delete(self, entity) -> T:
        pass

