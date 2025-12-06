from app.domain.entities.rooms import Room
from app.domain.repositories.room_repository import RoomRepository
from app.domain.entities.enums import RoomType, RoomStatus, ACType
from app.domain.exceptions.rooms_exceptions import RoomAlreadyInStatus
from typing import List, Optional



class RoomServices:
    def __init__(self, room_repository: RoomRepository):
        self.room_repository = room_repository

    async def create_room(self, room_number: str, room_type: RoomType, ac_or_non_ac: ACType, 
                          floor: int, status: Optional[RoomStatus] = RoomStatus.AVAILABLE) -> Room:
        existing_room = await self.room_repository.get_by_number(room_number)
        if existing_room:
            raise ValueError("Room with this number already exists.")
        
        room = Room(room_number=room_number, room_type=room_type, 
                    ac_or_non_ac=ac_or_non_ac, floor=floor, status=status)
        await self.room_repository.save(room)
        return room
    

    async def room_category(self, room: Room) -> str:
        return room.room_type.value


    async def is_room_ac(self, room: Room) -> bool:
        return room.ac_or_non_ac == ACType.AC


    # --- AC Type Methods ---


    async def make_room_ac(self, room: Room) -> str:
        if room.ac_or_non_ac == ACType.AC:
            return "Room is already AC"
        room.ac_or_non_ac = ACType.AC
        return "Room converted to AC"

    async def make_room_non_ac(self, room: Room) -> str:
        if room.ac_or_non_ac == ACType.NON_AC:
            return "Room is already Non AC"
        room.ac_or_non_ac = ACType.NON_AC
        return "Room converted to Non AC"
    

    async def is_room_ac(self, room: Room) -> bool:
        return room.ac_or_non_ac == ACType.AC

    async def room_category(self, room: Room) -> str:
        return room.room_type.value
    

     # --- Status Methods ---
    async def mark_status(self, room: Room, new_status: RoomStatus) -> str:
        if not isinstance(new_status, RoomStatus):
            raise TypeError(f"new_status must be RoomStatus enum, got {type(new_status)}")
        if room.status == new_status:
            raise RoomAlreadyInStatus("Room is already in that status")
        room.status = new_status
        return f"Room status updated to {new_status.value}"