from dataclasses import dataclass
from .base import BaseEntity
from .rooms import Room
from .enums import IDCard
from typing import Optional

@dataclass(kw_only=True)
class Guest(BaseEntity):
    name : str
    place : str
    address : str
    id_card : IDCard
    id_card_num : str

    id_card_image : str