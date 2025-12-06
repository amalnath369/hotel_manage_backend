from dataclasses import dataclass
from .enums import RoomType,RoomStatus,ACType
from .base import BaseEntity


@dataclass(kw_only=True)
class Room(BaseEntity):
    room_number : str
    room_type : RoomType
    ac_or_non_ac : ACType
    floor : int
    status : RoomStatus = RoomStatus.AVAILABLE

    def __post_init__(self):
        if not self.room_number:
            raise ValueError("Room number cannot be empty")
        
        if self.floor <= 0:
            raise ValueError("Floor must be a positive integer")
        
        if not isinstance(self.room_type, RoomType):
            raise TypeError(f"room_type must be a RoomType enum, got {type(self.room_type)}")
        
        if not isinstance(self.ac_or_non_ac, ACType):
            raise TypeError(f"ac_or_non_ac must be an ACType enum, got {type(self.ac_or_non_ac)}")
        
        if not isinstance(self.status, RoomStatus):
            raise TypeError(f"status must be a RoomStatus enum, got {type(self.status)}")
        
    
    

if __name__ == "__main__":
    a= Room(floor=1,room_number=125,room_type=RoomType.SINGLE,ac_or_non_ac=ACType.AC)
        
    print(a.floor)
    print(a.ac_or_non_ac)
    print(a.is_active)
    print(a.status)
    a.mark_status("available")
    print(a.status)
