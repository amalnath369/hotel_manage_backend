from dataclasses import dataclass
from .base import BaseEntity
from .users import User
from .rooms import Room
from .enums import IDCard
from typing import Optional




@dataclass(kw_only=True)
class BlacklistGuest(BaseEntity):
    name : str
    email : str
    phone : int
    reason : str
    id_card :  IDCard
    id_card_num : str
    id_card_image_path : Optional[str] = None
    guest_photo_path: Optional[str] = None



@dataclass(kw_only=True)
class Guest(BaseEntity):
    name : str
    place : str
    address : str
    email : str
    phone : int
    id_card : IDCard
    
    id_card_num : str
    id_card_image_path : str

    guest_photo_path: Optional[str] = None
    


    def __post_init__(self):
        req_fields = ['name', 'place', 'email', 'phone', 'address','id_card_num',
                      'id_card_image_path','id_card']
        missing_fields = [i for i in req_fields if  getattr(self, i) is None]

        if missing_fields:
           raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        
        if not isinstance(self.id_card, IDCard):
            raise TypeError(f"id_card must be an IDCard enum, got {type(self.id_card)}")
        

